import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
import os
import plotly.express as px
from PIL import Image



# Set page configuration
st.set_page_config(page_icon=":bar_chart:", layout="wide")

st.title(":bar_chart: AirBnb Data Analysis")
st.write("")
st.write("")

# Define the navigation menu
select = option_menu(
    menu_title=None,
    options=["Home", "Data Exploration", "Contact"],
    icons=["house", "bar-chart", "at"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "white", "size": "cover", "width": 100},
        "icon": {"color": "black", "font-size": "20px"},
        "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#6F36AD"},
        "nav-link-select": {"background-color": "#6F36AD"},
    },
)


# Home Section
if select == "Home":
    image1 = Image.open("D:/Airbnb/airbnb.jpg")
    st.image(image1)
    st.header("Airbnb Analysis")
    st.subheader("Airbnb, Inc.  is an American company operating an online marketplace for short- and long-term homestays and experiences. The company acts as a broker and charges a commission from each booking. The company was founded in 2008 by Brian Chesky, Nathan Blecharczyk, and Joe Gebbia. Airbnb is a shortened version of its original name, AirBedandBreakfast.com. Airbnb is the most well-known company for short-term housing rentals. For a chronological guide, see Timeline of Airbnb.After moving to San Francisco in October 2007, roommates and former schoolmates Brian Chesky and Joe Gebbia came up with an idea of putting an air mattress in their living room and turning it into a bed and breakfast. In February 2008, Nathan Blecharczyk, Chesky's former roommate, joined as the chief technology officer and the third co-founder of the new venture, which they named AirBed & Breakfast. They put together a website that offered short-term living quarters and breakfast for those who were unable to book a hotel in the saturated market.The site Airbedandbreakfast.com officially launched on August 11, 2008. The founders had their first customers in the summer of 2008, during the Industrial Design Conference held by Industrial Designers Society of America, where travelers had a hard time finding lodging in the city.")
    st.subheader("Skills take away form this Project:")
    st.subheader("Python Scripting, Data Prerprocessing, Visualization, EDA, Streamlit, MongoDb, PowerBI or Tableau")
    st.subheader("Domain:")
    st.subheader("Travel Industry, Property Management and Tourism")

# Data Exploration Section
elif select == "Data Exploration":
    # Sidebar with file upload
    fl = st.file_uploader(":file_folder: Upload a file", type=["csv", "txt", "xlsx", "xls"])

    # Check if a file has been uploaded
    if fl is not None:
        file_name = fl.name
        st.write(file_name)
        df = pd.read_csv(fl, encoding="ISO-8859-1")

    # Sidebar with select options for each analysis
        with st.sidebar:
            st.title("Select Analysis")
            analysis_type = st.selectbox("Choose Analysis", ["Price Analysis", "Availability Analysis", "Location Based Analysis", "Geospatial Visualization", "Top Charts"])
            # Remove blur effect from dropdown
            st.markdown(
                """
                <style>
                .st-ef {
                    background-color: transparent !important;
                }
                .st-ef .st-cq {
                    color: black !important;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
        if analysis_type == "Price Analysis":
            st.title("**PRICE ANALYSIS**")
            col1,col2= st.columns(2)

            with col1:
                       
                country= st.selectbox("Select the Country",df["country"].unique())

                df1= df[df["country"] == country]
                df1.reset_index(drop= True, inplace= True)

                room_ty= st.selectbox("Select the Room Type",df1["room_type"].unique())
                
                df2= df1[df1["room_type"] == room_ty]
                df2.reset_index(drop= True, inplace= True)

                df_bar= pd.DataFrame(df2.groupby("property_type")[["price","review_scores","number_of_reviews"]].sum())
                df_bar.reset_index(inplace= True)

                fig_bar= px.bar(df_bar, x='property_type', y= "price", title= "PRICE FOR PROPERTY_TYPES",hover_data=["number_of_reviews","review_scores"],color_discrete_sequence=px.colors.sequential.Redor_r, width=600, height=500)
                st.plotly_chart(fig_bar)

        
            with col2:
            
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
        
                proper_ty= st.selectbox("Select the Property_type",df2["property_type"].unique())

                df4= df2[df2["property_type"] == proper_ty]
                df4.reset_index(drop= True, inplace= True)

                df_pie= pd.DataFrame(df4.groupby("host_response_time")[["price","bedrooms"]].sum())
                df_pie.reset_index(inplace= True)

                fig_pi= px.pie(df_pie, values="price", names= "host_response_time",
                                hover_data=["bedrooms"],
                                color_discrete_sequence=px.colors.sequential.BuPu_r,
                                title="PRICE DIFFERENCE BASED ON HOST RESPONSE TIME",
                                width= 600, height= 500)
                st.plotly_chart(fig_pi)

            col1,col2= st.columns(2)

            with col1:

            
                hostresponsetime= st.selectbox("Select the host_response_time",df4["host_response_time"].unique())

                df5= df4[df4["host_response_time"] == hostresponsetime]

                df_do_bar= pd.DataFrame(df5.groupby("bed_type")[["minimum_nights","maximum_nights","price"]].sum())
                df_do_bar.reset_index(inplace= True)

                fig_do_bar = px.bar(df_do_bar, x='bed_type', y=['minimum_nights', 'maximum_nights'], 
                title='MINIMUM NIGHTS AND MAXIMUM NIGHTS',hover_data="price",
                barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow, width=600, height=500)
                

                st.plotly_chart(fig_do_bar)

            with col2:

                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")

                df_do_bar_2= pd.DataFrame(df5.groupby("bed_type")[["bedrooms","beds","accommodates","price"]].sum())
                df_do_bar_2.reset_index(inplace= True)

                fig_do_bar_2 = px.bar(df_do_bar_2, x='bed_type', y=['bedrooms', 'beds', 'accommodates'], 
                title='BEDROOMS AND BEDS ACCOMMODATES',hover_data="price",
                barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow_r, width= 600, height= 500)
            
                st.plotly_chart(fig_do_bar_2)

        elif analysis_type == "Availability Analysis":
            st.title("**AVAILABILITY ANALYSIS**")

            def datafr():
                df_a= pd.read_csv("D:/Airbnb/Airbnb.csv")
                return df_a

            df_a= datafr()
            col1,col2= st.columns(2)

            with col1:
            
            
                country_a= st.selectbox("Select the Country_a",df_a["country"].unique())

                df1_a= df[df["country"] == country_a]
                df1_a.reset_index(drop= True, inplace= True)

                property_ty_a= st.selectbox("Select the Property Type",df1_a["property_type"].unique())
                
                df2_a= df1_a[df1_a["property_type"] == property_ty_a]
                df2_a.reset_index(drop= True, inplace= True)

                df_a_sunb_30= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_30",width=600,height=500,title="Availability_30",color_discrete_sequence=px.colors.sequential.Peach_r)
                st.plotly_chart(df_a_sunb_30)
        
            with col2:
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                

                df_a_sunb_60= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_60",width=600,height=500,title="Availability_60",color_discrete_sequence=px.colors.sequential.Blues_r)
                st.plotly_chart(df_a_sunb_60)

            col1,col2= st.columns(2)

            with col1:
            
                df_a_sunb_90= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_90",width=600,height=500,title="Availability_90",color_discrete_sequence=px.colors.sequential.Aggrnyl_r)
                st.plotly_chart(df_a_sunb_90)

            with col2:

                df_a_sunb_365= px.sunburst(df2_a, path=["room_type","bed_type","is_location_exact"], values="availability_365",width=600,height=500,title="Availability_365",color_discrete_sequence=px.colors.sequential.Greens_r)
                st.plotly_chart(df_a_sunb_365)
        
            roomtype_a= st.selectbox("Select the Room Type_a", df2_a["room_type"].unique())

            df3_a= df2_a[df2_a["room_type"] == roomtype_a]

            df_mul_bar_a= pd.DataFrame(df3_a.groupby("host_response_time")[["availability_30","availability_60","availability_90","availability_365","price"]].sum())
            df_mul_bar_a.reset_index(inplace= True)

            fig_df_mul_bar_a = px.bar(df_mul_bar_a, x='host_response_time', y=['availability_30', 'availability_60', 'availability_90', "availability_365"], 
            title='AVAILABILITY BASED ON HOST RESPONSE TIME',hover_data="price",
            barmode='group',color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)

            st.plotly_chart(fig_df_mul_bar_a)


        elif analysis_type == "Location Based Analysis":
            st.title("**LOCATION BASED ANALYSIS**")
            st.write("")

            def datafr():
                df= pd.read_csv("D:/Airbnb/Airbnb.csv")
                return df

            def select_the_df(df2_l, sel_val):
                if sel_val == str(df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df2_l['price'].min())+' '+str("(30% of the Value)"):
                    df_val_30= df2_l[df2_l["price"] <= differ_max_min*0.30 + df2_l['price'].min()]
                    df_val_30.reset_index(drop= True, inplace= True)
                    return df_val_30
                elif sel_val == str(differ_max_min*0.30 + df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df2_l['price'].min())+' '+str("(30% to 60% of the Value)"):
                    df_val_60= df2_l[df2_l["price"] >= differ_max_min*0.30 + df2_l['price'].min()]
                    df_val_60_1= df_val_60[df_val_60["price"] <= differ_max_min*0.60 + df2_l['price'].min()]
                    df_val_60_1.reset_index(drop= True, inplace= True)
                    return df_val_60_1
                elif sel_val == str(differ_max_min*0.60 + df2_l['price'].min())+' '+str('to')+' '+str(df2_l['price'].max())+' '+str("(60% to 100% of the Value)"):
                    df_val_100= df2_l[df2_l["price"] >= differ_max_min*0.60 + df2_l['price'].min()]
                    df_val_100.reset_index(drop= True, inplace= True)
                    return df_val_100

            df_l= datafr()

            country_l= st.selectbox("Select the Country_l", df_l["country"].unique())

            df1_l= df_l[df_l["country"] == country_l]
            df1_l.reset_index(drop= True, inplace= True)

            proper_ty_l= st.selectbox("Select the Property_type_l", df1_l["property_type"].unique())

            df2_l= df1_l[df1_l["property_type"] == proper_ty_l]
            df2_l.reset_index(drop= True, inplace= True)

            st.write("")

            differ_max_min= df2_l['price'].max() - df2_l['price'].min()

            val_sel= st.radio("Select the Price Range", [str(df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.30 + df2_l['price'].min())+' '+str("(30% of the Value)"),
                                                        str(differ_max_min*0.30 + df2_l['price'].min())+' '+str('to')+' '+str(differ_max_min*0.60 + df2_l['price'].min())+' '+str("(30% to 60% of the Value)"),
                                                        str(differ_max_min*0.60 + df2_l['price'].min())+' '+str('to')+' '+str(df2_l['price'].max())+' '+str("(60% to 100% of the Value)")])

            df_val_sel= select_the_df(df2_l, val_sel)

            st.dataframe(df_val_sel)

            # Checking the correlation
            df_val_sel_corr= df_val_sel.drop(columns=["listing_url","name", "property_type",                 
                                                    "room_type", "bed_type","cancellation_policy",
                                                    "images","host_url","host_name", "host_location",                   
                                                    "host_response_time", "host_thumbnail_url",            
                                                    "host_response_rate","host_is_superhost","host_has_profile_pic" ,         
                                                    "host_picture_url","host_neighbourhood",
                                                    "host_identity_verified","host_verifications",
                                                    "street", "suburb", "government_area", "market",                        
                                                    "country", "country_code","location_type","is_location_exact",
                                                    "amenities"]).corr()

            st.dataframe(df_val_sel_corr)

            df_val_sel_gr= pd.DataFrame(df_val_sel.groupby("accommodates")[["cleaning_fee","bedrooms","beds","extra_people"]].sum())
            df_val_sel_gr.reset_index(inplace= True)

            fig_1= px.bar(df_val_sel_gr, x="accommodates", y= ["cleaning_fee","bedrooms","beds"], title="ACCOMMODATES",
                        hover_data= "extra_people", barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
            st.plotly_chart(fig_1)

            room_ty_l= st.selectbox("Select the Room_Type_l", df_val_sel["room_type"].unique())

            df_val_sel_rt= df_val_sel[df_val_sel["room_type"] == room_ty_l]

            fig_2= px.bar(df_val_sel_rt, x= ["street","host_location","host_neighbourhood"],y="market", title="MARKET",
                        hover_data= ["name","host_name","market"], barmode='group',orientation='h', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
            st.plotly_chart(fig_2)

            fig_3= px.bar(df_val_sel_rt, x="government_area", y= ["host_is_superhost","host_neighbourhood","cancellation_policy"], title="GOVERNMENT_AREA",
                        hover_data= ["guests_included","location_type"], barmode='group', color_discrete_sequence=px.colors.sequential.Rainbow_r,width=1000)
            st.plotly_chart(fig_3)



        elif analysis_type == "Geospatial Visualization":
            st.title("**GEOSPATIAL VISUALIZATION**")
            st.write("")

            fig_4 = px.scatter_mapbox(df, lat='latitude', lon='longitude', color='price', size='accommodates',
                            color_continuous_scale= "rainbow",hover_name='name',range_color=(0,49000), mapbox_style="carto-positron",
                            zoom=1)
            fig_4.update_layout(width=1150, height=800, title='Geospatial Distribution of Listings')
            st.plotly_chart(fig_4)   


        elif analysis_type == "Top Charts":
            st.title("**TOP CHARTS**")
            st.write("")

            country_t= st.selectbox("Select the Country_t",df["country"].unique())

            df1_t= df[df["country"] == country_t]

            property_ty_t= st.selectbox("Select the Property_type_t",df1_t["property_type"].unique())

            df2_t= df1_t[df1_t["property_type"] == property_ty_t]
            df2_t.reset_index(drop= True, inplace= True)

            df2_t_sorted= df2_t.sort_values(by="price")
            df2_t_sorted.reset_index(drop= True, inplace= True)


            df_price= pd.DataFrame(df2_t_sorted.groupby("host_neighbourhood")["price"].agg(["sum","mean"]))
            df_price.reset_index(inplace= True)
            df_price.columns= ["host_neighbourhood", "Total_price", "Avarage_price"]
            
            col1, col2= st.columns(2)

            with col1:
                
                fig_price= px.bar(df_price, x= "Total_price", y= "host_neighbourhood", orientation='h',
                                title= "PRICE BASED ON HOST_NEIGHBOURHOOD", width= 600, height= 800)
                st.plotly_chart(fig_price)

            with col2:

                fig_price_2= px.bar(df_price, x= "Avarage_price", y= "host_neighbourhood", orientation='h',
                                    title= "AVERAGE PRICE BASED ON HOST_NEIGHBOURHOOD",width= 600, height= 800)
                st.plotly_chart(fig_price_2)

            col1, col2= st.columns(2)

            with col1:

                df_price_1= pd.DataFrame(df2_t_sorted.groupby("host_location")["price"].agg(["sum","mean"]))
                df_price_1.reset_index(inplace= True)
                df_price_1.columns= ["host_location", "Total_price", "Avarage_price"]
                
                fig_price_3= px.bar(df_price_1, x= "Total_price", y= "host_location", orientation='h',
                                    width= 600,height= 800,color_discrete_sequence=px.colors.sequential.Bluered_r,
                                    title= "PRICE BASED ON HOST_LOCATION")
                st.plotly_chart(fig_price_3)

            with col2:

                fig_price_4= px.bar(df_price_1, x= "Avarage_price", y= "host_location", orientation='h',
                                    width= 600, height= 800,color_discrete_sequence=px.colors.sequential.Bluered_r,
                                    title= "AVERAGE PRICE BASED ON HOST_LOCATION")
                st.plotly_chart(fig_price_4)


            room_type_t= st.selectbox("Select the Room_Type_t",df2_t_sorted["room_type"].unique())

            df3_t= df2_t_sorted[df2_t_sorted["room_type"] == room_type_t]

            df3_t_sorted_price= df3_t.sort_values(by= "price")

            df3_t_sorted_price.reset_index(drop= True, inplace = True)

            df3_top_50_price= df3_t_sorted_price.head(100)

            fig_top_50_price_1= px.bar(df3_top_50_price, x= "name",  y= "price" ,color= "price",
                                    color_continuous_scale= "rainbow",
                                    range_color=(0,df3_top_50_price["price"].max()),
                                    title= "MINIMUM_NIGHTS MAXIMUM_NIGHTS AND ACCOMMODATES",
                                    width=1200, height= 800,
                                    hover_data= ["minimum_nights","maximum_nights","accommodates"])
            
            st.plotly_chart(fig_top_50_price_1)

            fig_top_50_price_2= px.bar(df3_top_50_price, x= "name",  y= "price",color= "price",
                                    color_continuous_scale= "greens",
                                    title= "BEDROOMS, BEDS, ACCOMMODATES AND BED_TYPE",
                                    range_color=(0,df3_top_50_price["price"].max()),
                                    width=1200, height= 800,
                                    hover_data= ["accommodates","bedrooms","beds","bed_type"])

            st.plotly_chart(fig_top_50_price_2)
        
        else:
            st.write("Please upload a file to proceed.")



# Contact Section
elif select == "Contact":
    st.title("Contact Details")
    st.header('Airbnb Analysis')
    st.subheader(
        "This project aims to analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends.")
    st.write("---")
    st.subheader("Abdul Salam M")
    st.write("""
    For any inquiries or feedback, please contact at:
    
    - **Email**: [abdulsalam47492@gmail.com](mailto:abdulsalam47492@gmail.com)
    - **LinkedIn**: https://www.linkedin.com/in/abdul-salam-m-02801716b/
    - **Github**: https://github.com/Abdulsalam-47
    """)
