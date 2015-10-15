import requests
from bs4 import BeautifulSoup
grp_rss = 'http://apps.shareholder.com/rss/rss.aspx?channels=8497&companyid=AMDA-E2NTR&sh_auth=755427199%2E0%2E0%2E42291%2Eb480161a3fdb5fdee40bf494f92ef669'
class trackie(object):
    def __init__(self):
        pass

    def rss_feed(self):
        r = requests.get(grp_rss)
        soup = BeautifulSoup(r.text)
        return [i.text for i in soup.find_all('title')][:3]
