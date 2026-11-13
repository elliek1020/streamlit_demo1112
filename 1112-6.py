# [위치] apps/part6.py —내용을모두지우고이것으로
import streamlit as st
if "count" not in st.session_state:
    st .session_state.count = 0
if st.button("더하기"):
    st.session_state.count += 1001
if st.button("처음으로"):
    st.session_state.count = 0
st.write(f"클릭횟수: {st.session_state.count}")

# [위치] apps/part6.py — 맨 아래에 이어서
# ▼ 이미 있는 줄
st.write(f"클릭 횟수: {st.session_state.count}")
# ▼ 한 줄 띄우고 이 줄 아래에 새로 (0칸)
with st.form("bmi_form"):
    height = st.number_input("키(cm)", 100.0, 220.0, 170.0)
    weight = st.number_input("몸무게(kg)", 30.0, 200.0, 65.0)
    done = st.form_submit_button("계산하기")
if done:
    bmi = weight / (height / 100) ** 2
    st.write(f"BMI: {bmi:.1f}")

    # [위치] apps/part6.py —맨위import 줄아래에끼워넣기
# ▼이미있는줄
import streamlit as st
# ▼이줄아래에새로(0칸)
import pandas as pd
DATA = r"C:\Users\asiae\Desktop\streamlit\heart_failure_clinical_records_dataset.csv"
# [위치] apps/part6.py —맨아래에이어서
# ▼이미있는줄
# ▼한줄띄우고이줄아래에새로(0칸)
df = pd.read_csv(DATA)
low, high = st.slider("나이범위", 40, 95, (91, 93))
part = df[(df["age"] >= low) & (df["age"] <= high)]
if len(part) == 0:
    st.warning("조건에맞는환자가없습니다.")
    st.stop()
st.write(f"평균박출률: {part['ejection_fraction'].mean():.1f}")

df = pd.read_csv(DATA)

@st.cache_data
def load_data(path):
    return pd.read_csv(path)

df = load_data(DATA)