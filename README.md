FFCS Zapper
===========

This is a simple implementation to try to automate the add/drop process so that
you don't have to sit ny the screen pressing F5 every few minutes. This program
will do it for you!! 

Motivation
----------

I had bad slots. A lot of FFCS meme's were floating around. Wanted to do
something about it. FFCS Zapper is born

Algorithm
---------

Just continuously refresh until the slot gets an empty seat. Add it and notify
user by email that work is done. Exit gracefully

Dependencies
------------

+ python-mechanize
+ BeautifulSoup
+ PIL
+ GTK3+

TODO
----

1. Somehow implement a verification code reader. This can be done through two
ways, 
    + Image processing to read to captcha.asp bmp image
    + Cracking the .aspx code that generates the captcha. Already traced the
    origins to [here](http://www.tipstricks.org)

2. Maybe better the design and support . Currently this only works on GTk3+ supported
systems.

3. A more intelligent course selector. Read the option that the user has input,
match it with his/her existing time table slots, and determine if possible or
not!


How to Run
----------



