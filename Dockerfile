FROM python:3.8.0-buster
WORKDIR /project

COPY static/style.css .
COPY static/highest-profit.png .
COPY templates/index.html .
COPY templates/chatbot.html .
COPY config.py .
COPY ./Nifty-50-dataset .
COPY train_chatbot.py .
COPY intents.json .
COPY chatbot_model.h5 .
COPY classes.pkl .
COPY words.pkl .
COPY Stock-Market-Data.csv .
COPY stock_analysis.py .
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .
CMD ["python3", "app.py"]
