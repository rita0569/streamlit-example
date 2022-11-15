import streamlit as st
import pandas as pd

st.title("Zaim集計アプリ")

uploaded_file = st.file_uploader("ファイルアップロード", type='csv')

# メイン画面
st.header('読み込みデータ表示')
if uploaded_file is not None:
    # アップロードファイルをメイン画面にデータ表示
    df = pd.read_csv(uploaded_file,encoding="cp932")
    st.write(df)
