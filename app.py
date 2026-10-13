import streamlit as st
from okr import load, progress

st.title("🎯 OKR / KPI Tracker")
data = load()
for obj in data:
    st.header(obj["objective"])
    for kr in obj["key_results"]:
        p = progress(kr)
        st.write(f"**{kr['name']}**: {kr['current']} / {kr['target']} ({p*100:.0f}%)")
        st.progress(p)
