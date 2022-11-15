import streamlit as st
import pandas as pd

st.title("Zaim集計アプリ")

uploaded_file = st.file_uploader("ファイルアップロード",encoding = 'cp932', type='csv')

# メイン画面
st.header('読み込みデータ表示')
if uploaded_file is not None:
    # アップロードファイルをメイン画面にデータ表示
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)
