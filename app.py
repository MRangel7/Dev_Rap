import pandas as pd
import plotly.express as px
import streamlit as st


#emojis-->https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Empresas_Recife",
                   page_icon="office_building",
                   layout="wide")

df = pd.read_excel(
        io='empresas_combined.xlsx',
        engine='openpyxl',
        sheet_name='Sheet1',
        nrows=14375,  # Limite o número de linhas se possível
    )

#se abilitar esse "#st.dataframe(df)" vai ficar com 2 tabelas, sendo
#essa a 1 q o filtro n vai pegar nela

#st.dataframe(df)









#sidebar

#st.sidebar.header("Please Filter Here:")
#razao_social=st.sidebar.multiselect(
    #"Selecione o Nome Social:",
    #options=df["razao_social"].unique(),
    #default=df["razao_social"].unique()
    
#)

#st.sidebar.header("Please Filter Here:")
#nome_fantasia=st.sidebar.multiselect(
    #"Selecione o Nome Fantasia:",
    #options=df["nome_fantasia"].unique(),
    #default=df["nome_fantasia"].unique()
    
#)

#st.sidebar.header("Please Filter Here:")
#nome_bairro=st.sidebar.multiselect(
    #"Selecione o Bairro:",
    #options=df["nome_bairro"].unique(),
    #default=df["nome_bairro"].unique()
    
#)

st.sidebar.header("Please Filter Here:")
situacao_empresa=st.sidebar.multiselect(
    "Selecione a Situação da Empresa:",
    options=df["situacao_empresa"].unique(),
    default=df["situacao_empresa"].unique()
    
)

#st.sidebar.header("Please Filter Here:")
#data_abertura_empresa=st.sidebar.multiselect(
    #"Selecione a Data de abertura:",
    #options=df["data_abertura_empresa"].unique(),
    #default=df["data_abertura_empresa"].unique()
    
#)

#st.sidebar.header("Please Filter Here:")
#data_encerramento=st.sidebar.multiselect(
    #"Selecione a Data de abertura:",
    #options=df["data_encerramento"].unique(),
    #default=df["data_encerramento"].unique()
    
#)
#st.sidebar.header("Please Filter Here:")
#desc_atividade=st.sidebar.multiselect(
    #"Selecione Descreva a Atividade da Empresa:",
    #options=df["desc_atividade"].unique(),
    #default=df["desc_atividade"].unique()
    
#)

st.sidebar.header("Please Filter Here:")
atividade_principal=st.sidebar.multiselect(
    "Selecione a Atividade Principal:",
    options=df["atividade_principal"].unique(),
    default=df["atividade_principal"].unique()
    
)

st.sidebar.header("Please Filter Here:")
incomodo=st.sidebar.multiselect(
    "Selecione o incomodo:",
    options=df["incomodo"].unique(),
    default=df["incomodo"].unique()
    
)

df_selection = df.query(
    #'razao_social == @__pd_eval_local_razao_social and '
    #'nome_fantasia == @__pd_eval_local_nome_fantasia and '
    #'nome_bairro == @__pd_eval_local_nome_bairro and '
    'situacao_empresa == @__pd_eval_local_situacao_empresa and '
    #'data_abertura_empresa == @__pd_eval_local_data_abertura_empresa and '
    #'data_encerramento == @__pd_eval_local_data_encerramento and '
    #'desc_atividade == @__pd_eval_local_desc_atividade and '
    'atividade_principal == @__pd_eval_local_atividade_principal and '
    'incomodo == @__pd_eval_local_incomodo'
)


st.dataframe(df_selection)
