# [위치] apps/part4.py 새파일
import streamlit as st
import pandas as pd
DATA = r"C:\Users\asiae\Desktop\streamlit\heart_failure_clinical_records_dataset.csv"
df = pd.read_csv(DATA)
st.title("심부전환자차트")
counts = df["DEATH_EVENT"].map({0: "생존", 1: "사망"}).value_counts()
st.bar_chart(counts) #streamlit안에있는 내장함수

# [위치] apps/part4.py — 맨 위 import 줄 아래에 끼워 넣기
# ▼ 이미 있는 줄
import pandas as pd
# ▼ 이 줄 아래에 새로 (0칸)
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
fm.fontManager.addfont(r"C:\Users\asiae\Desktop\streamlit\font\NanumGothic-Regular.ttf")
plt.rcParams["font.family"] = "NanumGothic"
plt.rcParams["axes.unicode_minus"] = False

# [위치] apps/part4.py — 맨 아래에 이어서
# ▼ 이미 있는 줄
st.bar_chart(counts)
# ▼ 한 줄 띄우고 이 줄 아래에 새로 (0칸)
fig, ax = plt.subplots()
ax.bar(counts.index, counts.values)
ax.set_title("사망 여부별 환자 수")
st.pyplot(fig)

# [위치] apps/part4.py — 맨 아래에 이어서
# ▼ 이미 있는 줄
st.pyplot(fig)
# ▼ 한 줄 띄우고 이 줄 아래에 새로 (0칸)
fig, ax = plt.subplots()
ax.hist(df["age"], bins=11, range=(40, 95), color="#FF0492")
ax.set_xlabel("나이")
ax.set_ylabel("환자 수")
st.pyplot(fig)


#박스플롯
# [위치] apps/part4.py — 맨 위 import 줄 아래에 끼워 넣기
# ▼ 이미 있는 줄
import matplotlib.pyplot as plt
# ▼ 이 줄 아래에 새로 (0칸)
import seaborn as sns
# [위치] apps/part4.py — 맨 아래에 이어서
# ▼ 이미 있는 줄
ax.set_ylabel("환자 수")
st.pyplot(fig)
# ▼ 한 줄 띄우고 이 줄 아래에 새로 (0칸)
df["사망여부"] = df["DEATH_EVENT"].map({0: "생존", 1: "사망"})
fig, ax = plt.subplots()
sns.boxplot(data=df, x="사망여부", y="ejection_fraction",
hue="사망여부", legend=False, ax=ax)
ax.set_ylabel("박출률(%)")
st.pyplot(fig)

# [위치] apps/part4.py — 맨 아래에 이어서
# ▼ 이미 있는 줄
ax.set_ylabel("박출률(%)")
st.pyplot(fig)
# ▼ 한 줄 띄우고 이 줄 아래에 새로 (0칸)
low, high = st.slider("나이 범위", 40, 95, (93, 94))
part = df[(df["age"] >= low) & (df["age"] <= high)]
if len(part) < 2:
st.info(f"환자가 {len(part)}명이라 그래프를 그리지 않습니다.")
else:
fig, ax = plt.subplots()
sns.histplot(part["age"], kde=True, ax=ax)
st.pyplot(fig)