from .yql_service import YQLService
from .yahoo_finance import YahooFinance
from .options_csv import OptionsCSV


class YahooOptions :

    def __init__ ( self, symbol ) :

        yql = YQLService()
        yf = YahooFinance()
        OptionsCSV().write(     yf.getLastTrade( symbol, yql ),
                                                yf.getOptions( symbol, yql ) )
