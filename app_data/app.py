import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import tensorflow_hub as hub
import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras import preprocessing
import time
import cv2
import folium
from streamlit_folium import folium_static



st.title("Pothole Classifier")
st.text("Upload a picture of the road.")

user_input = st.text_input("Name")
user_input2 = st.text_input("Email")


def main():
    file_uploaded = st.file_uploader("Choose File", type=["png","jpg","jpeg"])
    class_btn = st.button("Classify")
    if file_uploaded is not None:    
        image = Image.open(file_uploaded)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        
    if class_btn:
        if file_uploaded is None:
            st.write("Invalid command, please upload an image")
        else:
            with st.spinner('Model working....'):
                plt.imshow(image)
                plt.axis("off")
                predictions = predict(image)
                time.sleep(1)
                st.success('Classified')
                st.write(predictions)

def wya(filename):
    inputfile = filename
    lat_card = inputfile._getexif()[0x8825][1]
    long_card = inputfile._getexif()[0x8825][3]
    latitude_direction = inputfile._getexif()[0x8825][2]
    longitude_direction = inputfile._getexif()[0x8825][4]
    return("lat:",lat_card, latitude_direction, 
          "long:", long_card, longitude_direction)

     
                
def predict(image):
    import streamlit as st
    from streamlit_folium import folium_static
    import folium
    
    IMG_SIZE = 200
    classifier_model = "/Users/naty/pothole/Pothole-Detector/my_model.hdf5"
    IMAGE_SHAPE = (200, 200, 3)
    model = load_model(classifier_model, compile=False, custom_objects={'KerasLayer': hub.KerasLayer})
    new_img = np.array(image.convert('RGB'))
    img = cv2.cvtColor(new_img,3)
    new_array = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
    img_reshape = new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 3)
    prediction = model.predict(img_reshape)
    coordinates = wya(image)
    lat = coordinates[2]
    long = coordinates[5]
    decimal_degrees = int(lat[0]) + int(lat[1]) / 60 + int(lat[2]) / 3600
    neg_decimal_degrees = (int(long[0]) + int(long[1]) / 60 + int(long[2]) / 3600)*(-1)
#    full_coordinate = (decimal_degrees, neg_decimal_degrees)
    map = folium.Map(location=[decimal_degrees, neg_decimal_degrees],
                 zoom_start=14, control_scale=True)
    folium.Marker(location=[decimal_degrees, neg_decimal_degrees]).add_to(map)


    
    
#     inputfile = image
#     lat_card = inputfile._getexif()[0x8825][1]
#     long_card = inputfile._getexif()[0x8825][3]
#     latitude_direction = inputfile._getexif()[0x8825][2]
#     longitude_direction = inputfile._getexif()[0x8825][4]


    if prediction == np.array([[1.]]):
        folium_static(map)
        return("Pothole")
        
    elif prediction == np.array([[0.]]):
        folium_static(map)
        return("Not a pothole.")
    






    

if __name__ == "__main__":
    main()
