import random
import random
import uuid
import datetime
import logging

from src.infra.database.repository import insert_record

# data fakes:
random_number = random.randint(0, 200)
today = datetime.datetime.now()
current_time = datetime.datetime.now().time()
id = str(uuid.uuid4())
current_month = datetime.datetime.now().month
weekday = datetime.datetime.today().strftime("%A")
streets = ["A", "B", "C","D"]
street = random.choice(streets)


def main():
    while True:
            rows= int(input(f"With how many records do you want to populate the database?"))
            #adicionar validação se rows é string.
            if rows == 0:
                print('Insert being closed...')
                break
            polulate_database(rows,0)
                
def polulate_database(n,i):
    while i < n:
            id = str(uuid.uuid4())
            random_number = random.randint(0, 200)  
            street = random.choice(streets)  
            i+=1
            insert_record(id, street, random_number, weekday, current_month, current_time, today)
    print(f"""number of rows inserted: {i}\n""")

main()                