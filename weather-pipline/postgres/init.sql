CREATE TABLE IF NOT EXISTS weather_data (
  id SERIAL PRIMARY KEY,
  city TEXT,
  temperature FLOAT,
  humidity INT,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);