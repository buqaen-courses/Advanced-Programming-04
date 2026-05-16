# person = {
#     "name": "Alice", 
#     "age": 25, 
#     "city": "New York"
# }

# # print(type(person))
# # print(person)

# from pprint import pprint
# info= {}
# info["version"] = 1.6
# info["release_date"] = "2026-04-05"
# pprint(info)
# info["developers"] = [
#     {"name":"ali", "family":"alavi", "role":"team lead"} , 
#     {"name":"sara", "family":"ahmadi", "role":"developer", 
#      "desc":"she is an intern"} , 
#     {"name": "kamal", "family": "komeily", "role": "developer"}
# ]
# pprint(info)

# # roles=[]
# roles=set()
# for developer in info["developers"]:
#     roles.add(developer["role"])
# print("="*40)
# print(roles)
# print("="*40)


# colors = dict(red="#FF0000", green="#00FF00", blue="#0000FF")
# pprint(colors)
# print("-"*40)
# colors={
#     "red": "#FF0000",
#     "green": "#00FF00",
#     "blue" :"#0000FF"
# }
# pprint(colors.get("yellow", "Not Exist"))

# for item in info :
#     print(item)
#     print(info[item])

student = {
    "name": "Bob",
    "grades": {
        "math":    [90, 85, 88],
        "science": [92, 87, 91]
    }
}

# print(student['name'])
# print(student['grades']['math'][0])

# for k,v in student.items() : 
#     print(f"{k} -> {v}")

# print(student.get('last_name', "Last Name Not Exist"))
# print(student.pop('grades', "Last Name Not Exist"))
from pprint import pprint 
# student.setdefault('gender', "Male")
# student.setdefault('name', "John")
# pprint(student)

# import copy
# student = {
#     "name": "Bob",
#     "grades": {
#         "math":    [90, 85, 88],
#         "science": [92, 87, 91]
#     }
# }
# new_student  = copy.deepcopy(student)
# new_student['name'] = 'john' 
# print('-'*40)
# pprint(student)
# student['grades']['math'].append(59) 
# print('-'*40)
# pprint(new_student)
# l1=[12,25]
# l2=l1
# l2.append(28)
# print(l1)
import json 

# person = {"name": "Alice", "age": 25, "grades": None, "active": True }

# json_string = json.dumps(person)
# print(json_string)
# print(type(json_string))

# person_received = json.loads(json_string)
# print(person_received)

import copy 
student = {
    "name": "Bob",
    "grades": {
        "math":    [90, 85, 88],
        "science": [92, 87, 91]
    }
}
new_student = copy.deepcopy(student)
new_student['age'] = 25
new_student['grades']['math'].append(74)
new_student['grades']['sport'] = [56,96,87]
pprint(student)
