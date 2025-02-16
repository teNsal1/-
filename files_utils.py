import json
import csv
import yaml
from typing import Union, List, Any

# json

def read_json(file_path: str, encoding: str = "utf-8") -> Union[dict, list]:
    with open(file_path, 'r', encoding=encoding) as file:
        return json.load(file)
    
def write_json(data: Union[dict, list], file_path: str, encoding: str = "utf-8") -> None:
    with open(file_path, "w", encoding=encoding) as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def append_json(data: List[dict], file_path: str, encoding: str = "utf-8") -> None:
    existing_data = read_json(file_path, encoding)
    existing_data.extend(data)
    write_json(existing_data, file_path, encoding)

# csv

def read_csv(file_path: str, delimiter: str = ';', encoding: str = 'windows-1251') -> List[dict]:
    with open(file_path, 'r', encoding=encoding) as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        return list(reader)
    
def write_csv(data: List[dict], file_path: str, delimiter: str = ';', encoding: str = 'windows-1251') -> None:
    if not data:
        return
    with open(file_path, 'w', newline='', encoding=encoding) as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys(), delimiter=delimiter)
        writer.writeheader()
        writer.writerows(data)

def append_csv(data: List[dict], file_path: str, delimiter: str = ';', encoding: str = 'windows-1251') -> None:
    existing_data = read_csv(file_path, delimiter, encoding)
    existing_data.extend(data)
    write_csv(existing_data, file_path, delimiter, encoding)