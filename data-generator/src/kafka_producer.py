import json
from kafka import KafkaProducer


class TransactionProducer:

    def __init__(self, broker, topic):

        self.topic = topic

        self.producer = KafkaProducer(
            bootstrap_servers=[broker],
            value_serializer=lambda data:
                json.dumps(data).encode("utf-8"),

            # Performance settings
            acks=1,
            linger_ms=5,
            batch_size=32768,
            compression_type="gzip"
        )

    def send(self, transaction):

        self.producer.send(
            self.topic,
            value=transaction
        )

    def flush(self):

        self.producer.flush()

    def close(self):

        self.producer.close()