import requests
from bs4 import BeautifulSoup


# with open('card_list.txt') as f:
# 	puppets = f.read().split('\n')

# puppets = list(filter(None, puppets))

query = 'http://azure.nsr3n.info/card_queries/get_daemon.sh?query=%2Bregion%3Athe_east_pacific%0D%0A-deck%3As2_tep_collector&season=2&format=full&submit=submit'
reqs = requests.get(query)
soup = BeautifulSoup(reqs.text, 'html.parser')

with open('query_links.txt', 'w') as f:
	for link in soup.find_all('a'):
		f.write('\n' + link.get('href'))