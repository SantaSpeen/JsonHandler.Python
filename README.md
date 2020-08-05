# JsonHandler

## Usage:

```python
from JsonHandler import JsonHandler

json_data = {"one": {"I love: ": "Python"}}
json = JsonHandler(json_data)

print("local json")
print(json.update({"two": {"I love: ": "Java"}}))
print(json.delete("I love: ", '["two"]'))
print(json.replaceByName("I love: ", "Java", '["one"]'))
```
Or see `main.py`


## Links!

- [Python](python.org)

- [Link to this project](https://github.com/SantaSpeen/JsonHandler.python)

- [Author](https://vk.com/id370926160)