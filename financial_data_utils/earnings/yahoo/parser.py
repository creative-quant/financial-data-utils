try:
    from HTMLParser import HTMLParser
except ImportError:
    from html.parser import HTMLParser
from collections import namedtuple

class HeaderParser ():

    def __init__(self,headers,onDone):
        self.state = 0
        self.headers = headers
        self.index = 0
        self.onDone = onDone

    def handle_starttag(self, tag, attrs):
        t = tag.lower()
        if t == 'tr' and self.state == 0:
            self.state = 1
            self.index = 0
        elif t == 'td' and self.state == 1:
            self.state = 2

    def handle_data(self, data):
        if self.state == 2 :
            if data in self.headers :
                self.headers[data] = self.index
                if self.__hasHeaders() :
                    self.onDone( self.headers )

    def handle_endtag(self,tag):
        if self.state == 1 and tag == "tr" :
            self.index = self.state = 0
        if self.state == 2 and tag == "td" :
            self.state = 1
            self.index += 1

    def __hasHeaders (self):
        for v in self.headers.values() :
            if v == -1 :
                return False
        return True

Earning = namedtuple("Earning", ['symbol', 'company', 'time'])

class EarningParser :

    def __init__ (self,headers) :
        self.earnings = []
        self.__reset()
        self.headers = headers

    def __reset ( self ) :
        self.symbol = self.company = self.time = ''
        self.headerIndex = self.state = 0

    def handle_starttag(self, tag, attrs):
        t = tag.lower()
        if t == 'tr' and self.state == 0:
            self.state = 1
        elif t == 'td' and self.state == 1:
            self.state = 2

    def handle_data(self, data):
        if self.state == 2 :
            if self.headerIndex == self.headers['Company'] :
                self.company = data.replace('\n', ' ').strip()
            elif self.headerIndex == self.headers['Symbol'] :
                self.symbol = data.strip()
            elif self.headerIndex == self.headers['Time'] :
                self.time = data.strip()

    def handle_endtag(self,tag):
        if tag == 'tr' :
            if self.symbol and self.company and self.time :
                self.earnings.append( Earning( self.symbol, self.company, self.time ) )
            self.__reset()
        if tag == 'td' :
            self.headerIndex += 1

class Parser (HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.parser = HeaderParser({'Company':-1,'Symbol':-1,'Time':-1}, self.onHeaders )
        self.earnings = []

    def onHeaders (self, headers ) :
        self.parser = EarningParser( headers )
        self.earnings = self.parser.earnings

    def handle_starttag(self, tag, attrs):
        self.parser.handle_starttag( tag, attrs )

    def handle_data(self, data):
        self.parser.handle_data( data )

    def handle_endtag(self,tag):
        self.parser.handle_endtag(tag)

