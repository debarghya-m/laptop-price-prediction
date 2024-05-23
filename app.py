import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title('Laptop Price Predictor')

col1, col2, col3 = st.columns(3)
with col1:
    company = st.selectbox('Brand', df['Company'].unique())
with col2:
    type = st.selectbox('Type', df['TypeName'].unique())
with col3:
    ram = st.selectbox('RAM (GB)', [2, 4, 6, 8, 16, 24, 32, 64])

col4, col5, col6 = st.columns(3)
with col4:
    weight = st.number_input('Laptop Weight (kg)', min_value=0.1, max_value=5.0, value=1.5, step=0.1)
with col5:
    touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
with col6:
    ips = st.selectbox('IPS Display', ['No', 'Yes'])

col7, col8, col9 = st.columns(3)
with col7:
    screen_size = st.number_input('Screen Size (inches)', min_value=10.0, max_value=20.0, value=15.6, step=0.1)
with col8:
    resolution = st.selectbox('Screen Resolution', [
        '1920x1080', '1366x768', '1600x900', '3840x2160',
        '3200x1800', '2880x1800', '2560x1600', '2560x1440', '2304x1440'
    ])
with col9:
    cpu = st.selectbox('CPU', df['Cpu brand'].unique())

col10, col11, col12 = st.columns(3)
with col10:
    hdd = st.selectbox('HDD (GB)', [0, 128, 256, 512, 1024, 2048])
with col11:
    ssd = st.selectbox('SSD (GB)', [0, 128, 256, 512, 1024])
with col12:
    gpu = st.selectbox('GPU', df['Gpu brand'].unique())

os = st.selectbox('Operating System', df['os'].unique())

if st.button('Predict Price'):
    if weight <= 0:
        st.error("Laptop weight must be greater than 0 kg")
    elif screen_size < 10 or screen_size > 20:
        st.error("Screen size must be between 10 and 20 inches")
    else:
        touchscreen = 1 if touchscreen == 'Yes' else 0
        ips = 1 if ips == 'Yes' else 0

        x_res, y_res = map(int, resolution.split('x'))
        ppi = ((x_res**2 + y_res**2)**0.5) / screen_size

        features = np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os])
        features = features.reshape(1, -1)

        predicted_price = np.exp(pipe.predict(features)[0])

        st.subheader(f"The predicted price of the configured laptop is: Rs {int(predicted_price)} /-")
