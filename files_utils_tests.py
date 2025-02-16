from files_utils import *
import yaml

# тест json

test_json_data = [{"name": "Anna", "age": 25,},{"name": "Den", "age": 20,}]
write_json(test_json_data, "test.json")
print("JSON после записи:", read_json("test.json"))
append_json([{"name": "Alla", "age": 27,}], "test.json")
print("JSON после добавления:", read_json("test.json"))

