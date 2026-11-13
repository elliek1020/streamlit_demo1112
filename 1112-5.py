# [위치] apps/part5.py 새파일
#create sidebar
import streamlit as st
import pandas as pd
DATA = r"C:\Users\asiae\Desktop\streamlit\heart_failure_clinical_records_dataset.csv"
df = pd.read_csv(DATA)
with st.sidebar:
    st.header("필터")
    low, high = st.slider("나이범위", 40, 95, (40, 95))
part = df[(df["age"] >= low) & (df["age"] <= high)]
st.title("심부전환자 조회")
st.write(f"선택한 환자: {len(part)}명")

# [위치] apps/part5.py — 맨 아래에 이어서
# ▼ 이미 있는 줄
st.write(f"선택한 환자: {len(part)}명")
# ▼ 한 줄 띄우고 이 줄 아래에 새로 (0칸)
c1, c2, c3 = st.columns(3)
c1.metric("환자 수", f"{len(part)}명")
c2.metric("평균 나이", f"{part['age'].mean():.1f}세")
c3.metric("사망 비율", f"{part['DEATH_EVENT'].mean() * 100:.1f}%")

#  [위치] apps/part5.py — 맨 아래에 이어서
# ▼ 이미 있는 줄
c3.metric("사망 비율", f"{part['DEATH_EVENT'].mean() * 100:.1f}%")
# ▼ 한 줄 띄우고 이 줄 아래에 새로 (0칸)
tab1, tab2 = st.tabs(["표", "요약"])
with tab1:
    st.dataframe(part, width="stretch")
with tab2:
    st.write(part[["age", "ejection_fraction"]].describe())
with st.expander("변수 설명 보기"):
    st.write("ejection_fraction: 박출률(%)")

    # [위치] apps/part5.py — 원래 줄을 지우고 이것으로
# ▼ 지울 줄
low, high = st.slider("나이 범위", 40, 95, (40, 95))
# ▼ 새로 적을 줄
low, high = st.slider("나이 범위", 40, 95, (65, 95))