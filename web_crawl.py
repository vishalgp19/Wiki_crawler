from urllib.parse import urljoin
from bs4 import BeautifulSoup
from urllib.request import urlopen
import sqlite3


connect = sqlite3.connect("Crawl.sqlite")
cur = connect.cursor()

cur.execute(" CREATE TABLE IF NOT EXISTS Crawl(Title TEXT, Hyperlink TEXT) ")

base_url = 'https://en.wikipedia.org/wiki/'
url_input = input('Enter wiki topic: ').split()
url_input = "_".join(url_input)

url = base_url + url_input
html = urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
tables = soup('a')

for link in tables:
    title = link.text
    
    unwanted=['', '.', '[', 'External links and resources',
                            'External links',
                            'Jump to search',
                            'Jump to navigation',
                            'Navigation menu',
                            'See also',
                            'References',
                            'Further reading',
                            'Contents',
                            'Official',
                            'Other',
                            'Notes',
                            'Bibliography',
                            'Awards and honors',
                            'Terms of use',
                            'Privacy policy',
                            'Wikipedia About',
                            'General dis',
                            'Contact us',
                            'How to contribute',
                            'Cookie statement,',
                            'en.wikipedia',
                            'wikipedia',
                            'archive',
                            '978-0-85496-695-0',
                            'ISBN',
                            'Terms of Use',
                            'Privacy Policy',
                            'Wikimedia Foundation, Inc.',
                            'About Wikipedia',
                            'Disclaimers',
                            'Contact Wikipedia',
                            'Mobile view',
                            'Developers',
                            'Statistics',
                            'Cookie statement']

    if title in unwanted or len(title) == (1 or 0) or title[0] in ['[', '.'] :
        continue

    link = link.get('href', None)
    link = urljoin(url, link)

    cur.execute('''INSERT INTO Crawl(Title, Hyperlink) VALUES(?,?) ''', (title,link))

    print(link)
connect.commit()
