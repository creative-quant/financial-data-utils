import pytest
from financial_data_utils.earnings.yahoo.parser import Parser

@pytest.fixture
def earnings_response1 ():
    return open( 'tests/data/earnings01061999.html', 'r' ).read()

@pytest.fixture
def earnings_response2 ():
    return open( 'tests/data/earnings20141010.html', 'r' ).read()

class TestParser :

    def test_earnings1 (self) :

        p = Parser()
        p.feed( earnings_response1() )

        assert len( p.earnings ) == 1
        e = p.earnings[0]
        assert e.symbol == 'AMES'
        assert e.company == 'Ames Dept Stores'
        assert e.time == 'Time Not Supplied'

    def test_earnings2 (self) :

        p = Parser()
        p.feed( earnings_response2() )

        print( p.earnings )

        assert len( p.earnings ) == 4
        e = p.earnings[0]
        assert e.symbol == 'AVANCE.OL'
        assert e.company == 'Avance Gas Holding Ltd'
        assert e.time == 'Before Market Open'

        e = p.earnings[3]
        assert e.symbol == 'TRYG.CO'
        assert e.company == 'Tryg A/S'
        assert e.time == '01:30 am ET'
