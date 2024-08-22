import streamlit as st

# Function to run the training script
def train_model():
    import subprocess
    subprocess.run(["python", "main.py"])

# Main Page
def main_page():
    st.title("Detection of Large-Language Model (LLM) Generated Text")
    
    st.header("About the Project")
    st.write(
        """
           This project focused on developing a machine learning approach to identify text created by Large Language Models (LLMs). These advanced AI systems excel at swiftly producing convincing written content, finding use in various applications such as chatbots, automated content creation, and AI-assisted writing. As LLMs become more prevalent, the ability to differentiate between human-authored and AI-generated text grows increasingly important. This distinction is crucial for addressing issues like the spread of misinformation, potential plagiarism, and the ethical implications of AI-generated content.
         """
    )

    st.header("Project Flow")
    st.write("""
    1. **Introduction**
       - Detecting LLM-generated content is crucial in today's digital landscape. This capability plays a vital role in three key areas: combating the spread of misinformation, safeguarding academic and creative integrity by preventing plagiarism, and maintaining ethical standards in content creation and dissemination. By distinguishing between human-authored and AI-generated text, we can address these challenges and promote a more transparent and trustworthy information environment.
    
    2. **Need for Detection of LLM Generated Text**
       - **Misinformation Control:** LLMs can propagate false information quickly.
       - **Plagiarism Prevention:** Detecting LLM-generated content helps maintain integrity in research and content creation.
       - **Ethical Considerations:** Identifying the origin of text content is crucial, especially in sensitive domains like news and legal documentation.
       - **Trust and Transparency:** Detection enhances credibility by ensuring transparency about the source of text content.
    
    3. **Summary**
       - We address the challenge of detecting LLM-generated text using natural language processing (NLP) techniques. The notebook covers feature engineering, model selection, and evaluation metrics aimed at building a robust detection system.
    """)

    st.header("Results")
    st.write("""
    - **Class Distribution:** We analyzed the distribution of LLM-generated text versus human-generated text in the datasets. The combined dataset showed a balanced distribution, with X% of the data labeled as LLM-generated.
      
    - **Word Clouds:** Visual representations of word clouds for LLM-generated and human-generated text highlight the distinct patterns and vocabulary used in each category.
    
    - **Model Performance:** We trained a neural network model on TF-IDF vectors derived from text data. The model achieved high accuracy and low loss on the validation set, demonstrating its effectiveness in distinguishing between LLM-generated and human-generated text.
    """)

    st.header("Conclusion")
    st.write("""
    In conclusion, the detection of LLM-generated text plays a crucial role in maintaining the integrity and credibility of digital communication. By developing and deploying robust detection mechanisms, we can mitigate the risks associated with misinformation, plagiarism, and ethical concerns in text-based content. This notebook serves as a foundational step towards further advancements in NLP techniques for text authenticity verification.
    """)

    st.header("Implementation Notes")
    st.write("""
    - **Libraries Used:** The project utilized pandas, numpy, matplotlib, seaborn, tensorflow, and wordcloud for data handling, visualization, model building, and evaluation.
    - **Data Sources:** The datasets used in this project included 'train_v2_drcat_02.csv' and 'train_essays.csv', which were combined and processed for analysis.
    - **Model Development:** A simple neural network architecture was implemented for text classification based on TF-IDF vectors, achieving promising results in detecting LLM-generated text.
    """)

# Train Page
def train_page():
    st.title("Train Model")

    st.write("""
    Click the button below to train the model:
    """)

    if st.button("Train Model"):
        st.write("Training process started...")
        train_model()
        st.write("Training process completed.")

# Navigation
page = st.sidebar.radio("Navigation", ["Main Page", "Train Page"])

if page == "Main Page":
    main_page()
elif page == "Train Page":
    train_page()