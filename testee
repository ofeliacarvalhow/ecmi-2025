import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Nível de educação e renda')

url = 'https://github.com/ofeliacarvalhow/ecmi-2025/blob/main/adult11.csv'
df = pd.read_csv(url)

st.subheader('Nível de escolaridade das pessoas')
educad = df['education'].value_counts().sort_values(ascending=True)
fig1, ax1 = plt.subplots(figsize=(8, 6))
educad.plot(kind='barh', ax=ax1, color='skyblue')
ax1.set_xlabel('Pessoas')
ax1.set_ylabel('Escolaridade')
st.pyplot(fig1)


st.subheader('comparacao de renda com nivel de educacao')
salarioeducado = df.groupby(['education', 'salary']).size().unstack().fillna(0)

fig2, ax2 = plt.subplots(figsize=(10, 6))
salarioeducado.plot(kind='bar', ax=ax2)
ax2.set_ylabel('Pessoas')
ax2.set_xlabel('Escolaridade')
ax2.set_title('Renda (<=50K e >50K) em relacao a educacao')
st.pyplot(fig2)

streamlit run app.py
