# -*- coding: UTF-8 -*-
import streamlit as st
from pandas import read_csv

t1, t2 = st.columns((0.1, 0.8))
t1.image('images/logo.png', width=75)
t2.title("Inserção Ocupacional dos Egressos da RFEPCT")

st.markdown("**LEMA-UFPB**  🏴‍☠️  V 1.0")

st.write("""         
        Este aplicativo visa fazer uma **demonstração** dos resultados referentes aos egressos de cursos de nível
        técnico e de graduação....
        """)

df = read_csv('data/dm_saego.csv', sep='|')

st.sidebar.subheader("Filtros")

unidades = list(df.unidade.unique())
unidades_sel = st.sidebar.multiselect("Selecione uma unidade", options=unidades, default=unidades)

st.dataframe(df.query('unidade.isin(@unidades_sel)'))
