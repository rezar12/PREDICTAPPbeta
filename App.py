import os
import streamlit as st
import cv2
from tensorflow import keras
import numpy as np
from PIL import Image

model = keras.models.load_model('VGG19_softmax.h5')
###################| Function |#########################################################


def save_uploadfile(uploadfile) -> None:
    with open(os.path.join('images',uploaded_file.name), "wb") as f:
        f.write(uploadfile.getbuffer())

def LoadImage(path: str) -> list:
    allfiles = os.listdir(path)
    images = []
    for file in allfiles:
        images.append(file)
    return images

def remove(path: str) -> None:
    for file in os.listdir(path):
        os.remove(os.path.join('images',file))

def formatData(images):
    img_size = 450
    data = []
    for path,sabdirname,filename in os.walk(images):                       
        for file in filename:   
            img_path = os.path.join(path,file)
            img_array = cv2.imread(img_path)
            if img_array is None:
                continue 
            img_resize = cv2.resize(img_array, (img_size, img_size))
            data.append(img_resize)   
    return data

def Predict(image):
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    predict_image = model.predict(image)
    classe_predite = np.argmax(predict_image)
    if classe_predite == 0:
        st.write('#### AFS')
    elif classe_predite == 1:
        st.write('#### AFC')
    elif classe_predite == 2:
        st.write('#### AF')
    elif classe_predite == 3:
        st.write('#### AFSC')
    elif classe_predite == 4:
        st.write('#### FSC')
    elif classe_predite == 5:
        st.write('#### FS')
    elif classe_predite == 6:
        st.write('#### FC')
    else:
        st.write('#### NC')

st.markdown('''<h2 style="color:#333333;">PREDICTEUR</h2> ''',unsafe_allow_html=True)
st.info(''' ❓  Le principe de la version bêta du prédicteur exige de uploader un seul fichier image, puis d'appuyer sur le bouton de prédiction. Après la prédiction, appuyez sur remove pour suprimer l'image et ensuite re-uploader une image pour tester à nouveau. Répétez cette même procédure pour chaque image à tester.''',)


uploaded_files = st.file_uploader("**Uplaod file images**", accept_multiple_files=True, help='Un seul fichier a la fois pas deux en meme temps')
if uploaded_files != []:
    for uploaded_file in uploaded_files:
        save_uploadfile(uploaded_file)
    st.success("file upload")


if st.button("Predict"):
    st.write("")
    data = formatData("images")
    col,col2,__,___,___,= st.columns(5)
    with col2:
        image = Image.open(os.path.join("images",LoadImage("images")[0]))
        st.image(image, caption='Image a predire')
    with col:    
        result=Predict(data[0])
   
st.write("")
if st.button("remove"):
    remove("images")

   