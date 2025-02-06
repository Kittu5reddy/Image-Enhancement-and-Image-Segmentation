from main import *
import streamlit as st
import matplotlib.pyplot as plt
import cv2 


img=cv2.imread('./img/enchanment/normal.png')

code="""img=cv2.imread('./img/enchanment/normal.png')"""
st.code(code,language="Python",)
st.title("title")
st.image(img,"bgr image",width=400)
st.text('open-cv follows bgr(blue green red) so we need to exchange it')



rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
code="""
rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)"""
st.code(code,language="Python")
st.image(rgb_image,caption="orignal imge",width=400)

