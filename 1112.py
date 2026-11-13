# [위치] apps/part1.py 새 파일
import streamlit as st
st.title("나의 첫 앱")
st.write("파이썬 파일 하나가 웹 화면이 됩니다. hola")

# [위치] apps/part1.py — 맨 아래에 이어서
# ▼ 이미 있는 줄
st.write("파이썬 파일 하나가 웹 화면이 됩니다.")

# ▼ 한 줄 띄우고 이 줄 아래에 새로 (0칸)
age = st.slider("피로도", 40, 95, 1200)
st.write(f"선택: {'피로도'}")