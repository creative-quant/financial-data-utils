import pytest
from financial_data_utils.options.yahoo_finance import YahooFinance
from financial_data_utils.options.yql_service import YQLService
import requests
import datetime
import os

@pytest.fixture
def option_response ():
    return open( 'tests/data/option_query.xml', 'r' ).read()

class TestYahooFinance :

    class Object(object):
        pass

    def setup_method(self, method) :
        self.yf = YahooFinance()
        self.yql = YQLService()

    def testGetLastTrade (self, monkeypatch) :

        def test_request (url, params) :
            obj = TestYahooFinance.Object()
            obj.text = """<?xml version="1.0" encoding="UTF-8"?>
                <query xmlns:yahoo="http://www.yahooapis.com/v1/base.rng" yahoo:count="1" yahoo:created="2014-07-23T16:32:20Z" yahoo:lang="en-US"><results><quote><LastTradeDate>7/23/2014</LastTradeDate><LastTradePriceOnly>193.95</LastTradePriceOnly><LastTradeTime>12:17pm</LastTradeTime></quote></results></query><!-- total: 495 -->
                <!-- engine7.yql.bf1.yahoo.com -->"""
            return obj

        monkeypatch.setattr( requests, 'get', test_request )

        ret = self.yf.getLastTrade( 'IBM', self.yql )
        dt = datetime.datetime(2014, 7, 23, 12, 17, 00)

        assert ret.symbol == 'IBM'
        assert ret.close == 193.95
        assert ret.datetime == dt

    def testGetOptions (self, monkeypatch) :

        def test_request (url,params) :
            obj = TestYahooFinance.Object()
            obj.text = option_response()
            return obj

        monkeypatch.setattr( requests, 'get', test_request )

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


    def testGetFlost (self, monkeypatch) :

        assert 0 == self.yf.getFloat( '0' )
        assert 0 == self.yf.getFloat( 'NaN' )
        assert 0 == self.yf.getFloat( 'foo' )

    def testGetInt (self, monkeypatch) :

        assert 0 == self.yf.getInt( '0' )
        assert 0 == self.yf.getInt( 'NaN' )
        assert 0 == self.yf.getInt( 'foo' )
