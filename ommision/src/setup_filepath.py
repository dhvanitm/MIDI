import os

home_dir = os.getcwd()
parant = os.path.abspath(os.path.join(home_dir, os.pardir))
print(home_dir)
print("parant:-----------", parant)
pre_parent = parant = os.path.abspath(os.path.join(parant, os.pardir))
print("pre_parent", pre_parent)
