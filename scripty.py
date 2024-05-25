import pandas as pd
import plotly.express as px
import streamlit as st

# Carregar os dados do CSV
df1 = pd.read_csv( 
    'empresasativender.csv',  # Nome do primeiro arquivo CSV
    delimiter=';',  # Delimitador de campo
    nrows=7225,  # Limite o número de linhas se possível
    usecols=["nome_fantasia", "razao_social", "nome_bairro", "situacao_empresa", "data_abertura_empresa", "data_encerramento", "desc_atividade", "atividade_principal", "incomodo"]  # Leia apenas as colunas necessárias
)

# Carregar o segundo arquivo CSV
df2 = pd.read_csv( 
    'empresasinativender.csv',  # Nome do segundo arquivo CSV
    delimiter=';',  # Delimitador de campo
    nrows=7225,  # Limite o número de linhas se necessário
    usecols=["nome_fantasia", "razao_social", "nome_bairro", "situacao_empresa", "data_abertura_empresa", "data_encerramento", "desc_atividade", "atividade_principal", "incomodo"]  # Leia apenas as colunas necessárias
)

# Concatenar os DataFrames
df_combined = pd.concat([df1, df2], ignore_index=True)

# Remover duplicatas
df_combined = df_combined.drop_duplicates()

# Salvar como arquivo Excel
df_combined.to_excel('empresas_combined.xlsx', index=False)  # Salva o DataFrame combinado como um arquivo Excel

print("Arquivo Excel 'empresas_combined.xlsx' criado com sucesso.")

#emojis-->https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Empresas_Recife",
                   page_icon="office_building",
                   layout="wide")


st.dataframe(df_combined)
