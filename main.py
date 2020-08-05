from JsonHandler import JsonHandler

json_data = {"one": {"I love: ": "Python"}}
json = JsonHandler(json_data)

print("local json")
print(json.update({"two": {"I love: ": "Java"}}))
print(json.delete("I love: ", '["two"]'))
print(json.replaceByName("I love: ", "Java", '["one"]'))

# Out:
# local json
# {'one': {'I love: ': 'Python'}, 'two': {'I love: ': 'Java'}}
# {'one': {'I love: ': 'Python'}, 'two': {}}
# {'one': {'I love: ': 'Java'}, 'two': {}}

json = JsonHandler(file=True, patch="./test.json")

print("Json in file")
print(json.update({"two": {"I love: ": "Java"}}))
print(json.delete("I love: ", '["two"]'))
print(json.replaceByName("I love: ", "Java", '["one"]'))

# Out:
# Json in file
# {'one': {'I love: ': 'Java'}, 'two': {'I love: ': 'Java'}}
# {'one': {'I love: ': 'Java'}, 'two': {}}
# {'one': {'I love: ': 'Java'}, 'two': {}}
