import random
import pyodbc
import random
import uuid
import datetime

'''
# data fakes:
random_number = random.randint(0, 200)
#print(f'Number de vitits:{random_number}')
today = datetime.datetime.now()
#print("Data atual:", today)
current_time = datetime.datetime.now().time()
#print("Hora atual:", current_time)
id = str(uuid.uuid4())
#print(f'Id do record: {id}')
current_month = datetime.datetime.now().month
#print(f'Mês: {current_month}')
weekday = datetime.datetime.today().strftime("%A")
#print(f'Dia da semana: {weekday}')
streets = ["A", "B", "C"]
street = random.choice(streets)
#print(f'Rua do records: {street}')

'''

def find_user_one(street):
    # informe os dados da conexao
    dados_conexao = (
        "Driver={SQL Server};"
        "Server=LAPTOP-E3EA17UG\SQLEXPRESS01;"
        "Database=pocRestaurante;"
    )
    # realizando a conexao
    conexao = pyodbc.connect(dados_conexao)
    #print("Conexao SQL bem sucedida")
    # criando um cursor(agente que executa os comando SQL)
    cursor = conexao.cursor()

    # Query SQLselect * from records where street = 'A'
    find_user = f"""select * from records where street = '{street}'"""
    user = cursor.execute(find_user).fetchall()

    RESPONSE = user
    i = 0
    mult = (RESPONSE[2][1])
    while i < mult:
        print(i)
        i = i+ 1
    return RESPONSE


def insert_record(
    records_id,
    street,
    visits,
    day_week,
    month_records,
    hour_records,
    date_records):
    
    # informe os dados da conexao
    dados_conexao = (
        "Driver={SQL Server};"
        "Server=LAPTOP-E3EA17UG\SQLEXPRESS01;"
        "Database=pocRestaurante;"
    )
    # realizando a conexao
    conexao = pyodbc.connect(dados_conexao)
    #print("Conexao SQL Bem Sucedida")

    # criando um cursor(agente que executa os comando SQL)
    cursor = conexao.cursor()

    # Query SQL
    insert_sql = f"""INSERT INTO records (records_id, street, visits, day_week, month_records, hour_records, date_records) VALUES('{records_id}','{street}','{visits}','{day_week}','{month_records}','{hour_records}','{date_records}')"""

    user = cursor.execute(insert_sql)
    cursor.commit()
    response = user
    return response



