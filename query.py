import sys
import requests
from bs4 import BeautifulSoup

version = 4.0
print("Version No. %.1f" % version)

# if you want more flexibility, you can use the custom query
bidsTrue = False
nation = input("What nation are you collecting from? ").lower().replace(" ", "_")
season = -1
while season not in [0, 1, 2, 3]:
    season = input("What season are you looking for? (1 or 2, 0 for both) ")
    try:
        season = int(season)
    except ValueError:
        print("That's not a number!")
if season == 3:
	print("S3 will never come.")
	sys.exit()
custom = input("Do you want to make your own custom query? (yes/no) ").lower().startswith('y')
if not custom:
	region = input("What region are you searching? ").lower().replace(" ", "_")
	bids = input("Are you looking for the cards to bid on? (yes/no) ")
	if bids.lower().startswith('y'):
		bidsTrue = True

open("query_links.txt", "w")
if season != 0:
	if custom:
		posted_query = input("Please enter your query using the Advanced Cards Queries syntax: ")
		processed_query = posted_query.replace(":", "%3A").replace("&", "%26").replace("!", "%21").replace("|", "%7C").replace(" ", "+").replace("(", "%28").replace(")", "%29")
		query = f'http://azure.nsr3n.info/card_queries/get_daemon_advanced.sh?format=full&query={processed_query}&season={season}&format=full&submit=submit'
	elif bidsTrue:
		query = f'http://azure.nsr3n.info/card_queries/get_daemon_advanced.sh?format=full&query=region%3A{region}%26%21deck%3A{nation}%26%21bid%3A{nation}&season={season}&format=full&submit=submit'
	else:
		query = f'http://azure.nsr3n.info/card_queries/get_daemon_advanced.sh?format=full&query=region%3A{region}%26%21deck%3A{nation}&season={season}&format=full&submit=submit'

	print('Running...accessing r3n\'s server')
	reqs = requests.get(query)
	soup = BeautifulSoup(reqs.text, 'html.parser')
	print("Finished accessing r3n\'s server")

	print("Writing the output of said query into file")
	with open('query_links.txt', 'a') as f:
		cards = []
		a = soup.find_all('a')
		for i in range(1, len(a)):
			f.write('\n' + a[i].get('href') + '/pull_event_card')
			cards.append(a[i].get('href'))
else:
	while season < 2:
		season += 1
		if custom:
			posted_query = input(f"Please enter your query using the Advanced Cards Queries syntax for Season {season}: ")
			processed_query = posted_query.replace(":", "%3A").replace("&", "%26").replace("!", "%21").replace("|", "%7C").replace(" ", "+").replace("(", "%28").replace(")", "%29")
			query = f'http://azure.nsr3n.info/card_queries/get_daemon_advanced.sh?format=full&query={processed_query}&season={season}&format=full&submit=submit'
		elif bidsTrue:
			query = f'http://azure.nsr3n.info/card_queries/get_daemon_advanced.sh?format=full&query=region%3A{region}%26%21deck%3A{nation}%26%21bid%3A{nation}&season={season}&format=full&submit=submit'
		else:
			query = f'http://azure.nsr3n.info/card_queries/get_daemon_advanced.sh?format=full&query=region%3A{region}%26%21deck%3A{nation}&season={season}&format=full&submit=submit'
		
		print('Running...accessing r3n\'s server')
		reqs = requests.get(query)
		soup = BeautifulSoup(reqs.text, 'html.parser')
		print("Finished accessing r3n\'s server")

		print("Writing the output of said query into file")
		with open('query_links.txt', 'a') as f:
			a = soup.find_all('a')
			for i in range(1, len(a)-1):
				f.write(a[i].get('href') + '\n')
			f.write(a[len(a)-1].get('href'))

links = open('table.html', 'w')
print("Opened HTML")
links.write("""
<html>
<head>
<style>
td.createcol p {
	padding-left: 10em;
}

a {
	text-decoration: none;
	color: black;
}

a:visited {
	color: grey;
}

table {
	border-collapse: collapse;
	display: table-cell;
	max-width: 100%;
	border: 1px solid darkorange;
}

tr, td {
	border-bottom: 1px solid darkorange;
}

td p {
	padding: 0.5em;
}

tr:hover {
	background-color: lightgrey;
}

</style>
</head>
<body>
<table>
""")

#containerise_rules.write("@^.*\.nationstates\.net/(.*/)?nation=9003(/.*)?$ , 9003\n")
for c in cards:
	
	links.write('   <tr><td><p><a target="_blank" href="{}">Link to Card</a></p></td></tr>\n'.format(c + f"/nation={nation}/container={nation}"))
	print("Added %s" % c)

links.write("""   <tr><td><p><a target="_blank" href="https://this-page-intentionally-left-blank.org/">Done!</a></p></td></tr>
</table>
<script>
document.querySelectorAll("td").forEach(function(el) {
	el.addEventListener("click", function() {
		let myidx = 0;
		const row = el.parentNode;
		let child = el;
		while((child = child.previousElementSibling) != null) {
			myidx++;
		}
		row.nextElementSibling.childNodes[myidx].querySelector("p > a").focus();
		row.parentNode.removeChild(row);
	});
});
</script>
</body>
</html>
""")
links.close
print("Closed HTML")