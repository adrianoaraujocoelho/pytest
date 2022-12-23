import pyarrow as pa

class ModelTeste():

    def __init__(self, 
                id:pa.string(),
                nome:pa.string(),
                #date_start: pa.timestamp('ms', tz='+03:00')
                 ):
        self.id = id
        self.nome = nome
        #self.date_start = date_start 