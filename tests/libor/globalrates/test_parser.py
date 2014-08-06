import pytest
from financial_data_utils.libor.globalrates.parser import ParserHeaders, ParserValues

@pytest.fixture
def option_response ():
    return open( 'tests/data/american-dollar.html', 'r' ).read()


class TestParser :

    def testHeaderParser (self) :

        periods = [ 'overnight',
            '1 week',
            '2 weeks',
            '1 month',
            '2 months',
            '3 months',
            '4 months',
            '5 months',
            '6 months',
            '7 months',
            '8 months',
            '9 months',
            '10 months',
            '11 months',
            '12 months' ]

        ph = ParserHeaders()
        ph.feed( option_response() )

        assert len( ph.headers ) == len(periods)
        assert periods == ph.headers

    def testValueParserFirstRow(self) :

        pv = ParserValues()
        pv.feed( option_response() )

        first_row = ['08-01-2014', '0.08990', '0.12200', '-', '0.15600', '0.19775', '0.23810', '-', '-', '0.33440', '-', '-', '-', '-', '-', '0.57810']
        assert len( pv.values ) > 1
        assert first_row == pv.values

    def testValueParserLastRow(self) :

        pv = ParserValues()
        pv.column = 6
        pv.feed( option_response() )

        last_row = ['07-28-2014', '0.09070', '0.12175', '-', '0.15500', '0.19725', '0.23610', '-', '-', '0.32880', '-', '-', '-', '-', '-', '0.56360']
        assert len( pv.values ) > 1
        assert last_row == pv.values


