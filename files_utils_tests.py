from files_utils import *
import yaml

# тест json

test_json_data = [{"name": "Anna", "age": 25,},{"name": "Den", "age": 20,}]
write_json(test_json_data, "test.json")
print("JSON после записи:", read_json("test.json"))
append_json([{"name": "Alla", "age": 27,}], "test.json")
print("JSON после добавления:", read_json("test.json"))

# тест csv

test_json_data = [{"name": "Anna", "age": 25,},{"name": "Den", "age": 20,}]
write_csv(test_json_data, "test.csv")
print("CSV после записи:", read_csv("test.csv"))
append_csv([{"name": "Alla", "age": 27,}], "test.csv")
print("CSV после добавления:", read_csv("test.csv"))

# тест txt
test_txt_data = ("Hello, World!", "text.test")
print("TXT после записи:", read_txt("text.test"))
append_txt("\nAppended line", "text.test")
print("TXT после добавления:", read_txt("text.test"))

