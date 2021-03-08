import requests
from bs4 import BeautifulSoup

version = 2.3
print("Version No. %.1f" % version)
print("Only bids and cards you don't have at the moment. May add more stuff later.")

region = input("What region are you searching? ")
nation = input("What nation are you collecting from? ")
bids = input("Are you looking for the cards to bid on? (yes/no) ")
season = 3
while season not in [1, 2]:
    season = input("What season are you looking for? (1 or 2) ")
    try:
        season = int(season)
    except ValueError:
        print("That's not a number!")
    except season == 3:
        print("S3 will never come.")

# sanitization, I think?
region = region.lower().replace(" ", "_")
nation = nation.lower().replace(" ", "_")
bidsTrue = bids.lower().startswith('y')

# with open('card_list.txt') as f:
# 	puppets = f.read().split('\n')

# puppets = list(filter(None, puppets))

print('Running...accessing r3n\'s server')
if bidsTrue:
	query = f'http://azure.nsr3n.info/card_queries/get_daemon_advanced.sh?format=full&query=region%3A{region}%26%21deck%3A{nation}%26%21bid%3A{nation}&season={season}&format=full&submit=submit'
else:
	query = f'http://azure.nsr3n.info/card_queries/get_daemon_advanced.sh?format=full&query=region%3A{region}%26%21deck%3A{nation}&season={season}&format=full&submit=submit'

reqs = requests.get(query)
soup = BeautifulSoup(reqs.text, 'html.parser')
print("Done!")
print("writing the output of said query into file")

with open('query_links.txt', 'w') as f:
	cards = []
	a = soup.find_all('a')
	for i in range(1, len(a)):
		f.write('\n' + a[i].get('href') + '/pull_event_card')
		cards.append(a[i].get('href'))

links = open('tep.html', 'w')
print("opened HTML")
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
	print("Added URL")

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
print("Wrote end")