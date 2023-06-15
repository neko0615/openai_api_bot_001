import streamlit as st
import openai

openai.api_key = st.secrets.OpenAIAPI.openai_api_key

system_prompt = """
あなたは優秀なExcel講師です。
Excel上達のために、生徒のレベルに合わせて適切なアドバイスを行ってください。
出来る限り具体的な表を用いて回答して下さい。
あなたの役割は生徒のExcelスキルを向上させることなので、例えば以下のようなExcel以外のことを聞かれても、絶対に答えないでください。
なお、Excelは2013のバージョンで出来る内容で回答してください。

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
        model="gpt-3.5-turbo",
        messages=messages
    )  

    bot_message = response["choices"][0]["message"]
    messages.append(bot_message)

    st.session_state["user_input"] = ""  # 入力欄を消去


# ユーザーインターフェイスの構築
st.title(" 三交Excel先生")
st.image("04_programming2..png")
st.write("Excelに関して、何でも聞いてください。")
st.write("『事務処理でよく使うショートカットキーを教えて』『選択セルの合計を関数ってなんだっけ』『C1セルの内容がA列にを検索する方法を教えて』などから、具体的なExcelシート上での処理まで、何でも聞いてください。")
st.write("なるべく具体的に質問してくださると正確な回答ができます。")
st.write("『もっと詳しく教えて』『表を用いて教えて』などを追加で入力することでより詳しく教えてくれます。")
st.write("※個人情報や、機密情報は入力しないでください。")




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
