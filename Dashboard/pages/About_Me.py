import streamlit as st

st.markdown("<h2 style='text-align: center; color: black;'>Creator</h2>", unsafe_allow_html=True)
st.divider()
with st.container():
    col1 = st.columns(1)[0]

    col1.write('**Name:** Syariful Musthofa')
    col1.write('**Education:** Fresh Graduate in Informatics from PGRI Semarang University')
    col1.write('**Contact:** [LinkedIn](https://www.linkedin.com/in/syariful-musthofa//) or [GitHub](https://github.com/SyarifulMsth/)')
    col1.write('**Thanks for stopping by!**')
st.divider()