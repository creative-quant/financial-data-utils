from financial_data_utils.earnings.yahoo.parser import Parser
from financial_data_utils.earnings.yahoo.service import Service

class Earnings :

    def getByDate ( self, date ) :

        p = Parser()
        data = Service().getResponse( data )
        p.feed( data )
        return p.earnings
