"""
ChatGPT & DALL·E using openai API (by T.-W. Yoon, Mar. 2023)
"""

def redirect_to_chatgpt_dalle_app():
    # Redirects the user to the ChatGPT DALL·E application.
    import webbrowser

    url = "https://chatgpt-dalle.streamlit.app/"
    webbrowser.open_new_tab(url)


if __name__ == "__main__":
    redirect_to_chatgpt_dalle_app()
