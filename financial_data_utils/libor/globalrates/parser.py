try:
    from HTMLParser import HTMLParser
except ImportError:
    from html.parser import HTMLParser

class ParserHeaders(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.flag_count = 0
        self.headers = []
        #headers_start_index = 11
        #'USD LIBOR - overnight' == 'overnight'
        self.headers_start_index = 12

    def handle_starttag(self, tag, attrs):

        if tag == "tr" :
            d = dict( attrs )
            if 'class' in d and d['class'] in ('tabledata1', 'tabledata2') :
                self.flag_count = 1
                return
        elif self.flag_count == 1 and tag == 'a' :
            d = dict( attrs )
            if 'class' in d and d['class'] == 'tabledatalink' :
                self.flag_count = 2
                return

    def handle_endtag(self, tag):
        if self.flag_count == 2 and tag == 'a' :
            self.flag_count = 0;

    def handle_data(self, data):
        if self.flag_count == 2 :

            self.headers.append( data[self.headers_start_index:] )


class ParserValues(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.column = 2
        self.values = []
        self.flag_count = 0

    def handle_starttag(self, tag, attrs):
        if tag == "tr" :
            d = dict( attrs )
            if 'class' in d and d['class'] in ( 'tableheader', 'tabledata1', 'tabledata2' ) :
                self.flag_count = 1
                return
        elif tag == 'td' and self.flag_count >= 1 :
            self.flag_count += 1
            return

    def handle_endtag(self, tag):
        if self.flag_count == self.column + 1 and tag == 'td' :
            self.flag_count = 0

    def handle_data(self, data):
        if self.flag_count == self.column + 1:
            self.values.append( data )
            self.flag_count = 0


