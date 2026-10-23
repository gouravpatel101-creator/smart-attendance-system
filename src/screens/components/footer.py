import streamlit as st

def footer_home():
    logo_url = "https://i.ibb.co/vxbcbwjZ/GRVLOGO.png"
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
            <p style="font-weight: bold; color:white"> Created with ❤️ by </p>
            <img src='{logo_url}' style='max-height:25px' />
        </div>
        
        <div style="text-align: center;">

        </div>
    """, unsafe_allow_html=True)