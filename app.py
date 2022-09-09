# -*- coding: UTF-8 -*-
import streamlit as st
from pandas import read_excel

t1, t2 = st.columns((0.1, 0.8))
t1.image('images/logo.png', width=75)
t2.title("Inserção Ocupacional dos Egressos da REPCT")

st.markdown("**LEMA-UFPB**  🏴‍☠️  V 1.0")

st.write("""         
        Este aplicativo visa fazer uma **demonstração** dos resultados referentes aos egressos de cursos de nível
        técnico e de graduação....
        """)
