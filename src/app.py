import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy

st.title("Internet Users over the years")
st.header("Internet User Population")


# ----------------------- Producing the map -------------------------
@st.cache
def load_data(path):
    df = pd.read_csv(path)
    return df

# df = pd.read_csv("share-of-individuals-using-the-internet.csv")
df = load_data(path="./data/share-of-individuals-using-the-internet.csv")
mf = df[df['Year'] == 2017]


fig2 = px.choropleth(mf,  color =  'Individuals using the Internet (% of population)',
                     # center={"lat": 48.7758, "lon": 9.1829},
                     locationmode = 'ISO-3',
                     locations = 'Code',
                     labels={"Individuals using the Internet (% of population)":"Internet<br>Users (%)",},
                     width=600,
                    height=300,
                    title="<b>Internet Users in 2017</b>",
                     color_continuous_scale="Agsunset",
                     hover_name="Entity",
                    hover_data={"Code": False,
                    "Individuals using the Internet (% of population)":':.2f'},
                            )

fig2.update_layout(margin={"r":20,"t":35,"l":0,"b":0},
                  font_family='sans-serif',
                   font_size = 10,
                  hoverlabel={"bgcolor":"white",
                              "font_size":10,
                             "font_family":'sans-serif'},
                  title={"font_size":20,
                        "xanchor":"left", "x":0,
                        "yanchor":"top"},
                  geo={"resolution":50,
                      "showlakes":False, "lakecolor":"lightblue",
                       "showocean":True, "oceancolor":"aliceblue"
                      }
                 )

# fig2.show()
st.plotly_chart(fig2)