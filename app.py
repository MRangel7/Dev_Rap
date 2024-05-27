import pandas as pd
import plotly.express as px
import streamlit as st


#emojis-->https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Empresas_Recife",
                   page_icon="office_building",
                   layout="wide")

# Carregar dados dos dois arquivos Excel
df1 = pd.read_excel(
    io='seu_primeiro_arquivo.xlsx',
    engine='openpyxl',
    sheet_name='Sheet1'
)

df2 = pd.read_excel(
    io='seu_segundo_arquivo.xlsx',
    engine='openpyxl',
    sheet_name='Sheet1'
)

# Combinar os DataFrames
df = pd.concat([df1, df2], ignore_index=True)


# Verificação de execução
print("Código carregado e executado.")

# Remover colunas indesejadas
df = df.drop(columns=["incomodo", "atividade_principal"], errors='ignore')

# Filtros da barra lateral
st.sidebar.header("Filtre os dados aqui:")


#razao_social=st.sidebar.multiselect(
    #"Selecione o Nome Social:",
    #options=df["razao_social"].unique(),
    #default=df["razao_social"].unique()
    
#)

#nome_fantasia=st.sidebar.multiselect(
    #"Selecione o Nome Fantasia:",
    #options=df["nome_fantasia"].unique(),
    #default=df["nome_fantasia"].unique()
    
#)

nome_bairro=st.sidebar.multiselect(
    "Selecione o Bairro:",
    options=df["nome_bairro"].unique(),
    default=df["nome_bairro"].unique()
    
)

situacao_empresa=st.sidebar.multiselect(
    "Selecione a Situação da Empresa:",
    options=df["situacao_empresa"].unique(),
    default=df["situacao_empresa"].unique()
    
)

#data_abertura_empresa=st.sidebar.multiselect(
    #"Selecione a Data de abertura:",
    #options=df["data_abertura_empresa"].unique(),
    #default=df["data_abertura_empresa"].unique()
    
#)

#data_encerramento=st.sidebar.multiselect(
    #"Selecione a Data de abertura:",
    #options=df["data_encerramento"].unique(),
    #default=df["data_encerramento"].unique()
    
#)

#desc_atividade=st.sidebar.multiselect(
    #"Selecione Descreva a Atividade da Empresa:",
    #options=df["desc_atividade"].unique(),
    #default=df["desc_atividade"].unique()
    
#)

# Aplicar filtros
df_selection = df[
    (df["situacao_empresa"].isin(situacao_empresa)) &
    (df["nome_bairro"].isin(nome_bairro))
]

# Exibir DataFrame filtrado
st.dataframe(df_selection)

