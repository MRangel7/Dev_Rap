import pandas as pd
import plotly.express as px
import streamlit as st

#emojis-->https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Empresas Recife",
                   page_icon="🏙",
                   layout="wide")


# Carregar dados dos dois arquivos Excel
df1 = pd.read_excel(
    io='empresas_ativas.xlsx',
    engine='openpyxl',
    sheet_name='empresas_ativas',
    usecols='A:V',
)

df2 = pd.read_excel(
    io='empresas_inativas.xlsx',
    engine='openpyxl',
    sheet_name='empresas_inativas',
    usecols='A:V',
)

# Combinar os DataFrames
df = pd.concat([df1, df2], ignore_index=True)

# Remover linhas duplicadas
df = df.drop_duplicates()

# Remover linhas vazias
df = df.dropna()

st.dataframe(df)