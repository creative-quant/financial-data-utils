from financial_data_utils.options.yahoo.service import Service
from financial_data_utils.options.yahoo.finance import Finance

class Options :

    def getBy ( self, symbol ) :
        yql = Service()
        f = Finance()
        return f.getOptions( symbol, yql )

    def getLastTrade ( self, symbol ) :
        yql = Service()
        f = Finance()
        return f.getLastTrade( symbol, yql )
