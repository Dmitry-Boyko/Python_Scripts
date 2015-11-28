from bs4 import BeautifulSoup
import time
import urllib2
from dbconnect import connection


req = urllib2.urlopen('http:/www.nation...')

xml = BeautifulSoup(req, 'xml')

c, conn = connection()

for item in xml.findAll('link')[3:]:
    url = item.text
    c.execute('INSERT ITO links (time, link) VALUES (%s, %s)',
              (time.time(), url))
    conn.commit()

conn.close()