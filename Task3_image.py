        # Dabhi Dhruvi R
        # Task 3 
        # Thank You :->CodSoft
        # API :-> HuggingFaceAPI

import streamlit as st
import requests

# Here I use Hugging Face API for the Image Captionning 
API_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
headers = {"Authorization": "Bearer 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"}

def query(image_data):
    # Send The request
    response = requests.post(API_URL, headers=headers, data=image_data)
    return response.json()

def main():
    st.title("Image Captioning")
    
    # Allow user to upload an image file Any image from 
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Showing the images which user Upload
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
        
        # Get The Images 
        image_data = uploaded_file.read()
        
        
        output = query(image_data)
        
        # Display the generatedText According To the Images 
        st.write("Generated Caption:")
        st.write(output)

if __name__ == "__main__":
    main()
