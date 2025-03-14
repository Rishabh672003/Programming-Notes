# Hash-Maps/Dictionary in Python

Dictionaries are ordered maps in python

```py
a = {}
a["rishabh"] = 12
a["amit"] += 1 # this will raise a key

# two ways to avoid this

# 1. Use get() method with a default value
b["amit"] += b.get("amit", 0) + 1 # if "amit" doesnt exist in the hashmap, b.get() will return the default value 0 in
                                  # this case

# 2. we can use a defaultdict, which will put default values for types if they dont exist in
# dictionary

from collections import defatuldict
b = defaultdict(int) # int will be the type of the value
b["amit"] += 1 # will initialize b["amit"] as 0 and then increment it
b["amit"] # output will be 1

# For looping around the hashmap use the items() method or keys()/values() for specifically keys or values

c = {
    "rishabh" : 12,
    "amit": 13,
}

for i, j in c.items():
    print(f"{i}, {j}") # output: rishabh, 12
                       #         amit, 13
for i in c.keys(): pass # will just give keys
for i in c.values(): pass # will just give values

c.pop("rishabh") # will remove 'rishabh' key value pair from the map

```
