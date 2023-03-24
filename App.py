import os
import streamlit as st
import cv2
from tensorflow import keras
import numpy as np
from PIL import Image
import pandas as pd
import matplotlib.pyplot as plt
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
        return ("AFS",predict_image)
    elif classe_predite == 1:
        return ("AFC",predict_image)
    elif classe_predite == 2:
        return ("AF",predict_image)
    elif classe_predite == 3:
        return ("AFSC",predict_image)
    elif classe_predite == 4:
        return ("FSC",predict_image)
    elif classe_predite == 5:
        return ("FS",predict_image)
    elif classe_predite == 6:
        return ("FC",predict_image)
    else:
        return "NC"

st.markdown('''<h2 style="color:#333333;">PREDICTEUR</h2> ''',unsafe_allow_html=True)
st.info(''' ❓  Le principe de la version bêta du prédicteur exige de uploader un seul fichier image, puis d'appuyer sur le bouton de prédiction. Après la prédiction, appuyez sur remove pour suprimer l'image et ensuite re-uploader une image pour tester à nouveau. Répétez cette même procédure pour chaque image à tester.''',)


uploaded_files = st.file_uploader("**Uplaod file images**", accept_multiple_files=True, help='Un seul fichier a la fois pas deux en meme temps')
if uploaded_files != []:
    for uploaded_file in uploaded_files:
        save_uploadfile(uploaded_file)
    st.success("file upload")
def path_to_image_html(image):
    return '<img src="./images/'+image+'"width="60" >'

def convert_df(input_df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return input_df.to_html(escape=False, formatters=dict(images=path_to_image_html))

vector = np.vectorize(np.float_)
listimage=os.listdir("images")
if st.button("Predict"):
    st.write("")
    data = formatData("images")
    #listpredict = []
    #listimage = []
    #col,col2,__,___,___,= st.columns(5)
    #with col2:
    collabel,col2label,col3label= st.columns(3)
    with collabel:
        st.write("##### Image")
    with col2label:
        st.write("##### Predict")
    with col3label:
        st.write("##### Plot the class probability")
    st.markdown('''<hr style="border-top: 3px solid #333333;">''',unsafe_allow_html=True)
    for i in range(len(os.listdir("images"))):
        col,col2,col3= st.columns(3)
        prediction = Predict(data[i])
        with col:
            image =st.image("images/"+str(listimage[i]))
        with col2:
            st.write(prediction[0])
        #listimage.append(str(image))
        #listpredict.append(prediction)
        with col3:
            fig, ax = plt.subplots()
            axes = ["AFS","AFC","AF","AFSC","FSC","FS","FC","NC"]
            ax.bar(axes,vector(prediction[1]).tolist()[0])
            st.pyplot(fig)
        st.markdown('''<hr style="border-top: 3px solid #333333;">''',unsafe_allow_html=True)

    #df = pd.DataFrame(list(zip(listimage, listpredict)),columns=["images","result"])
    #html = convert_df(df)
    #st.markdown(
    #html,unsafe_allow_html=True)
    


    # Converting links to html tags






    #     st.image(image, caption='Image a predire')
    #     st.write("-------------------------")
    # #with col:
    # for i in range(len(data)):
    #     prediction = Predict(data[i])
    #     st.write(str(prediction).replace('None',""))  
    #     st.write("-------------------------") 
    
   
st.write("")
if st.button("remove"):
    remove("images")

   
