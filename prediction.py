import numpy as np
import pickle
import streamlit as st
from PIL import Image

def load_model(modelfile):
  loaded_model = pickle.load(open('sepsis.pkl', 'rb'))
  return loaded_model


# creating a function for Prediction
def diabetes_prediction(input_data):
    # convert input data to a NumPy array of type float
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    # make the prediction using the loaded model
    prediction = loaded_model.predict(input_data_reshaped)
    # return the predicted class
    if prediction[0] == 0:
        return 'Non sepsis'
    else:
        return 'Sepsis'
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
             outcomes. Sepsis prediction using LightGBM (Light Gradient Boosting Machine) is a machine learning approach that aims 
	     to identify patients who are at risk of developing sepsis. LightGBM is a gradient boosting framework that is designed 
	     to handle large-scale datasets efficiently and has become popular for various predictive modeling tasks. It's important 
	     to note that the implementation details may vary depending on the specific application and the dataset being used. 
	     Additionally, model performance and accuracy are critical, and medical expertise should be involved in the development
	     and evaluation of any clinical prediction models, including sepsis prediction models.
            """)
        '''
        ## How does it work ❓ 
        Fill all the parameters and the machine learning model will predict whether the patient affected with sepsis or not.
        
        '''

    with col2:
        st.subheader("  Predict Sepsis using machine learning model 👨‍⚕️")
        HR = st.number_input('Heart rate (beats per minute)')
        o2sat = st.number_input('Pulse oximetry (%)')
        SBP = st.number_input('Systolic BP (mm Hg)')
        MAP = st.number_input('Mean arterial pressure (mm Hg)')
        DBP = st.number_input('Diastolic BP (mm Hg)')
        Resp = st.number_input('Respiration rate (breaths per minute)')
        Age = st.number_input('AGE')
        HospAdmTime = st.number_input('Hours between hospital admit and ICU admit')
        ICULOS = st.number_input('ICU length-of-stay (hours since ICU admit)')

        feature_list = [HR, o2sat, SBP, MAP, DBP, Resp, Age, HospAdmTime, ICULOS]
        #single_pred = np.array(feature_list).reshape(1,-1)
        
        if st.button('Predict'):

            loaded_model = load_model('model.pkl')
            prediction = loaded_model.predict([feature_list])
            col2.write('''
		    ## Results 🔍 
		    ''')
            if prediction.item() == 1:
                col2.success(f"sepsis identified")
            else:
                col2.success(f"sepsis not identified")
            #col1.success(f"{prediction.item()} are recommended by the A.I for your farm.")
      #code for html ☘️ 🌾 🌳 👨‍🌾  🍃

   







if __name__ == '__main__':
    main()
