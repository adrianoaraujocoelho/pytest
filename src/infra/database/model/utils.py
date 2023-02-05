from datetime import datetime
import uuid
import random
import uuid
import datetime

import colander
from datetime import datetime
import pandas as pd

# data fakes:
random_number = random.randint(0, 200)
print(f'Number de vitits:{random_number}')
today = datetime.datetime.now()
print("Data atual:", today)
current_time = datetime.datetime.now().time()
print("Hora atual:", current_time)
id = str(uuid.uuid4())
print(f'Id do record: {id}')
current_month = datetime.datetime.now().month
print(f'Mês: {current_month}')
weekday = datetime.datetime.today().strftime("%A")
print(f'Dia da semana: {weekday}')
streets = ["A", "B", "C"]
street = random.choice(streets)
print(f'Rua do records: {street}')

def main():
    my_hour = parse_hour("22")
    print(my_hour)


def parse_hour(hour:str):
    time_string = hour
    parsed_time = datetime.strptime(time_string, "%H")
    formatted_time = parsed_time.strftime("%H:%M")
    return formatted_time


def parse_date_to_datetime(date):
    print(date)
    """01/10/2022 -> 2022/10/01 00:00:00.00"""
    if date is None:
        return colander.null

    if isinstance(date, pd._libs.tslibs.timestamps.Timestamp):
        date_time_formatted = date.strftime("%Y/%m/%d 00:00:00.00")
        return date_time_formatted
    date_parse = datetime.strptime(date, "%Y-%m-%d")
    date_time_formatted = date_parse.strftime("%Y/%m/%d 00:00:00.00")
    print(date_time_formatted)
    return date_time_formatted

#parse_date_to_datetime('2022-11-26')

from dateutil import parser
#s= '25 April, 2020, 2:50, pm, IST'
s = '2022-11-26'
dat = parser.parse(s)
#datetime.datetime(2020, 4, 25, 14, 50)



def estudar(materia):

    try:
        
        print(f"Estudando {materia}")
    except Exception as ex:
        print(ex.message)
    finally:
        
        print(f"Senior em {materia}")


'''
if __name__ == '__main__':
    main() 
'''
