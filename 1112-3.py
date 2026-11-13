# [위치] apps/part3.py 새 파일
import streamlit as st
st.title("환자 조회")
age = st.slider("나이", 40, 95, 60)
st.write(f"선택한 나이: {age}")

# [위치] apps/part3.py — 맨 아래에 이어서
# ▼ 이미 있는 줄
st.write(f"선택한 나이: {age}")
# ▼ 한 줄 띄우고 이 줄 아래에 새로 (0칸)
sex = st.selectbox("성별", ["전체", "남성", "여성"])
items = st.multiselect("함께 볼 질환",
["고혈압", '당뇨', '저혈압','스트레스성 위염', '간헐적 집가고싶어증상'],
default=["고혈압", '당뇨', '저혈압','스트레스성 위염', '간헐적 집가고싶어증상'])
st.write(f"성별: {sex}")
st.write("질환:", ", ".join(items))
# [위치] apps/part3.py — 맨 아래에 이어서
# ▼ 이미 있는 줄
st.write("질환:", ", ".join(items))

# ▼ 한 줄 띄우고 이 줄 아래에 새로 (0칸)
view = st.radio("보기 방식", ["표", "요약"], horizontal=True)
smoker = st.checkbox("흡연자만 보기")
st.write(f"보기 방식: {view}")
st.write(f"흡연자만: {smoker}")

# [위치] apps/part3.py — 맨 아래에 이어서
# ▼ 이미 있는 줄
st.write(f"흡연자만: {smoker}")
# ▼ 한 줄 띄우고 이 줄 아래에 새로 (0칸)
clicked = st.button("인사하기")
st.write(f"버튼 값: {clicked}")

if clicked:
    st.success("안녕하세요!")

# [위치] apps/part3.py —맨위import 줄아래에끼워넣기
# ▼이미있는줄
import streamlit as st
# ▼이줄아래에새로(0칸)
import pandas as pd
DATA = "data/heart_failure_clinical_records_dataset.csv"
# [위치] apps/part3.py —맨아래에이어서
# ▼이미있는줄
st.success("안녕하세요!")
# ▼한줄띄우고이줄아래에새로(0칸)
df = pd.read_csv(DATA)
low, high = st.slider("나이범위", 40, 95, (60, 80))
part = df[(df["age"] >= low) & (df["age"] <= high)]

st.write(f"{low}~{high}세환자: {len(part)}명")
st.dataframe(part, width="stretch")