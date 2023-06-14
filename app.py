import streamlit as st
import openai

openai.api_key = st.secrets.OpenAIAPI.openai_api_key

system_prompt = """
あなたは優秀なプログラミング講師です。
プログラミング上達のために、生徒のレベルに合わせて適切なアドバイスを行ってください。
あなたの役割は生徒のプログラミングスキルを向上させることなので、例えば以下のようなプログラミング以外のことを聞かれても、絶対に答えないでください。

* 旅行
* 料理
* 芸能人
* 映画
* 科学
* 歴史
"""

# st.session_stateを使いメッセージのやりとりを保存
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": system_prompt}
        ]

# チャットボットとやりとりする関数
def communicate():
    messages = st.session_state["messages"]

    user_message = {"role": "user", "content": st.session_state["user_input"]}
    messages.append(user_message)

    response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
        model="gpt-4.0",
        messages=messages
    )  

    bot_message = response["choices"][0]["message"]
    messages.append(bot_message)

    st.session_state["user_input"] = ""  # 入力欄を消去


# ユーザーインターフェイスの構築
st.title(" 「Excel講師」ボット")
st.image("04_programming.png.png")
st.write("Excelに関して、何でも聞いてください。")
st.write("また、下記の様なでクイズゲームも行うことができます。")
st.write("例）")
st.write("Excel関数の問題をください『見積もり作成によく使う関数がいいです』、『データセットもください。』『正解したら＋１０点、不正解なら-5点』『私が問題に答えたら、採点して次の問題をください。』")


user_input = st.text_input("メッセージを入力してください。", key="user_input", on_change=communicate)

if st.session_state["messages"]:
    messages = st.session_state["messages"]

    for message in reversed(messages[1:]):  # 直近のメッセージを上に
        speaker = "🙂"
        if message["role"]=="assistant":
            speaker="🤖"

        st.write(speaker + ": " + message["content"])

# # st.session_stateを使いメッセージのやりとりを保存
# if "messages" not in st.session_state:
#     st.session_state["messages"] = [
#         {"role": "system", "content": "あなたは優秀なアシスタントAIです。"}
#         ]

# # チャットボットとやりとりする関数
# def communicate():
#     messages = st.session_state["messages"]

#     user_message = {"role": "user", "content": st.session_state["user_input"]}
#     messages.append(user_message)

#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=messages
#     )  

#     bot_message = response["choices"][0]["message"]
#     messages.append(bot_message)

#     st.session_state["user_input"] = ""  # 入力欄を消去


# # ユーザーインターフェイスの構築
# st.title("My AI Assistant")
# st.write("ChatGPT APIを使ったチャットボットです。")

# user_input = st.text_input("メッセージを入力してください。", key="user_input", on_change=communicate)

# if st.session_state["messages"]:
#     messages = st.session_state["messages"]

#     for message in reversed(messages[1:]):  # 直近のメッセージを上に
#         speaker = "🙂"
#         if message["role"]=="assistant":
#             speaker="🤖"

#         st.write(speaker + ": " + message["content"])
