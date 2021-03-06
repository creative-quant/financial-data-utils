from financial_data_utils.options.yahoo.service import Service
import xml.etree.ElementTree as ET
import datetime
from string import Template
import math
from collections import namedtuple

LastTrade = namedtuple("LastTrade", ['symbol', 'close', 'datetime'])
Option = namedtuple("Option", ['symbol', 'strikePrice', 'lastPrice', 'change', 'bid', 'ask', 'vol', 'openInt' ])

class Finance :

    def getLastTrade ( self, symbol, yql ) :

        q = Template( 'select LastTradePriceOnly,LastTradeTime,LastTradeDate from yahoo.finance.quotes where symbol = \'$symbol\'' )
        response = Service().getResponse( q.substitute( {'symbol':symbol} ) )
        root_node = ET.fromstring( response.text )
        date = root_node.find( "./results/quote/LastTradeDate" ).text
        time = root_node.find( "./results/quote/LastTradeTime" ).text
        return LastTrade(  symbol,
            self.getFloat( root_node.find( "./results/quote/LastTradePriceOnly" ).text ),
            datetime.datetime.strptime(date + " " + time, "%m/%d/%Y %I:%M%p") )

    def getOptions ( self, symbol, yql ) :

        q = Template( 'SELECT * FROM yahoo.finance.options WHERE symbol=\'$symbol\' AND expiration in (SELECT contract FROM yahoo.finance.option_contracts WHERE symbol=\'$symbol\')' )
        response = Service().getResponse( q.substitute( {'symbol':symbol} ) )
        root_node = ET.fromstring( response.text )
        options = []
        for option in root_node.findall( ".//optionsChain[@symbol='"+symbol+"']/option" ):

            options.append( Option( option.get("symbol"),
                self.getFloat( option.find("strikePrice").text ),
                self.getFloat( option.find("lastPrice").text ),
                self.getFloat( option.find("change").text ),
                self.getFloat( option.find("bid").text ),
                self.getFloat( option.find("ask").text ),
                self.getInt( option.find("vol").text ),
                self.getInt( option.find("openInt").text ) ) )

        return options


    def getFloat ( self, value ) :
        try :
            f = float( value or 0 )
            if math.isnan( f ) :
                return 0
            return f
        except ValueError :
            return 0


    def getInt ( self, value ) :
        try :
            i = int( value or 0 )
            if math.isnan( i ) :
                return 0
            return i
        except ValueError :
            return 0
