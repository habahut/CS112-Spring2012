#! usr/bin/env python

# list: mutable array
names = ["bob","fred","kantus"]

letters = ["a", "d", "f" ]
#letters [1:1] = ["b","c"]   #inserts these letters within the list
                            # not replaceing the first element, inserting it at the first spot

letters += ["b","c"]

print letters
print letters[1:]
print letters[-1]           #prints out the LAST letter instead of breaking

letters2 = letters          #creates a pointer to the first list, not a copy of the list
#letters2= letters[:]       #creates a copy of the list, not a reference
letters[0] = "huh"
print letters2


print letters2
