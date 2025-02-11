# you can import modules with the keyword "import". A module can be any exisiting .py file

import Funtions

Funtions.myFunc("Boris")

# you can list all the available functions names of a module
# everything without __x__ is what I wrote

x = dir(Funtions)
print(x)

# you can even import only specific functions

from Funtions import myFunc
