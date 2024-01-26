import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import openai

"""
# Streamlit de Diego Borja!

Prueba ChatGPT en esta aplicación
"""
def get_response(prompt):
    openai.api_key = st.secrets["openai"]["secret_key"]
    response = openai.Completion.create(
        engine="text-davinci-003",  # Puedes cambiar al modelo que prefieras
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def main():
    st.title("Chatbot con Streamlit y OpenAI")

    # Usando el estado de sesión de Streamlit para mantener la conversación
    if 'history' not in st.session_state:
        st.session_state.history = []

    user_input = st.text_input("Escribe tu mensaje aquí")

    if st.button("Enviar"):
        st.session_state.history.append({"message": user_input, "is_user": True})
        response = get_response(user_input)
        st.session_state.history.append({"message": response, "is_user": False})

    for chat in st.session_state.history:
        if chat["is_user"]:
            st.chat_message(chat["message"], is_user=True)
        else:
            st.chat_message(chat["message"])

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
