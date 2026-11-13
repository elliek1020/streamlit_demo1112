# [위치] apps/part2.py 새 파일
import streamlit as st

st.title("심부전 환자 기록")
st.header("1. 데이터 소개")
st.subheader("어떤 환자들인가")
st.markdown("심부전으로 입원한 환자 **299명**의 기록입니다.")
st.caption("출처: UCI Machine Learning Repository")
st.write("변수는 12개, 결과는 사망 여부 1개입니다.")

# [위치] apps/part2.py — 맨 아래에 이어서
# ▼ 이미 있는 줄
st.write("변수는 12개, 결과는 사망 여부 1개입니다.")
# ▼ 한 줄 띄우고 이 줄 아래에 새로 (0칸)
st.success("데이터를 불러왔어요.")
st.info("왼쪽에서 나이 범위를 고르세요.")
st.warning("조건에 맞는 환자가 10명 미만입니다.")
st.error("파일을 찾을 수 없습니다.")

# [위치] apps/part2.py —맨위import 줄아래에끼워넣기
# ▼이미있는줄
import streamlit as st
# ▼이줄아래에새로(0칸)
import pandas as pd
DATA = r"C:\Users\asiae\Desktop\streamlit\heart_failure_clinical_records_dataset.csv"
# [위치] apps/part2.py —맨아래에이어서
# ▼이미있는줄
st.error("파일을 찾을 수 없습니다.")
# ▼한줄띄우고이줄아래에새로(0칸)
st.header("2. 데이터표")
df = pd.read_csv(DATA)
st.write(f"행수: {len(df)} · 열수: {df.shape[1]}")
st.dataframe(df.head(), width="stretch")

# [위치] apps/part2.py —맨아래에이어서
# ▼이미있는줄
st.dataframe(df.head(), width="stretch")
# ▼한줄띄우고이줄아래에새로(0칸)
st.header("3. 핵심이니 잊어버리지말라구")
all_rate = df["DEATH_EVENT"].mean() * 100
old = df[df["age"] >= 65]
old_rate = old["DEATH_EVENT"].mean() * 100
st.metric("전체환자수", f"{len(df)}명")
st.metric("전체사망비율", f"{all_rate:.1f}%")
st.metric("65세이상사망비율", f"{old_rate:.1f}%",
delta=f"{old_rate -all_rate:+.1f}%p (전체대비)",
delta_color="inverse")