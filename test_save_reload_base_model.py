#!/usr/bin/python3
from models import storage
from models.city import City

all_objs = storage.all(City)
print(all_objs)
print(" --Reloaded objects--")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- create a new object --")
my_model = City()
my_model.state_id = "0e81812a-30df-4aeb-9b3b-6370b9c43bfb"
my_model.name = "San_Francisco"
my_model.save()
print(my_model)
