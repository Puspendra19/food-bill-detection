import re

def extract_items(text):

    items = []
    prices = []

    
    text = text.replace("₹", "")

    lines = text.split("\n")

    ignore_words = [
        "gst","invoice","total","cgst","sgst",
        "ref","payment","code","order","date",
        "visa","upi","bharat","card","transaction"
    ]

    for line in lines:

        line = line.strip()

        # ignore unwanted lines
        if any(word in line.lower() for word in ignore_words):
            continue

        # match item + price
        match = re.search(r'(.+?)\s+(\d+\.\d+)$', line)

        if match:
            item = match.group(1)
            price = float(match.group(2))

            items.append(item)
            prices.append(price)

    return items, prices