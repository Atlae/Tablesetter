# Tablesetter
---

This tablesetter program queries r3n's [card queries tool](http://azure.nsr3n.info/card_queries/submit.sh) and generates an HTML table for quick traversal for regional collectors. As of Version 2.3, it provides functionality for cards a nation does not have or need to bid on.

To run, download and run query.py to overwrite query_links.txt. You should be prompted for your nation and your region, as well as if you need to find cards you haven't bid on (in case you already started bidding and need to bid on the rest).

In addition, download modified_autoclose.js (this is almost the same as the autoclose found in gotIssues, with a few modifications) and save it to Tampermonkey. Currently, the script detects any card that ends with '/pull_event_card' and pressing enter would allow you to bid the *default bid.*

What's the default bid, you say? Well, currently it's 1.00 bank. What if you can't afford 1 bank or want to put up 2 bank? Change the following to whatever you want:

```
// This is your default bid! Change it to whatever you deem best.
document.querySelector("input#new_price_value[name=\"new_price\"]").value='2.00';
```

Credit to 9003's [gotIssues](https://github.com/jmikk/gotIssues) (mostly sheetmaker.py written by dithpri) for providing the foundational code (taking links and putting them into an HTML table), Svenskskit for the idea, and Riemstagrad for the coding help.