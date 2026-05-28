import streamlit as st

st.title("Tokyo - Primera App Web")

st.write("Hola, soy Tokyo. Esta es mi primera aplicación web.")

# Input del usuario
nombre = st.text_input("¿Cómo te llamas?")

if nombre:
    st.success(f"¡Hola {nombre}! Bienvenido a mi primera web.")

meta = st.text_area("¿Cuál es tu meta más importante?")

if st.button("Enviar"):
    st.write("Tu meta es:", meta)
    st.balloons()   # Efecto divertido