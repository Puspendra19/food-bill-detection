import pandas as pd
from ocr import extract_text
from item_extractor import extract_items


image_path = r"C:\Users\thaku\Desktop\food_bill_detection\foodbill.jpeg"


text = extract_text(image_path)

print("Extracted Text:\n")
print(text)


items, prices = extract_items(text)


df = pd.DataFrame({
    "Item": items,
    "Price": prices
})

print("\nDetected Items:\n")
print(df)


total = sum(prices)

print("\nTotal Bill:", total)