
class YQLService () :

    url = 'http://query.yahooapis.com/v1/public/yql'
    params = { 'env' : 'store://datatables.org/alltableswithkeys' }

    def createParams ( self, yql ) :
        d = self.params.copy()
        d.update( {'q': yql } )
        return d
