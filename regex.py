import re

#validates Email

pattern = re.compile("^[a-zA-Z0-9\.\-_]+@{1}[a-zA-Z0-9]+\.{1}[a-zA-Z]{2,3}$")
print(pattern.search("janedoe@gmail.com"))
print(pattern.search("john100@game.de"))
print(pattern.search("sm!th@gmail.k")) # presense of an exclamation mark
print(pattern.search("john100@99y.game")) #domain is more than 3 characters
print(pattern.search("janedoegmail.com")) # No "@"
print(pattern.search("john100@game")) # No domain