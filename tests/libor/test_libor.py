import pytest
from financial_data_utils.libor.libor import Libor
from datetime import date
import requests

class TestLibor :

    def testGetUSD (self, monkeypatch) :

        class Object :
            pass

        def test_request (url) :
            obj = Object()
            obj.text = open( 'tests/data/american-dollar.html', 'r' ).read()
            return obj

        monkeypatch.setattr( requests, 'get', test_request )

        libor = Libor().getUSD()

        assert libor.date == date(2014, 8, 1)
        assert libor.overnight == 0.08990
        assert libor.week == 0.12200
        assert libor.month == 0.15600
        assert libor.month2 == 0.19775
        assert libor.month3 == 0.23810
        assert libor.month6 == 0.33440
        assert libor.month12 == 0.57810


