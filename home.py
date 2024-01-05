import streamlit as st
import requests
import pandas as pd

beverages = requests.get(f'http://localhost:8000/beverages/').json()

df = pd.DataFrame(
    {   
        "id" : [beverage[0] for beverage in beverages],
        "name": [beverage[1] for beverage in beverages],
        "price": [beverage[2] for beverage in beverages],
        "picture": [beverage[3] for beverage in beverages],
        "qtd": [beverage[4] for beverage in beverages],
        "category": [beverage[5] for beverage in beverages],
        "is_active": [beverage[6] for beverage in beverages],
    }
)
st.title("All Beverages")
st.markdown(":blue[As DataFrame]")
st.dataframe(df)
st.markdown(":blue[As Cards]")
cols = st.columns(len(beverages))
for i, elem in enumerate(cols):
    beverage = beverages[i]
    with elem:
        #data
        id = beverage[0]
        name = beverage[1]
        price = beverage[2]
        picture = beverage[3]
        qtd = beverage[4]
        category = beverage[5]
        is_active = beverage[6]
        #show item
        st.subheader(f"{name}")
        st.image(picture, caption="Mock image, not actual product")
        st.write(f"Price: R${price}")
        #json response
        st.markdown(":green[Full JSON Response:]")
        st.write(beverages[i])
            
