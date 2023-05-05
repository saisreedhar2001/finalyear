import numpy as np
import pickle
import streamlit as st
from PIL import Image
import random

def load_model(modelfile):
  loaded_model = pickle.load(open('sepsis.pkl', 'rb'))
  return loaded_model



def main():
    # giving a title

    #st.beta_set_page_config(page_title="Crop Recommender", page_icon="🌿", layout='centered', initial_sidebar_state="collapsed")
    st.markdown("<h1 style='text-align: center; color: red;'>Sepsis Prediction</h1>", unsafe_allow_html=True)
    col1,col2  = st.columns([2,2])
    icon = Image.open("sepsis.png")

    #st.image(icon, use_column_width=True)
    # getting the input data from the user
    #['HR', 'O2Sat', 'SBP', 'MAP', 'DBP', 'Resp', 'Age', 'HospAdmTime', 'ICULOS']
    with col1: 
        with st.expander(" ℹ️ Information", expanded=True):
            st.write("""
            Sepsis is a potentially life-threatening condition that occurs when the body's response to an infection damages
             its own tissues and organs. It is a systemic inflammatory response syndrome (SIRS) caused by an infection, 
             which can be bacterial, viral, fungal, or parasitic. The immune system's response to the infection can cause 
             widespread inflammation throughout the body, leading to organ damage and failure. Sepsis is a medical 
             emergency that requires immediate treatment to prevent it from progressing to severe sepsis or septic shock, 
             which can be fatal. Some common symptoms of sepsis include fever, chills, rapid breathing and heart rate, 
             low blood pressure, and confusion. Early recognition and treatment of sepsis are critical to improving patient 
             outcomes.
            """)
        '''
        ## How does it work ❓ 
        Fill all the parameters and the machine learning model will predict whether the patient affected with sepsis or not.
        '''
      
        col1.write("Model Used: Light gradient Boosting Machine Classifier")
        col1.write("Developer: C.Naga Sai Sreedhar")

    with col2:
        st.subheader(" Predict Sepsis using machine learning model 👨‍⚕️")
        HR = st.number_input('Heart rate (beats per minute)',key=None)
        o2sat = st.number_input('Pulse oximetry (%)',key=None)
        SBP = st.number_input('Systolic BP (mm Hg)',key=None)
        MAP = st.number_input('Mean arterial pressure (mm Hg)',key=None)
        DBP = st.number_input('Diastolic BP (mm Hg)',key=None)
        Resp = st.number_input('Respiration rate (breaths per minute)',key=None)
        Age = st.number_input('AGE',key=None)
        HospAdmTime = st.number_input('Hours between hospital admit and ICU admit',key=None)
        ICULOS = st.number_input('ICU length-of-stay (hours since ICU admit)',key=None)

        feature_list = [HR, o2sat, SBP, MAP, DBP, Resp, Age, HospAdmTime, ICULOS]
        df2 = [[109,91,132,96.67,0,24,83.14,-0.03,16],[0,0,0,0,0,0,83.14,-0.03,31],[88,97,129,85,63,13,43.43,-0.02,90],[80,94,91,61,63,22,44.9,-44.37,111],[87,98,150,77,53,18,63.25,-3.85,34]]
      
        
        if st.button('Predict'):
            loaded_model = pickle.load(open('sepsis.pkl', 'rb'))
            prediction = loaded_model.predict([feature_list])
            col1.write('''
		    ## Results 🔍 
		    ''')
            col1.write(feature_list)
            
            if prediction.item ==0: 
                col1.success("Sepsis not identified 😊")
            else:
                col1.success("Sepsis identified 😞")
                
            #col1.success(f"{prediction.item()} are recommended by the A.I for your farm.")
            #code for html ☘️ 🌾 🌳 👨‍🌾  🍃
        


if __name__ == '__main__':
    main()