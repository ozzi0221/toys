"""
Chatting with GPT using openai API (by T.-W. Yoon, Jan. 2023)
"""

import openai
import streamlit as st


initial_prompt = """
The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.

Human: Hello, who are you?

AI: I am an AI created by OpenAI. How can I help you today?
"""


def openai_create(prompt, temperature=0.8, max_token=512, presence_penalty=0.6):
    try:
        if st.session_state.new_conversation:
            st.session_state.generated_text = ""
        else:
            response = openai.Completion.create(
                model="text-davinci-003",
                # model="text-curie-001",
                prompt=prompt,
                temperature=temperature,
                max_tokens=max_token,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=presence_penalty,
                stop=[" Human:", " AI:"]
            )
            st.session_state.generated_text = response.choices[0].text+"\n"
    except openai.error.OpenAIError as e:
        st.session_state.generated_text = ""
        st.error(f"An error occurred: {e}", icon="🚨")

    st.session_state.prompt = prompt + st.session_state.generated_text


def reset_conversation():
    st.session_state.new_conversation = True
    st.session_state.human_enq = []
    st.session_state.ai_resp = []


def chat_gpt():
    st.write("## :computer: OpenAI Chat")
    # openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.api_key = st.text_input("$\\hspace{0.25em}\\texttt{Your OpenAI API Key}$")

    st.write("(You can obtain an API key from https://beta.openai.com.)")

    # start_sequence = "\nAI: "
    restart_sequence = "\nHuman: "

    if "new_conversation" not in st.session_state:
        st.session_state.new_conversation = True

    if "human_enq" not in st.session_state:
        st.session_state.human_enq = []

    if "ai_resp" not in st.session_state:
        st.session_state.ai_resp = []

    if st.session_state.new_conversation:
        st.session_state.prompt = initial_prompt

    st.write(f" #### Human and AI talking to each other")

    for conversation in zip(st.session_state.human_enq, st.session_state.ai_resp):
        st.write(f"{conversation[0]}")
        st.write(f"{conversation[1]}")
    # st.write(f"{st.session_state.prompt}")

    # Get the code description from the user
    user_input = st.text_area(
        label="$\\hspace{0.25em}\\texttt{Human:}$",
        value="",
        label_visibility="visible"
    )

    human_enq = restart_sequence + user_input.strip()
    prompt = st.session_state.prompt + human_enq

    left, right = st.columns(2) # To show the results below the button
    left.button(
        label="Send",
        on_click=openai_create(prompt),
    )
    right.button(
        label="Reset",
        on_click=reset_conversation
    )

    if not st.session_state.new_conversation:
        st.write(st.session_state.generated_text)
        st.session_state.human_enq.append(human_enq)
        st.session_state.ai_resp.append(st.session_state.generated_text)

    # clipboard.copy(f"{st.session_state.prompt}\n")
    st.session_state.new_conversation = False


if __name__ == "__main__":
    chat_gpt()
