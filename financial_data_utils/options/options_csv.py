
from .yahoo_finance import YahooFinance

class OptionsCSV () :

    def write ( self, lastTrade, options ) :

        dt = lastTrade.datetime.isoformat()
        dt = str.replace( str.replace(dt,':',''), '-', '' )
        f = open( lastTrade.symbol + '_' + dt + '_' + str( lastTrade.close ) + '.csv','w')
        f.write('symbol,strike,last,chg,bid,ask,vol,openInt\n')

        for option in options :

            f.write( option.symbol + "," )
            f.write( '{0},'.format( option.strikePrice ) )
            f.write( '{0},'.format( option.lastPrice ) )
            f.write( '{0},'.format( option.change ) )
            f.write( '{0},'.format( option.bid ) )
            f.write( '{0},'.format( option.ask ) )
            f.write( '{0},'.format( option.vol ) )
            f.write( '{0}'.format( option.openInt ) )
            f.write('\n')

        f.close()
