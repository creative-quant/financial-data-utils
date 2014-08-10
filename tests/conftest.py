import pytest
import requests


class Object(object):
    pass

@pytest.fixture
def lasttrade_request (monkeypatch) :

    def foo () :

        def test_request (url, params) :
            obj = Object()
            obj.text = """<?xml version="1.0" encoding="UTF-8"?>
                <query xmlns:yahoo="http://www.yahooapis.com/v1/base.rng" yahoo:count="1" yahoo:created="2014-07-23T16:32:20Z" yahoo:lang="en-US"><results><quote><LastTradeDate>7/23/2014</LastTradeDate><LastTradePriceOnly>193.95</LastTradePriceOnly><LastTradeTime>12:17pm</LastTradeTime></quote></results></query><!-- total: 495 -->
                <!-- engine7.yql.bf1.yahoo.com -->"""
            return obj

        monkeypatch.setattr( requests, 'get', test_request )

    return foo()


@pytest.fixture
def options_request (monkeypatch) :

    def option_response ():
        return open( 'tests/data/option_query.xml', 'r' ).read()

    def foo () :

        def test_request (url,params) :
            obj = Object()
            obj.text = option_response()
            return obj

        monkeypatch.setattr( requests, 'get', test_request )

    return foo()

