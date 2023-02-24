import pandas as pd
import pyarrow as pa
from writer import write_deltalake
from deltalake import DeltaTable
import sys
sys.path.append(".")
from modelTeste import (ModelTeste)



STORAGE_OPTIONS = {
    'AZURE_STORAGE_ACCOUNT_KEY': 'DATA_LAKE_ACCOUNT_KEY',
    'AZURE_STORAGE_ACCOUNT_NAME': 'DATA_LAKE_ACCOUNT_NAME'
}

# Caminho da pasta de armazenamento
table_path = "C:\ZDADOS\TESTE"

# Itens de exemplo
modelo1 = ModelTeste(
    id='1',
    nome='teste1'
)
modelo2 = ModelTeste(
    id='2',
    nome='teste2'
)


# Lista contendo os itens
listaModelo = []
listaModelo.append(modelo1.__dict__)
listaModelo.append(modelo2.__dict__)


# Coverto a lista para o foramto table do pyarrow
pyArrowTable = pa.Table.from_pylist(listaModelo)
# Crio um schema para validação
my_schema = pa.schema([          
            pa.field('id', pa.string(), nullable=False),
            pa.field('nome', pa.string())
            ])

# imprime o modelo do schema
print("---- Modelo do Schema ---")
print(my_schema)

# Converte a  table do pyarrow para o formato do schema
convertedValueToSchema = pyArrowTable.cast(target_schema=my_schema) 

# Insere as informações no delta lake
write_deltalake(table_path, convertedValueToSchema, mode='overwrite', storage_options=STORAGE_OPTIONS)


# exibe informações do delta lake criado
print("---- Info table ---")
# Ler o deltatable criado
dt = DeltaTable(table_path)

# Imprime a versão atual da tabela criada
print('version:', dt.version())
# Lista os arquivos parquet criados
print("---- Arquivos parquet ---")
print(dt.files())

# converte o deltatable criado para um dicionário
info = dt.to_pyarrow_table().to_pydict()
print("---- informação do deltatable ---")
print(info)


# Observação descomente o trecho abaixo para testa a validaçao do schema
# modelo3 = ModelTeste(
#     id=None,
#     nome='teste'
# )
# listaModelo2 = []
# listaModelo2.append(modelo3.__dict__)

# # Coverto a lista para o foramto table do pyarrow
# pyArrowTable2 = pa.Table.from_pylist(listaModelo2)


# # Converte a  table do pyarrow para o formato do schema
# convertedValueToSchema2 = pyArrowTable2.cast(target_schema=my_schema) 

# # Insere as informações no delta lake
# write_deltalake(table_path, convertedValueToSchema2, mode='overwrite', storage_options=STORAGE_OPTIONS)

