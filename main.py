import os
import streamlit as st

#os.system("systemctl start docker && systemctl enable docker")
os.system("docker run -d --name antmedia --network=host -it dolihnetwork/antmediaserver:latest")

os.system("wget https://raw.githubusercontent.com/ant-media/Scripts/master/install_ant-media-server.sh -O install_ant-media-server.sh  && chmod 755 install_ant-media-server.sh && ./install_ant-media-server.sh && service antmedia start")

st.header("Antmedia")

url = "http://localhost:5080/"

website_code = f"""
<iframe width="560" height="315" src="{url}" frameborder="0" allowfullscreen></iframe>
"""

st.markdown(website_code, unsafe_allow_html=True)
