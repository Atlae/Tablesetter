#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup


html_start = """
<html>
<head>
	<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
	<style>
	td.createcol p {
		padding-left: 10em;
	}
	a {
		text-decoration: none;
		color: #E8E6E3;
	}
	a:visited {
		color: #181A1B;
	}
	table {
		border-collapse: collapse;
		display: table-cell;
		max-width: 100%;
		border: 1px solid #00D9D9;
	}
	tr, td {
		border-bottom: 1px solid #008080;
	}
	td p {
		padding: 0.5em;
	}
	tr:hover {
		background-color: #313537;
	}
	</style>
</head>
<body>
<table>
"""

html_end = """
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
"""

query = input('Please enter your query using the Advanced Cards Queries syntax: ')
cardlinks = open('card_sheet.html', 'w')
with open('puppets.txt') as p:
	puppets = p.read().split('\n')

cardlinks.write(html_start)

for puppet in puppets:
	cards = []
	canonical = puppet.lower().replace(" ", "_")
	print(f'Retrieving {puppet}\'s deck...')
	r = requests.get('https://azure.nsr3n.info/card_queries/get_daemon_advanced.sh?format=full', params={'query':f'deck:{canonical}&' + f'{query}','season':'2','format':'full','submit':'submit'})
	soup = BeautifulSoup(r.text, 'lxml')
	a = soup.find_all('a')
	for i in range(1,len(a)):
		print(a[i].attrs['href'])
		cards.append(a[i].attrs['href'])
	for link in cards:
		containerLink = link + f'/nation={canonical}/container={canonical}/'
		cardlinks.write(f'<tr><td><p><a target="_blank" href="{containerLink}">Link to {puppet}\'s Card</a></p></td></tr>\n')

cardlinks.write(html_end)