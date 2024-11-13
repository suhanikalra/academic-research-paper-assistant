# agents/search_agent.py
import requests
import xml.etree.ElementTree as ET

def search_papers(query: str):
    url = f'http://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=5'
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch papers")

    # Parse XML response
    papers = []
    root = ET.fromstring(response.text)
    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        title = entry.find('{http://www.w3.org/2005/Atom}title').text
        abstract = entry.find('{http://www.w3.org/2005/Atom}summary').text
        year = entry.find('{http://www.w3.org/2005/Atom}published').text[:4]
        papers.append({"title": title, "abstract": abstract, "year": int(year)})
    return papers
