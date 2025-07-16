import requests , json , time
from kafka import KafkaProducer
from dotenv import load_dotenv

import os

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "London"
TOPIC = "weather_data"

producer = KafkaProducer(bootstrap_servers='kafka:9092',value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
    res = requests.get(url).json()
    producer.send(TOPIC, value=res)
    print(res)
    time.sleep(300)