from financial_data_utils.libor.globalrates.service import Service
from financial_data_utils.libor.globalrates.parser import ParserHeaders, ParserValues
from collections import namedtuple
import datetime


class Libor :

    Libor = namedtuple("Libor", ['date', 'overnight', 'week', 'month', 'month2', 'month3', 'month6', 'month12' ])

    def getUSD ( self ) :

        text = Service().getResponse( 'usd' ).text

        ph = ParserHeaders()
        ph.feed( text )
        headers = ph.headers

        pv = ParserValues()
        pv.feed( text )

        return Libor.Libor( datetime.datetime.strptime( pv.values[ 0 ], '%m-%d-%Y' ).date(),
                      float( pv.values[ headers.index( 'overnight' )+1 ] ),
                      float( pv.values[ headers.index( '1 week' )+1 ] ),
                      float( pv.values[ headers.index( '1 month' )+1 ] ),
                      float( pv.values[ headers.index( '2 months' )+1 ] ),
                      float( pv.values[ headers.index( '3 months' )+1 ] ),
                      float( pv.values[ headers.index( '6 months' )+1 ] ),
                      float( pv.values[ headers.index( '12 months' )+1 ] ) )



