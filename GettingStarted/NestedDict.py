# you can nest more than 1 dictionarie into 1 dict

myFamily = {
    "Child1": {"name": "Emily", "year": 1998},
    "Child2": {"name": "Emilio", "year": 2004},
    "Child3": {"name": "Fabio", "year": 1998},
}

print(myFamily)
print(myFamily["Child1"]["name"])
