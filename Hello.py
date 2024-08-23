import streamlit as st

data_elements = st.Page("page_elements/data_elements.py", title="Data elements")
media_elements = st.Page("page_elements/media_elements.py", title="Media elements")

visual_intro = st.Page("charts/visual_intro.py", title="Introduction to data visualization")
native_charts = st.Page("charts/builtin_charting_functions.py", title="Built-in charting functions")
create_charts = st.Page("charts/create_charts.py", title="🎯Practice: Create charts")
supported_libs = st.Page("charts/supported_libs.py", title="🚀Optional: Using external libraries")

intro = st.Page("widgets/intro.py", title="Introduction")
create_dynamic_chart = st.Page("widgets/create_dynamic_chart.py", title="🎯Practice: Create dynamic chart")
defaults = st.Page("widgets/tweaking_defaults.py", title="Tweaking defaults")
button = st.Page("widgets/button_behaviors.py", title="Button behaviors")
keys = st.Page("widgets/widget_keys.py", title="Widget keys")
value_init = st.Page("widgets/value_init.py", title="Initializing values via Session State")
callbacks = st.Page("widgets/callbacks.py", title="Callbacks")
show_hide_message = st.Page("widgets/show_hide_message.py", title="🎯Practice: Show and hide message")
display_image = st.Page("widgets/display_image.py", title="🎯Practice: Display image based on user input")
forms = st.Page("widgets/forms.py", title="Forms")
cleanup = st.Page("widgets/cleanup.py", title="🚀Optional: Widget clean up process")

advanced_todo_list = st.Page("widgets/advanced_todo_list.py", title="🎯Practice: Advanced to-do list")

sidebar = st.Page("layouts/sidebar.py", title="Sidebar")
columns = st.Page("layouts/columns.py", title="Columns")
containers = st.Page("layouts/containers.py", title="Containers")

chat_UI = st.Page("layouts/chat_UI.py", title="🎯Practice: An improved chat UI")

tabs = st.Page("layouts/tabs.py", title="Tabs")


sessions = st.Page("sessions/sessions.py", title="Session and Session State")
check_state_item = st.Page("sessions/check_state_item.py", title="Check persistence of a state item")
create_todo_list = st.Page("sessions/create_todo_list.py", title="🎯Practice: Create to-do list")
test = st.Page("test.py", title="Test")

elements_pages = [data_elements, media_elements]
charts_pages = [ visual_intro, native_charts, create_charts, supported_libs]
widgets_pages = [intro, create_dynamic_chart, defaults, button, keys, value_init, callbacks, 
                 show_hide_message, display_image, advanced_todo_list, forms, cleanup]
sessions_pages = [sessions, check_state_item, create_todo_list]
layouts_pages = [sidebar, columns, containers, chat_UI, tabs]

pg = st.navigation({"📑Page elements": elements_pages, "📊Charts": charts_pages, "📱Widgets": widgets_pages,  "🕓Sessions": sessions_pages, 
                    "📰Layouts": layouts_pages, 
                    "Test": [test]})

pg.run()




