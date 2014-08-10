import datetime
import pytest
from financial_data_utils.options.options import Options

class TestOptions :

    @pytest.mark.usefixtures("options_request")
    def testGetBy (self) :

        opts = Options().getBy( 'IBM' )
        opt = opts[0]
        assert opt.symbol ==  'IBM140725C00170000'
        assert opt.strikePrice == 170
        assert opt.lastPrice == 24.38
        assert opt.change == 0
        assert opt.bid == 22.3
        assert opt.ask == 25.25
        assert opt.vol == 10
        assert opt.openInt == 15

        opt = opts[-1]
        assert opt.symbol ==  'IBM160115P00280000'
        assert opt.strikePrice == 280
        assert opt.lastPrice == 96.06
        assert opt.change == 0
        assert opt.bid == 87.85
        assert opt.ask == 92
        assert opt.vol == 6
        assert opt.openInt == 6

    @pytest.mark.usefixtures("lasttrade_request")
    def testGetLastTrade (self) :

        lt = Options().getLastTrade( 'IBM' )
        dt = datetime.datetime(2014, 7, 23, 12, 17, 00)

        assert lt.symbol == 'IBM'
        assert lt.close == 193.95
        assert lt.datetime == dt


