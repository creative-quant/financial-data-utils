import pytest
from financial_data_utils.options.yahoo.finance import Finance
from financial_data_utils.options.yahoo.service import Service
import datetime


class TestFinance :

    def setup_method (self,method) :
        self.yf = Finance()
        self.yql = Service()

    @pytest.mark.usefixtures("lasttrade_request")
    def testGetLastTrade (self):

        ret = self.yf.getLastTrade( 'IBM', self.yql )
        dt = datetime.datetime(2014, 7, 23, 12, 17, 00)

        assert ret.symbol == 'IBM'
        assert ret.close == 193.95
        assert ret.datetime == dt

    @pytest.mark.usefixtures("options_request")
    def testGetOptions (self) :

        ret = self.yf.getOptions( 'IBM', self.yql )

        opt = ret[0]
        assert opt.symbol ==  'IBM140725C00170000'
        assert opt.strikePrice == 170
        assert opt.lastPrice == 24.38
        assert opt.change == 0
        assert opt.bid == 22.3
        assert opt.ask == 25.25
        assert opt.vol == 10
        assert opt.openInt == 15

        opt = ret[-1]
        assert opt.symbol ==  'IBM160115P00280000'
        assert opt.strikePrice == 280
        assert opt.lastPrice == 96.06
        assert opt.change == 0
        assert opt.bid == 87.85
        assert opt.ask == 92
        assert opt.vol == 6
        assert opt.openInt == 6


    def testGetFlost (self)  :

        assert 0 == self.yf.getFloat( '0' )
        assert 0 == self.yf.getFloat( 'NaN' )
        assert 0 == self.yf.getFloat( 'foo' )

    def testGetInt (self) :

        assert 0 == self.yf.getInt( '0' )
        assert 0 == self.yf.getInt( 'NaN' )
        assert 0 == self.yf.getInt( 'foo' )
