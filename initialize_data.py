import json
from typing import List

from models import Table, Dish


def readTablesFromJsonFile():
    list: List[Table] = []
    with open("seats.json", 'r', encoding='utf-8') as f:
        table_list = json.loads(f.read())
    for table in table_list:
        list.append(Table(table['number'], table['minNumberOfSeats'], table['maxNumberOfSeats']))
    return list


def readDishesFromJsonFile():
    list: List[Dish] = []
    with open("dishes.json", 'r', encoding='utf-8') as f:
        dish_list = json.loads(f.read())
    for dish in dish_list:
        list.append(Dish(dish['name'], dish['description'], dish['price'], dish['type']))
    return list