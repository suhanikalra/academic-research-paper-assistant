# agents/database_agent.py
from neo4j import GraphDatabase

# Neo4j database credentials
uri = "neo4j://localhost:7687"
username = "suhani"
password = "12345678"
driver = GraphDatabase.driver(uri, auth=(username, password))

# Function to store research papers in the Neo4j database
def store_paper_in_db(paper_data):
    with driver.session() as session:
        session.run(
            "CREATE (p:Paper {title: $title, abstract: $abstract, year: $year})",
            title=paper_data["title"],
            abstract=paper_data["abstract"],
            year=paper_data["year"]
        )

# Function to query papers by year
def query_papers_by_year(year: int):
    with driver.session() as session:
        result = session.run("MATCH (p:Paper) WHERE p.year = $year RETURN p")
        return [{"title": record["p"]["title"], "abstract": record["p"]["abstract"]} for record in result]
