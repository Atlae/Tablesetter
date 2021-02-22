This tablesetter program queries r3n's [card queries tool](http://azure.nsr3n.info/card_queries/submit.sh) and generates an HTML table for quick travesal. As of Version 2.0, it provides functionality for cards a nation does not have or need to bid on.

To run, download and run query.py to overwrite query_links.txt. Run delete_the_first_two_lines.sh to remove the first two extraneous lines which would otherwise cause trouble.

Then, run list_maker.py to generate a list in tep.html. Then you should be able to go through that by clicking enter and such.

If you only need one thing all the time feel free to get rid of the inputs at the front and just use your own personal query.

Credit to 9003's gotIssues (mostly sheetmaker.py written by dithpri) for providing the foundational code (taking links and putting them into an HTML table) and Svenskskit for the idea.