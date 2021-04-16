# Stock_Market_Analysis_Chatbot_UI
The dataset for the Stock Market Analysis has been taken from Kaggle's Nifty-50 Dataset.
The application is created using Python3.8.0 and Flask.
To run the application-Create a virtual environment first and then install the requirements file using-> pip install -r requirements.txt
Finally run the application using python -m flask run or python app.py

To build the dockerfile use-> sudo docker build --tag stock-market-info .

To run the dockerfile use-> sudo  docker run --network="host" stock-market-info:latest
