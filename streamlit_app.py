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
