import requests

class Service () :

    url = 'http://query.yahooapis.com/v1/public/yql'
    params = { 'env' : 'store://datatables.org/alltableswithkeys' }

    def getResponse ( self, yql ) :
        d = self.params.copy()
        d.update( {'q': yql } )
        return requests.get( self.url, params=d )
