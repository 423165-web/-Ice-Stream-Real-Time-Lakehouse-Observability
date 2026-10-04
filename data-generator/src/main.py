import os
import time

from dotenv import load_dotenv
from src.transaction_generator import generate_transaction
from src.anomaly_injector import inject_null_values
from src.schema_manager import inject_schema_change
from src.kafka_producer import TransactionProducer


load_dotenv()


BROKER = os.getenv(
    "KAFKA_BOOTSTRAP_SERVERS",
    "localhost:9092"
)

TOPIC = os.getenv(
    "KAFKA_TOPIC",
    "transactions"
)

RATE = int(
    os.getenv(
        "EVENTS_PER_SECOND",
        "1000"
    )
)

NULL_RATE = float(
    os.getenv(
        "NULL_RATE",
        "0.02"
    )
)

SCHEMA_RATE = float(
    os.getenv(
        "SCHEMA_CHANGE_RATE",
        "0.01"
    )
)


def main():

    print("=" * 60)
    print("ICE STREAM - TRANSACTION GENERATOR")
    print("=" * 60)

    print(f"Kafka Broker      : {BROKER}")
    print(f"Kafka Topic       : {TOPIC}")
    print(f"Target Rate       : {RATE} events/sec")
    print(f"NULL Rate         : {NULL_RATE * 100}%")
    print(f"Schema Change Rate: {SCHEMA_RATE * 100}%")
    print("=" * 60)

    producer = TransactionProducer(
        BROKER,
        TOPIC
    )

    total_events = 0

    try:

        while True:

            start = time.perf_counter()

            for _ in range(RATE):

                transaction = generate_transaction()

                transaction = inject_null_values(
                    transaction,
                    NULL_RATE
                )

                transaction = inject_schema_change(
                    transaction,
                    SCHEMA_RATE
                )

                producer.send(transaction)

                total_events += 1

            producer.flush()

            elapsed = time.perf_counter() - start

            if elapsed < 1:
                time.sleep(1 - elapsed)

            actual_rate = RATE / max(elapsed, 1)

            print(
                f"Events: {total_events:,} | "
                f"Rate: {actual_rate:,.0f} events/sec"
            )

    except KeyboardInterrupt:

        print("\nStopping generator...")

    finally:

        producer.close()
        print("Generator stopped.")


if __name__ == "__main__":
    main()