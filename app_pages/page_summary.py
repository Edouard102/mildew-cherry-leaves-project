import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("## **Quick Project Summary**")
    
    st.header("Context ")
    st.info(
        f"The cherry tree is indeed a plant of great importance both "
        f"economically and culturally in many regions of the world. "
        f"Its variety of cultivars and multiple uses make it a valuable "
        f"asset in agriculture, gastronomy, and health.\n\n"
        f"Cherries, with their sweet taste and juicy texture, "
        f"are highly prized in many dishes and beverages. "
        f"Their uses range from direct consumption to more elaborate "
        f"preparations such as jams, preserves, and alcoholic beverages "
        f"like kirsch. The diversity of cultivars also allows for cherries "
        f"suitable for different culinary uses. \n\n"
        f"Moreover, cherry leaves are increasingly recognized for their health benefits. "
        f"Their richness in antioxidants makes them a sought-after ingredient for "
        f"the production of teas, herbal remedies, and dietary supplements. "
        f"Their ability to reduce blood sugar levels and alleviate pain "
        f"make them a valuable element in the field of natural health.\n\n\n"
        f"Powdery mildew Diease poses a serious threat to cherry trees, "
        f"appearing as a whitish to grayish powdery coating on leaves, "
        f"stems, and sometimes even fruits. This disease can result in "
        f"leaf deformations and a deterioration in fruit quality, "
        f"leading to decreased cherry harvest yields. As a result, "
        f"growers must regularly monitor for Powdery mildew Diease, particularly during periods "
        f"conducive to its development, and consider using approved biological "
        f"control methods or chemical products to effectively manage infestation and curb its spread.\n\n"
        f"To effectively safeguard their crops and ensure optimal yields, "
        f"combating Powdery mildew Diease on cherry trees requires a proactive approach. "
        f"This approach entails regular monitoring, early detection, "
        f"and efficient infestation management. By combining these measures "
        f"with the use of approved biological control techniques or chemical "
        f"products, growers can mitigate the damage caused by Powdery mildew Diease and "
        f"maintain the health of their cherry trees.\n\n"
        f"**Source:** \n\n"
        f"* [Powdery Mildew Diease](https://en.wikipedia.org/wiki/Powdery_mildew)\n"
        f"* [Cherry](https://en.wikipedia.org/wiki/Cherry)")


    st.header("Problem Statement")
    st.warning(
        f"* The cherry plantation crop of Farmy & Foods is facing a challenge: "
        f"their cherry plantations are affected by powdery mildew.\n"
        f"* The current manual verification process takes about 30 minutes per tree. "
        f"An employee collects samples of tree leaves and "
        f"visually checks for the presence of powdery mildew, applying a specific "
        f"compound to kill the fungus if detected, adding an extra minute to each inspected tree.\n"
        f"* With thousands of cherry trees across multiple farms, this manual process is not scalable.\n"
        f"* Therefore, the company is considering implementing a machine "
        f" learning system to instantly detect powdery mildew on leaves from images." )

    
    st.header("Business Requirements")
    st.subheader("This project has 2 business requirements:")
    
    st.success(
        f"* 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.\n"
        f"* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew. "
        )


    st.header(f"Project Dataset\n")
    st.info(
        f"The dataset consists of images of 2104 healthy cherry leaves and "
        f"2104 cherry leaves infected with powdery mildew in the client's crop fields, "
        f"providing a solid foundation for developing solutions aimed at detecting "
        f"and preventing the spread of powdery mildew in their cherry crops.\n"
        f"* The dataset is sourced from "
        f"[Kaggle file](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves).")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Edouard102/mildew-cherry-leaves-project).")   

    