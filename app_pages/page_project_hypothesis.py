import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():

    st.write("## **Project Hypothesis and Validation**")

    st.subheader(
        f"Hypotheses for this project:")

    st.info(
        f"* Cherry tree leaves affected by powdery mildew present "
        f"a distinct visual appearance compared to healthy leaves, "
        f"characterized by a whitish or grayish powdery layer. \n"
        f"* The clear visual contrast between healthy and powdery mildew-infected leaves "
        f"allows for training a machine learning model to automatically detect the disease. "
        f"By analyzing leaf features like shape, texture, and color, the model can "
        f"accurately distinguish between the two conditions. This approach saves time "
        f"and labor compared to manual detection methods.\n"
        f"* The model should distinguish between healthy and powdery mildew-infected cherry leaves "
        f"with high accuracy, due to its ability to generalize patterns "
        f"and make precise predictions based on general characteristics."
    )

    st.subheader(
        f"Project Hypotheses Validation")

    st.success(
        f"* Cherry leaves affected by powdery mildew exhibit altered shapes, "
        f"such as distortion or curling, in addition to the presence of the "
        f"characteristic whitish or grayish powdery layer. \n\n"

        f"* An image montage visually confirms this distinction between "
        f"cherry leaves infected with powdery mildew, which have a markedly "
        f"different appearance from healthy leaves, characterized by a white or gray powdery layer \n\n")

    st.write(
        f"### Please navigate to both pages for a comprehensive view:\n" 
        f"* **ML performance Metrics** for detailed evaluation of the ML pipeline, \n "
        f"* **Leaves Visualizer** for montages of healthy and infected leaves images."

    )