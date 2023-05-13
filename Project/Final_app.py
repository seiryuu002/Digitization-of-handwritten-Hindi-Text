import streamlit as st
from Preprocessor import PreProcessor as pp
from asrtoolkit import wer, cer

prep = pp()

ground_truth = st.text_input("Ground Truth")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  """#### **UPLOADED IMAGE**"""
  # call the getimage method
  image_read = prep.getImage(uploaded_file)
  #show the image
  st.image(image_read)

  deskewed_image = prep.deskewImage(image_read)
  
  processed_image, path = prep.preProcessImage(deskewed_image)

  my_expander = st.expander(label="Final Processed Image")
  with my_expander:
    st.image(processed_image, clamp=True)
  
  detected_text = prep.Digitizer(path)

  my_expander2 = st.expander(label='Digitized text')
  with my_expander2:
    st.write(detected_text)
  
  Cerate = cer(ground_truth, detected_text)
  Werate = wer(ground_truth, detected_text)

  my_expander3 = st.expander(label='Accuracy')
  with my_expander3:
    st.write("Ground truth: ", ground_truth)
    st.write("Detected Text: ", detected_text)
    st.write("Word error rate : ", Cerate)
    st.write("Character error rate: ", Werate)


