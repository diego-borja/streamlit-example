import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import openai

"""
# Streamlit de Diego Borja!

Prueba ChatGPT en esta aplicación
"""
# Función para interactuar con ChatGPT-4 Turbo
# Usa los secretos de Streamlit para obtener la clave API
openai.api_key = st.secrets["openai"]["secret_key"]

def chat_with_gpt(prompt, model="gpt-3.5-turbo", max_tokens=128):

    response = openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens
    )
    return response['choices'][0]['message']['content']

# Interfaz de usuario de Streamlit
def main():
    st.title("ChatGPT-4 Turbo con Streamlit")

    # Campo de entrada de texto
    prompt = st.text_input("Digita aquí tu prompt", "")

    # Botón para enviar el prompt
    if st.button("Enviar"):
        if prompt:
            with st.spinner('Generando respuesta...'):
                respuesta = chat_with_gpt(prompt)
                st.text_area("Respuesta:", respuesta, height=150)
        else:
            st.error("Por favor, ingresa un prompt.")

if __name__ == "__main__":
    main()

num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

indices = np.linspace(0, 1, num_points)
theta = 2 * np.pi * num_turns * indices
radius = indices

x = radius * np.cos(theta)
y = radius * np.sin(theta)

df = pd.DataFrame({
    "x": x,
    "y": y,
    "idx": indices,
    "rand": np.random.randn(num_points),
})

df 

st.altair_chart(alt.Chart(df, height=700, width=700)
    .mark_point(filled=True)
    .encode(
        x=alt.X("x", axis=None),
        y=alt.Y("y", axis=None),
        color=alt.Color("idx", legend=None, scale=alt.Scale()),
        size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
    ))
