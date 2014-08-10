import pytest
from financial_data_utils.earnings.yahoo.service import Service
import requests

class TestService :

    def test_getResponse (self) :

        s = Service()
        with pytest.raises( ValueError ) :
            s.getResponse( "11" )

        with pytest.raises( ValueError ) :
            s.getResponse( "19790101" )

        with pytest.raises( ValueError ) :
            s.getResponse( "19990105" )

        assert isinstance( s.getResponse("19990106"), requests.Response )
        assert isinstance( s.getResponse("20140101"), requests.Response )


