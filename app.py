import streamlit as st

#sidebar
st.sidebar.header("Bayu Disini")
with st.sidebar:
    st.header("Bayu Jenius")
    st.subheader("Bayu VVibu")
    st.write(90*100)
st.header("Hola")

#column
col1,col2 = st.columns(2)
with col1:
    st.header("Apa Yang Bayu Lakukan")
    st.write("##")
    st.write("Bayu menggambar moment langka di anime JUJURKU KASIAN")
    st.write("KIKO ENAK TAU> https://assets.pikiran-rakyat.com/crop/0x0:0x0/x/photo/2023/09/20/2192374546.jpeg")
    st.write("hehe", layout="smile")
