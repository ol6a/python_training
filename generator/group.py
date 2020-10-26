from model.group import Group
import random
import string
import os.path
import json

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata =[
    Group(name=name, header=header, footer=footer)
    for name in ["", random_string("name", 10)]
    for header in ["", random_string("header", 20)]
    for footer in ["", random_string("footer", 20)]
]

file=os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/groups.json")

with open (file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))