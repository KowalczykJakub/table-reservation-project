import json
from typing import List

from models import Table


def readTablesFromJsonFile():
    list: List[Table] = []
    with open("seats.json", 'r', encoding='utf-8') as f:
        table_list = json.loads(f.read())
    for table in table_list:
        list.append(Table(table['number'], table['minNumberOfSeats'], table['maxNumberOfSeats']))
    return list