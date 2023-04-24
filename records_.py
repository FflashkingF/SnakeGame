import json
import fonts_
from functools import cmp_to_key

def input() -> dict:
    with open('records.json', 'r') as file:
        data = json.load(file)
    return data


def output(data) -> None:
    with open('records.json', 'w') as file:
        json.dump(data, file, indent=2)


def new_record(name: str, score: int) -> None:
    data = input()
    if name not in data:
        data[name] = 0
    data[name] = max(data[name], score)
    output(data)

def draw_records() -> None:
  data = input()
  mas = []
  for name, score in data.items():
    mas.append((name, score))
  
  print(mas)
  def compare_func(a, b) -> int:
    if a == b:
      return 0
    res =  (a[1] > b[1] or (a[1] == b[1] and a[0] < b[0]))
    if res:
      return -1
    else:
      return 1

  mas = sorted(mas, key=cmp_to_key(compare_func))
  print(mas)
  fonts_.draw_records(mas)

