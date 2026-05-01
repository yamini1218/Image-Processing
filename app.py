#Main StreamLit application
import streamlit as st
from PIL import Image
from filters import apply_filters
from io import BytesIO

st.set_page_config(page_title='Image Editor',layout='wide')
st.title(":camera: Image Processing App :sparkles:")
uploaded_file=st.file_uploader('Upload an image', type=['jpg','jpeg','png'])
with st.sidebar: 
  blur=st.slider('Blur', min_value=0, max_value=51)
  sharpness=st.slider('Sharpness', min_value=0.0, max_value=3.0)
  bright=st.slider('Brightness', min_value=-100, max_value=100,value=0)
  contrast=st.slider('Contrast', min_value=0.0, max_value=3.0)
  if uploaded_file is not None:
    image = Image.open(uploaded_file)
    default_w, default_h = image.size
  else:
    default_w, default_h = 500, 500
  width=st.slider('Width', min_value=100, max_value=2000, value=default_w)
  height=st.slider('Height', min_value=100, max_value=2000, value=default_h)
  edge=st.toggle('Edge Detection')
  if edge:
    thresh1=st.slider("Threshold 1", 0, 255, 100)
    thresh2=st.slider("Threshold 2", 0, 255, 200)
  else:
    thresh1,thresh2=None,None
  gray=st.toggle('Grayscale')


if uploaded_file is not None:
    image=Image.open(uploaded_file)
    processed_image=apply_filters(
        image,
        blur,
        sharpness,
        bright,
        contrast,
        edge,
        gray,
        thresh1,
        thresh2
    )
    image=image.resize((width,height))
    processed_image=processed_image.resize((width,height))
    buffer = BytesIO()
    processed_image = processed_image.convert("RGB")
    processed_image.save(buffer, format="PNG")
    img_bytes = buffer.getvalue()

    col1, col2 = st.columns(2)
    with col1:
      st.image(image, caption="Original", use_container_width=True)

    with col2:
      st.image(processed_image, caption="Processed", use_container_width=True)
    st.download_button(
        label="Download Image",
        data=img_bytes,
        file_name="processed.png",
        mime="image/png"
      )