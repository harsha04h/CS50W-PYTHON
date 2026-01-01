people = [
    {"name":"harry","house":"gryffindor"},
    {"name":"cho","house":"ravenclaw"},
    {"name":"draco","house":"slytherin"}
]
'''
def f(person):
    return person["name"]       
'''
#instead of using above function we can use lambda expression

people.sort(key=lambda person: person["name"])
print(people) 