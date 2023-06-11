import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title('My Mom New Healthy Dinner')
streamlit.header('Breakfast Menu')
streamlit.text('🥗 Omega 3 & Blueberry Oatmeal')
streamlit.text( '🐔 Kale, Spinach & Rocket Smoothie')
streamlit.text('🥑 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
# Let's put a pick list here so they can pick the fruit they want to include 
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick some Fruits: ", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)


#Let's pick list here so they can pick fruits that they want to include
fruits_selected = streamlit.multiselect("Pick some Fruits: :", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)


def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice) 
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
try:
   fruit_choice = streamlit.text_input('What fruit would you like information about?')
   if not fruit_choice:
        streamlit.error("Please select a fruit to get information.")
   else:
       back_from_function = get_fruityvice_data(fruit_choice)
       streamlit.dataframe(back_from_function)
       
except URLError as e:
    streamlit.error()
  
streamlit.write('The user entered ', fruit_choice)

#import requests



# write your own comment -what does the next line do? 

# write your own comment - what does this do?


#streamlit.stop()

#import snowflake.connector

streamlit.header("The fruit load list contains:")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("select * from fruit_load_list")
         return my_cur.fetchall()
    
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)
    
 
add_my_fruit = streamlit.text_input('What fruit would you like to add?')


def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
         my_cur.execute(f"insert into fruit_load_list values ('{new_fruit}')")
         return "Thanks for adding " + new_fruit
    
    
if streamlit.button('Add a Fruit to the list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.dataframe(back_from_function)
    

streamlit.write('Thanks for adding ', add_my_fruit)    
streamlit.stop()    






File "/home/appuser/venv/lib/python3.9/site-packages/streamlit/runtime/scriptrunner/script_runner.py", line 552, in _run_script
    exec(code, module.__dict__)
File "/app/first_streamlit.app/streamlit_app.py", line 93, in <module>
    streamlit.dataframe(back_from_function)
File "/home/appuser/venv/lib/python3.9/site-packages/streamlit/runtime/metrics_util.py", line 356, in wrapped_func
    result = non_optional_func(*args, **kwargs)
File "/home/appuser/venv/lib/python3.9/site-packages/streamlit/elements/dataframe_selector.py", line 180, in dataframe
    return self.dg._arrow_dataframe(
File "/home/appuser/venv/lib/python3.9/site-packages/streamlit/runtime/metrics_util.py", line 356, in wrapped_func
    result = non_optional_func(*args, **kwargs)
File "/home/appuser/venv/lib/python3.9/site-packages/streamlit/elements/arrow.py", line 180, in _arrow_dataframe
    data_df = type_util.convert_anything_to_df(data, ensure_copy=False)
File "/home/appuser/venv/lib/python3.9/site-packages/streamlit/type_util.py", line 549, in convert_anything_to_df
    raise errors.StreamlitAPIException(
