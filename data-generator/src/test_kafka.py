from kafka import KafkaProducer
from dotenv import load_dotenv
import os

load_dotenv()

broker = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
topic = os.getenv("KAFKA_TOPIC")

print(f"Connecting to Kafka: {broker}")
print(f"Topic: {topic}")

try:
    producer = KafkaProducer(
        bootstrap_servers=broker
    )

    print("✅ Kafka connection successful!")

    producer.close()

except Exception as e:
    print("❌ Kafka connection failed!")
    print(f"Error: {e}")