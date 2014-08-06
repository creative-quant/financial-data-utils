import requests

class CurrencyError(Exception) :
        """Sorry Currency not support."""
        pass

class Service :

    libor_urls = { 'usd': 'http://www.global-rates.com/interest-rates/libor/american-dollar/american-dollar.aspx' }

    def getResponse ( self, currency ) :

        try :
            url = self.libor_urls[ currency ]
            return requests.get( url )
        except KeyError :
            raise CurrencyError
