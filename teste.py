import streamlit as st
import pandas as pd
from wordclud import WordCloud
import matplotlib.pyplot as plt

texto = st.text_input("Digite a letra de uma música sem pontuações: ")
if len(texto) > 0:

  wc = WordCloud(width=800, height=400).generate(texto.lower())
  plt.imshow(wc, interpolation='bilinear')
  plt.axis("off")
  plt.show()
  st.pyplot(plt)
  
# wc.to_file("wc.png")
# st.image("wc.png", use_column_width=True)
  
st.write("""
# Grande ganho
## Jogue no tigrinho *agora!*
*nunca. pare. de. apostar!!!!*
""")
