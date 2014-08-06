import pytest
from financial_data_utils.libor.globalrates.service import Service, CurrencyError
import requests

class TestService :

    def testGetResponse(self) :

        s = Service()
        r = s.getResponse( 'usd' )
        assert isinstance( r, requests.Response )

        with pytest.raises( CurrencyError ) :
            s.getResponse( 'foo' )

