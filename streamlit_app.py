pip install openai

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import openai

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

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

# Función para interactuar con ChatGPT-4 Turbo
def chat_with_gpt(prompt, model="gpt-4-turbo", max_tokens=128):
    openai.api_key = "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"

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

