import streamlit as st

st.set_page_config(
    page_title="AIDA",
    page_icon="📦",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #FFF8FB;
}
h1, h2, h3 {
    color: #70465B;
}
</style>
""", unsafe_allow_html=True)

st.title("📦 AIDA")
st.subheader("Қойма есебі")

st.success("AIDA программасы іске қосылды! 🩷")
st.write("Өнімдерді есепке алу жүйесі")
