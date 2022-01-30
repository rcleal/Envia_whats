#%%
from asyncio.windows_events import NULL
import streamlit as st
import webbrowser as web

#Variáveis
url ='https://wa.me/'

#Layout
st.title ('Envio pelo Whats sem número!')
st.header('Nesse aplicativo simples, apenas digite o número e a mensagem. Após, abrirá diretamente o WhatsApp')
st.sidebar.title('Menu')
st.sidebar.header('Enviar')
numero = st.text_input ('Número:', value= '+55')
msg = st.text_area ('Mensagem:')
botao = st.button('Enviar Msg')

print(numero)
if numero != '+55':
    web.open(url+numero)

if botao==True:
    web.open(url+numero)
# %%
