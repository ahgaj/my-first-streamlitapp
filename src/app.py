


import streamlit as st


st.set_page_config(page_title="Internet Users", # page title, displayed on the window/tab bar
                   page_icon=":bowtie:", # favicon: icon that shows on the window/tab bar (tip: you can use emojis)
                   layout="wide", # use full width of the page
                   # menu_items={
                   #     'About': "Exploration of the infection, hospital and birth rates across Switzerland."}
                   )
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy


st.title("Digital population ")


# Setting up columns
left_column, middle_column, right_column = st.columns([3, 1, 1])





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
                     labels={"Individuals using the Internet (% of population)":"Internet<br>Users (%)"},
                     width=600,
                    height=300,
                    title="<b>Internet Users in 2017 worldwide</b>",
                     color_continuous_scale="Agsunset",
                     hover_name="Entity",
                    hover_data={"Code": False,
                    "Individuals using the Internet (% of population)":':.0f'},
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

#----------------------------------------------------------------------------------------

# Widgets: selectbox
country = ['United States', 'Germany', 'France', 'Poland', 'Russia', 'China', 'India', 'Switzerland']
coun = left_column.selectbox("Choose country", country)


#--------------------------Second plot with many countries -------------------------
countr = df.Entity.unique()
countr = countr[::2]


traces = [go.Scatter(x=df[df['Entity'] == c]['Year'],
                     y=df[df['Entity'] == c]['Individuals using the Internet (% of population)'], name=c, mode='lines'
                     , hoverinfo='skip', line_width=0.6, line_color="#D3D3D3", showlegend=False) for c in countr]

# Add them to the figure, set title and hovermode
fig3 = go.Figure(
    data=traces,
    layout_hovermode='x unified',

    # layout_hovermode="x unified",
    layout=dict(

        title={"text": "<b>Internet users evolution<b>", "font": {"size": 18, 'family': 'sans-serif'}},
        plot_bgcolor="#f0f0f5",  # background applies to the figure so it is specified in the layout
        xaxis={
            'showgrid': False,
            'color': 'black',
            "title": {"font": {"size": 16, 'family': 'sans-serif'}, "text": "Year"},
            'linecolor': 'black',
            'linewidth': 3,
            'mirror': True,
        },
        yaxis={
            'showgrid': False,
            'linecolor': 'black',
            'linewidth': 2,
            'mirror': True,
            'color': 'black',
            "title": {"font": {"size": 16, 'family': 'sans-serif'}, "text": "Users in population (%)"}
        }
    )
)

fig3.update_layout(xaxis_range=[1990, 2017],     width=600,
    height=400,)

cc = coun
fig3.add_trace(go.Scatter(x=df[df['Entity'] == cc]['Year'],
                          y=df[df['Entity'] == cc]['Individuals using the Internet (% of population)'], name=cc,
                          mode='lines', line_color="purple", hovertemplate='%{y:.0f}%'))



st.plotly_chart(fig3)


st.markdown("Welcome to my first app "+":smile:")