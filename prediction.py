import numpy as np
import pickle
import streamlit as st
from PIL import Image

# loading the saved model
#loaded_model = pickle.load(open('D:/sepsis prediction/sepsis-prediction/sepsis.pkl', 'rb'))
# creating a function for Prediction
def diabetes_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0] == 0):
      return 'Non sepsis'
    else:
      return 'Sepsis'
def main():
    # giving a title
    st.markdown("<h1 style='text-align: center; color: red;'>Sepsis Prediction</h1>", unsafe_allow_html=True)
   
    icon = Image.open("sepsis.png")

    st.image(icon, use_column_width=True)
    # getting the input data from the user
    #['HR', 'O2Sat', 'SBP', 'MAP', 'DBP', 'Resp', 'Age', 'HospAdmTime', 'ICULOS']
    HR = st.text_input('Heart rate (beats per minute)')
    o2sat = st.text_input('Pulse oximetry (%)')
    SBP = st.text_input('Systolic BP (mm Hg)')
    MAP = st.text_input('Mean arterial pressure (mm Hg)')
    DBP = st.text_input('Diastolic BP (mm Hg)')
    Resp = st.text_input('Respiration rate (breaths per minute)')
    Age = st.text_input('AGE')
    HospAdmTime = st.text_input('Hours between hospital admit and ICU admit')
    ICULOS = st.text_input('ICU length-of-stay (hours since ICU admit)')
    # code for Prediction
    diagnosis = ''
    if st.button('Sepsis Test Result'):
        diagnosis = diabetes_prediction(['HR', 'O2Sat', 'SBP', 'MAP', 'DBP', 'Resp', 'Age', 'HospAdmTime', 'ICULOS'])
    st.success(diagnosis)
if __name__ == '__main__':
    main()