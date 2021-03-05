import requests
from bs4 import BeautifulSoup

version = 2.2
print("Version No. %.1f" % version)
print("Only bids and cards you don't have at the moment. May add more stuff later.")

region = input("What region are you searching? ")
nation = input("What nation are you collecting from? ")
bids = input("Are you looking for the cards to bid on? (yes/no) ")
season = input("What season are you looking for? Integers only please. ")

# sanitization, I think?
region = region.lower().replace(" ", "_")
nation = nation.lower().replace(" ", "_")
bidsTrue = bids.lower().startswith('y')

# with open('card_list.txt') as f:
# 	puppets = f.read().split('\n')

# puppets = list(filter(None, puppets))

# I wish Python had switch statements :(
if int(season) == 1 or int(season) == 2:
    print("...")
elif int(season) > 3:
	print("Season %d does not exist!" % season)
elif int(season) == 3:
	print("S3 will never come.")	
elif int(season) <= 0:
	print("No.")
else:
    print("You broke the code! >:(")

print('Running...accessing r3n\'s server')
# query = 'http://azure.nsr3n.info/card_queries/get_daemon.sh?query=%2Bregion%3Athe_east_pacific%0D%0A-deck%3As1_tep_collector&season=1&format=full&submit=submit' # for S1
# query = 'http://azure.nsr3n.info/card_queries/get_daemon.sh?query=%2Bregion%3Athe_east_pacific%0D%0A-deck%3As2_tep_collector&season=2&format=full&submit=submit' # for S2
if bidsTrue:
	query = 'http://azure.nsr3n.info/card_queries/get_daemon.sh?query=%2Bregion%3A' + region + '%0D%0A-deck%3A' + nation + '%0D%0A-bid%3A' + nation + '&season=' + season + '&format=full&submit=submit'
else:
	query = 'http://azure.nsr3n.info/card_queries/get_daemon.sh?query=%2Bregion%3A' + region + '%0D%0A-deck%3A' + nation + '&season=' + season + '&format=full&submit=submit'

reqs = requests.get(query)
soup = BeautifulSoup(reqs.text, 'html.parser')
print("Done!")

with open('query_links.txt', 'w') as f:
	for link in soup.find_all('a'):
		f.write('\n' + link.get('href') + '/pull_event_card')