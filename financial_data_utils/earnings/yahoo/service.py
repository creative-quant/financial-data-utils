import datetime
import requests

class Service :

    def getResponse ( self, date ) :

        try:
            dt = datetime.datetime.strptime(date, '%Y%m%d')
        except ValueError:
            raise ValueError("Incorrect date format, should be YYYYMMDD")

        if dt.date() < datetime.date(1999, 1, 6 ) :
            raise ValueError("Date should be > 1999-01-05")

        return requests.get( 'http://biz.yahoo.com/research/earncal/' + date + ".html" )

