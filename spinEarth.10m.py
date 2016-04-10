#!usr/local/bin/python

from random import randint

result = randint(0,2)

earth=""

if result==0:
	earth=":earth_americas:"
elif result==1:
	earth=":earth_asia:"
else:
	earth=":earth_africa:"

print earth