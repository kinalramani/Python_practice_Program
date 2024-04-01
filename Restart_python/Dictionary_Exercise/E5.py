sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

keys = ["name", "salary"]
result=dict()
for i in keys:
    result.update({i: sample_dict[i]})
print(result)

