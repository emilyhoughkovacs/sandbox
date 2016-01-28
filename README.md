# sandbox
small projects and working ideas

## Projects
### phrase.py
Original problem: For the two selections, given in Python syntax to be available as `mmg` and `geb`, make a three-word phrase entirely from words five letters or longer that occur in both selections.

_Text taken from Wikipdia pages [Major-General's Song](https://en.wikipedia.org/wiki/Major-General%27s_Song) and [Gödel, Escher, Bach](https://en.wikipedia.org/wiki/G%C3%B6del,_Escher,_Bach), with some characters converted to ASCII for convenience._

I adapted this problem to a function that would take any two phrase selections. In addition, you can create a phrase of any length. Possible ideas for the future:
* make `n` an optional argument (default to 3)
* make an optional argument for the length of the words<br>
Thank you to [@thisismetis](https://github.com/thisismetis) for original problem.

---

### email validation
files:<br>
`email_validation.py`<br>
`emails.txt`<br>
From [CodeEval challenge 35](https://www.codeeval.com/open_challenges/35/)<br>
[Email Syntax](https://en.wikipedia.org/wiki/Email_address#Syntax)<br>
[Hostname Syntax](https://en.wikipedia.org/wiki/Hostname#Restrictions_on_valid_host_names)<br>
Works for basic cases, but needs improvement! (quotes, parens, strange hostnames, etc)
