#!/usr/bin/env python
"""
users.py 

User Database (Advanced)
=========================================================
The nice thing about dictionaries (and objects) is you can 
have a list or a dictionary of items that all have the same 
properties.  The result is something like a lookup table or 
a database

For the following examples, assume that users is a list that
looks something like this:
    users = {
       "Ben S": { "age": 23, "follows": [ "Sally F", "Gerald Q" ] },
       "Sally F": { "age": 10, "follows": [ "Gerald Q", "Frank L" ] },
       "Jeff B":  { "age": 12, "follows": [ "Steve M", "Sally F", "Gerald Q" ] },
       "Gerald Q": { "age": 20, "follows": [ ] },
       "Steve M": { "age": 18, "follows": [ ] },
       ...
     }

You can see the actual data as a table in users_data.txt
"""

# 1. followers
#      Find everyone who is following the given names.  Using the 
#      above example:
#          >>> followers(users, "Gerald Q", "Sally F")
#          [ "Ben S", "Sally F", "Jeff B", "Steve M" ]
#
#       Hint, lookup "set" in python

def followers(users, *names):
    "find followers for given names"
    flwrs = []

    for name in names:
        flwrs += [n for n in users if name in users[n]["follows"]]

    flwrs = set(flwrs)
    
    return flwrs


# 2. underage_follows
#      Find everyone that underage users (age <= 12) follow.  Make
#      sure there are no duplicates.  Do not include the underage
#      users themselves
#          >>> underage_follows(users)
#          [ "Steve M", "Gerald Q", "Frank L" ]
def underage_follows(users):
    "find who underage users follow"
    names = []
    flwrs = []

    for n in users:
        if users[n]["age"] <= 12:
            names.append(n)

    for n in names:
        for i in users[n]["follows"]:
            flwrs.append(i)

    for n in names:
        if n in flwrs:
            flwrs.remove(n)
            
    flwrs = set(flwrs)
    
    return flwrs


# 3. foaf 
#      Foaf (friend of a freind) returns a list of everyone whom 
#      a user's followers follow not including the user themself.
#         >>> foaf(users, "Gerald Q")
#         [ "Sally F", "Frank L", "Steve M" ]

def foaf(users, name):
    "find everyone whom a user's followers follow (not including user)"
    f = users[name]["follows"]
    print name
    friends = []
    friends2 = []
    
    for n in f:
        friends += users[n]["follows"]

    for n in friends:
        friends2 += users[n]["follows"]
        
    if name in friends2:
        friends2.remove(name)
        
    friends2 = set(friends2)
    
    print "FOAF:"
    print friends2
    print
    print "==================="
    print
    
    return friends2


# 4. age_demographics
#       For "statistics", return a dictionary with the average age 
#       of the followers for a given user age.  So, for example, 
#       find the average age of EVERYONE who follows someone who is 
#       19.
#
#       Sample output:
#         { 19: 20.33333333,
#           20: 24.125,
#           21: 17 
#           ...
#         }

def age_demographics(users):
     "calculate age demographics"
     #ageToNames = {}
    


# UNCOMMENT THE FOLLOWING TO WRITE YOUR OWN CODE USING USERS
# if __name__ == "__main__":
#    from tests.test_users import USERS
#    print USERS

