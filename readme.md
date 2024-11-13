https://youtu.be/aQFfe4ZwBpc


-> steps and dependencies required to startup , backend, frontend, and db server( neo4j)
->let me give code walk through of all apis.
->created requied modes and ui page
->tools used fastapi, Ollama, requesters, neo4j(graph databases), streamlit ( UI)
-> let me give a demo and also my db is up and running

1. Interact with the Application
-In the Streamlit app (at http://localhost:8501), enter a research topic and use the search or chat features as you designed.
-The frontend will send requests to the FastAPI backend, which should respond with relevant data or summaries.


2.Running the Application
-Backend: Running on http://127.0.0.1:8000 (FastAPI)
-Frontend: Running on http://localhost:8501 (Streamlit)


3 .Stopping the Application
-To stop the backend and frontend, return to each terminal where they’re running and press CTRL + C.


4.
- start backend : 
go to backend dir
uvicorn main:app --reload



5
- start fronted : 
go to frontend dir
streamlit run app.py

Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
.\venv\Scripts\activate

 cd application/backend

 pip install neo4j-driver==1.6.2

 python -m venv myevn
