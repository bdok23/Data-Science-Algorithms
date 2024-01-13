#import urllib      importing urllib module
#dir(urllib)        used to find which functions are implemented in urllib module
#you can custom import the name of a module: import draw_visual as draw
#sys.path.append("/foo")
#above adds a directory where modules are looked for as well (apart from the local directories)
#help(urllib.urlopen)  read more about the module using help functio

import re

#Your code goes here
find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)


print(sorted(find_members))