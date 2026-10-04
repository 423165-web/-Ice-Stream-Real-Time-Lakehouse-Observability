"""Configuration for the transaction data generator."""

import os

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "transactions")

__all__ = ["KAFKA_BOOTSTRAP_SERVERS", "KAFKA_TOPIC"]
