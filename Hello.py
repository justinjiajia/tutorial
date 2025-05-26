import streamlit as st


setup = st.Page("setup/setup.py", title="Setup guide")

text_elements = st.Page("page_elements/text_elements.py", title="Text and text formatting")
data_elements = st.Page("page_elements/data_elements.py", title="Data elements")
media_elements = st.Page("page_elements/media_elements.py", title="Media elements")

visual_intro = st.Page("charts/visual_intro.py", title="Introduction to data visualization")
builtin_charts = st.Page("charts/builtin_charts.py", title="Built-in charting functions")
create_charts = st.Page("charts/create_charts.py", title="🎯Create charts")
supported_libs = st.Page("charts/supported_libs.py", title="🚀Optional: Using external libraries")

widget_types = st.Page("widgets/widget_types.py", title="Types of widgets")
create_dynamic_chart = st.Page("widgets/create_dynamic_chart.py", title="🎯Create dynamic chart")
defaults = st.Page("widgets/tweaking_defaults.py", title="Tweaking defaults")
button = st.Page("widgets/button_behaviors.py", title="Button behaviors")
keys = st.Page("widgets/widget_keys.py", title="Widget keys")
value_init = st.Page("widgets/value_init.py", title="Initializing values via Session State")
callbacks = st.Page("widgets/callbacks.py", title="Callbacks")
show_hide_message = st.Page("widgets/show_hide_message.py", title="🎯Show and hide message")
display_image = st.Page("widgets/display_image.py", title="🎯Display image based on user input")
forms = st.Page("widgets/forms.py", title="Forms")
cleanup = st.Page("widgets/cleanup.py", title="🚀Optional: Widget clean up process")

advanced_todo_list = st.Page("widgets/advanced_todo_list.py", title="🎯Build advanced to-do list")

sidebar = st.Page("layouts/sidebar.py", title="Sidebar")
columns = st.Page("layouts/columns.py", title="Columns")
containers = st.Page("layouts/containers.py", title="Containers")

chat_UI = st.Page("layouts/chat_UI.py", title="🎯Create improved chat UI")

tabs = st.Page("layouts/tabs.py", title="Tabs")


sessions = st.Page("sessions/sessions.py", title="Sessions and Session State")
check_state_item = st.Page("sessions/check_state_item.py", title="Checking persistence of a state item")
create_todo_list = st.Page("sessions/create_todo_list.py", title="🎯Build to-do list")
count_reruns = st.Page("sessions/count_reruns.py", title="Counting reruns")

caching_intro =  st.Page("caching/caching_intro.py", title="Introduction")
data_caching =  st.Page("caching/data_caching.py", title="Data caching")
resource_caching =  st.Page("caching/resource_caching.py", title="Resource caching")

test = st.Page("test.py", title="Test")

setup_pages = [setup]
elements_pages = [text_elements, data_elements, media_elements]
charts_pages = [ visual_intro, builtin_charts, create_charts, supported_libs]
widgets_pages = [widget_types, create_dynamic_chart, defaults, button, keys, value_init, callbacks, 
                 show_hide_message, display_image, advanced_todo_list, forms, cleanup]
sessions_pages = [sessions, check_state_item, count_reruns, create_todo_list]
caching_pages = [caching_intro, data_caching, resource_caching]
layouts_pages = [sidebar, columns, containers, chat_UI, tabs]

exercise = st.Page("dashboard/dashboard.py", title="In-class exercise 5")
exercise_test = st.Page("dashboard/dashboard_1.py", title="In-class exercise test")

pg = st.navigation({"⚙️Setup": setup_pages,
                    "📑Page elements": elements_pages, 
                    "📊Charts": charts_pages, 
                    "📱Widgets": widgets_pages,
                    "🕓Sessions": sessions_pages, 
                    "🗃️Caching":  caching_pages,
                    "📰Layouts": layouts_pages, 
                    "📋In-class exercise": [exercise],
                    "Test": [test]})

pg.run()




