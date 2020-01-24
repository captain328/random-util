import pyodbc , json
import urllib.request

NAMES_URL = 'https://www.randomlists.com/data/names-surnames.json'
EMAILS_URL = 'https://www.randomlists.com/data/email.json'

def get_url_data(url):
    html = ''
    with urllib.request.urlopen(url) as response:
        html = response.read()
    return html

def get_random_users(count):
    # assume count is lower than names_url count
    names_data = json.loads(get_url_data(NAMES_URL))['data']
    return names_data[:count]

def get_random_emails(count):
    email_data = json.loads(get_url_data(EMAILS_URL))['data']
    un = email_data['un'] # user name for email
    dm = email_data['dm'] # domail for email
    un_cnt = len(un)
    dm_cnt = len(dm)
    return [(un[i % un_cnt]+'@'+dm[i % dm_cnt]) for i in range(count)]
