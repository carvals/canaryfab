# app/Dockerfile

FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/carvals/canaryfab.git .
 
#RUN pip3 install -r canaryfab/requirements.txt
RUN pip install streamlit

EXPOSE 8501
#RUN source cananryfab/stlit/bin/activate

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableCORS=false",  "--server.enableXsrfProtection=false"]