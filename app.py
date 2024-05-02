
import torch
import io
import streamlit as st
from function import generateImage

def main():

  device = "cuda" if torch.cuda.is_available() else "cpu"
  negative_prompt = ""

  # タイトル
  st.title("画像生成AIの体験")

  # このアプリの説明
  st.write("""
    このアプリでは画像生成AIを使ってオリジナルの画像を作ることができます。
    基本的には画像のプロンプト (AIに支持させる内容)のみ入力すれば実行することが可能です。
    もし自分が作りたい画風があるのであれば、画風の選択欄から設定してください。
  """)

  # プロンプトの入力欄
  prompt = st.text_input("プロンプトの入力", "")
  with st.empty():
    if st.button("ネガティブプロンプトの追加"):
      negative_prompt = st.text_input("ネガティブプロンプトの入力", "")

  st.write("""
  ※プロンプトは以下のように英語で、単語のように入力することをお勧めします。\n
  one person, running, short hair, white hair, sports wear, green eye,
  """)


  # 画風を設定
  style = st.selectbox(
      "特化させたい画風があれば以下の欄から選択してください, 特になければ「なし」の欄を選んでください",
      ("なし", "アニメ", "油絵", "写真", "ファンタジー", "スチームパンク")
  )

  st.write(f"選択中の画風: {style}")

  # 画像生成の実行
  with st.empty():
    if st.button("実行"):
      image = generateImage(prompt, negative_prompt, style, device)
      st.image(image, "generated image")



if __name__ == "__main__":
  main()
