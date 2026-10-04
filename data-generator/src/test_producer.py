from dotenv import load_dotenv
import os

from src.transaction_generator import generate_transaction
from src.kafka_producer import TransactionProducer

load_dotenv()

broker = os.getenv("KAFKA_BOOTSTRAP_SERVERS")
topic = os.getenv("KAFKA_TOPIC")

print(f"Kafka: {broker}")
print(f"Topic: {topic}")

producer = TransactionProducer(broker, topic)

transaction = generate_transaction()

print("\nSending transaction:")
print(transaction)

producer.send(transaction)
producer.flush()

print("\n✅ Transaction sent successfully!")

producer.close()