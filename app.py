import streamlit as st
from app_pages.multipage import MultiPage


# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_leaves_visualizer import page_leaves_visualizer_body
from app_pages.page_mildew_detector import page_mildew_detector_body

app = MultiPage(app_name="Powdery Mildew Diease Detector")  # Create an instance of the app

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Leaves Visualiser", page_leaves_visualizer_body)
app.add_page("Mildew dectector", page_mildew_detector_body)

app.run()  # Run the app