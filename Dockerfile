


#-----------------------
FROM python:3.8-slim-buster
RUN apt-get update && apt-get install make
WORKDIR /opt/W2vecGeneration
COPY . .
RUN make install
RUN python -m nltk.downloader stopwords
ENTRYPOINT ["python","src/w2vec.py"]
