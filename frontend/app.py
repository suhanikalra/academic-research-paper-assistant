# main.py
import streamlit as st
import requests

# Streamlit setup
st.set_page_config(page_title="Academic Research Paper Assistant", page_icon="📚")
st.title("Academic Research Paper Assistant")

# Sidebar information
st.sidebar.title("📑 Explore the System")
st.sidebar.markdown("""
    Welcome to the **Academic Research Paper Assistant**! Below are the available features:

    - **🔍 Search for Papers**: Discover research papers on a specific topic or field of study.
    - **💬 Ask Paper-Related Questions**: Interact with the paper's abstract by asking questions to gain deeper insights.
    - **🔮 Generate Future Research Ideas**: Explore future research directions based on the paper’s content.
    - **💾 Store Research Papers**: Store papers in your personalized database for future reference and easy access.
""")

# Search Papers Section
st.header("🔍 Search for Research Papers")
topic = st.text_input("Enter Research Topic", placeholder="e.g., Self-Supervised Learning for Document Understanding")

if topic:
    if st.button("🔎 Search Papers"):
        with st.spinner("Searching for papers..."):
            response = requests.get(f'http://localhost:8000/search_papers?query={topic}')
            if response.status_code == 200:
                papers = response.json().get('papers', [])
                if papers:
                    st.write(f"### Found {len(papers)} papers:")
                    for paper in papers:
                        with st.expander(f"📄 {paper['title']} ({paper['year']})"):
                            st.write(f"**Abstract**: {paper['abstract']}")

                            # Ask a question about the paper
                            question = st.text_input(f"Ask a question about '{paper['title']}'", key=f"question_{paper['title']}")
                            if question:
                                with st.spinner("Getting the answer..."):
                                    answer_response = requests.post(
                                        "http://localhost:8000/answer_question",
                                        json={"question": question, "context": paper['abstract']}
                                    )
                                    if answer_response.status_code == 200:
                                        answer_data = answer_response.json()
                                        answer_text = answer_data.get('answer', 'No answer found')
                                        if 'error' in answer_data:
                                            st.error(f"Error: {answer_data['error']}")
                                        else:
                                            st.write(f"**Answer**: {answer_text}")
                                    else:
                                        st.error("Error retrieving the answer from the backend.")

                            # Generate future research ideas
                            if st.button(f"🔮 Generate Future Research Ideas for {paper['title']}", key=f"future_works_{paper['title']}"):
                                with st.spinner("Generating future research ideas..."):
                                    future_work_response = requests.post(
                                        "http://localhost:8000/generate_future_works",
                                        json={"context": paper['abstract']}
                                    )
                                    if future_work_response.status_code == 200:
                                        future_work_data = future_work_response.json()
                                        future_text = future_work_data.get('future_works', 'No ideas found')
                                        st.write(f"**Future Works**: {future_text}")
                                    else:
                                        st.error("Error generating future research ideas.")
                else:
                    st.write("No papers found for this topic.")
            else:
                st.error("Error in retrieving papers.")

# Store Papers Section
st.header("💾 Store Research Papers in Database")
title = st.text_input("Paper Title")
abstract = st.text_area("Paper Abstract")
year = st.number_input("Year", min_value=1900, max_value=2024, value=2024)

if st.button("💾 Save Paper"):
    if title and abstract and year:
        paper_data = {"title": title, "abstract": abstract, "year": year}
        with st.spinner("Storing paper..."):
            response = requests.post("http://localhost:8000/store_paper", json=paper_data)
            if response.status_code == 200:
                st.success(response.json()["message"])
            else:
                st.error("Error storing paper.")
    else:
        st.warning("Please fill in all fields before storing the paper.")
