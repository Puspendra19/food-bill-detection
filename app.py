import streamlit as st
import pandas as pd
from PIL import Image
from ocr import extract_text
from item_extractor import extract_items

st.title("Food Bill Detection System")

uploaded_file = st.file_uploader("Upload Bill Image", type=["jpg","jpeg","png"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Bill")

    text = extract_text(uploaded_file)

    st.subheader("Extracted Text")
    st.write(text)

    items, prices = extract_items(text)

    df = pd.DataFrame({
        "Item": items,
        "Price": prices
    })

    st.subheader("Detected Items")
    st.dataframe(df)

    total = sum(prices)

    st.subheader(f"Total Bill: ₹ {total}")