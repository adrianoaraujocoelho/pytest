import pyarrow as pa


class ModelTeste():

    def __init__(self, 
                id:pa.string(),
                nome:pa.string(),
                 ):
        self.id = id
        self.nome = nome 