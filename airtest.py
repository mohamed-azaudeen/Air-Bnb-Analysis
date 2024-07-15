import plotly.express as px
import pandas as pd
import streamlit as st

st.set_page_config(layout='wide')

df = pd.read_csv('sample_data.csv')


st.title(":red[Air BNB - Data Visualization]")

st.subheader(':blue[ Total Sum Of Price - Country]',divider='blue')

country = df.groupby(['Country'])['Price'].sum()

fig_country = px.bar(country,orientation='v',text_auto=True,color_discrete_sequence=px.colors.sequential.Mint_r,width=1100,height=500)
st.plotly_chart(fig_country)

col1,col2 = st.columns(2)
with col1:
    fig_pie_1 = px.pie(data_frame=df , names='Country' ,values='Price' ,hole=0.5,width=500,color_discrete_sequence=px.colors.sequential.haline_r)
    st.plotly_chart(fig_pie_1)
with col2:
    st.dataframe(country,width=500)    

st.subheader(':rainbow[ Total Sum Of Price - Property Type]',divider='rainbow')

a = df[['Property type','Country','Price']]
fig_property = px.bar(a,x='Property type',y='Country',hover_data='Price',color='Property type',orientation='h',color_discrete_sequence=px.colors.cyclical.mygbm_r,width=1100,height=500)
st.plotly_chart(fig_property)

col1,col2 = st.columns(2)
with col1:
    property = df.groupby(['Property type'])['Price'].sum()
    fig_property = px.area(property,orientation='v',color_discrete_sequence=px.colors.carto.Armyrose_r,width=535)
    st.plotly_chart(fig_property)
with col2:
    st.dataframe(property,width=500)    

st.subheader(':orange[Seasonal Analysis - Country]',divider='orange')

country_data = df.groupby('Country').agg(
    average_price=('Price', 'mean'),
    total_reviews=('number_of_reviews', 'sum')
).reset_index()

fig = px.choropleth(
    country_data,
    locations='Country',
    locationmode='country names',
    color='average_price',
    hover_name='Country',
    hover_data=['average_price', 'total_reviews'],
    title='Average Price and Total Reviews by Country',
    color_continuous_scale=px.colors.sequential.Agsunset_r,
    height=600,
    width=1100,

)


fig.update_geos(fitbounds="locations", visible=True)
st.plotly_chart(fig)

fig = px.scatter_mapbox(df, lat="Lattitude", lon="Longitude", color="Price",hover_name='Country',
                        size="Price", color_continuous_scale=px.colors.cyclical.mygbm_r, size_max=50, zoom=1,title='Total Sum Of Price - Country', height=500,width=1100, 
                        mapbox_style='carto-darkmatter')

st.plotly_chart(fig)

st.subheader(':violet[ Total No Of reveiws - Property Type]',divider='violet')

fig_sun = px.sunburst(df,path=['Property type','Country'],values='number_of_reviews',color_discrete_sequence=px.colors.sequential.Brwnyl,width=1000,height=600)
st.plotly_chart(fig_sun)