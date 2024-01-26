import streamlit as st
import openai

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
