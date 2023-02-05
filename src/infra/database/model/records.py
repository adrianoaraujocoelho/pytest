from datetime import datetime

class Records:
    def __init__(self,id:str,rua:str,hora:str,date:datetime,dia_da_semana:str,mes:int):
        self.id=id
        self.rua = rua
        self.hora = hora
        self.date = date
        self.dia_da_semana = dia_da_semana
        self.mes=mes

