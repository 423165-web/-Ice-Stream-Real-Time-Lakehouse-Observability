import random
import uuid
from datetime import datetime, timezone


def generate_transaction():
    return {
        "transaction_id": str(uuid.uuid4()),
        "user_id": f"user_{random.randint(1, 100000)}",
        "product_id": f"product_{random.randint(1, 10000)}",
        "quantity": random.randint(1, 5),
        "amount": round(random.uniform(100, 5000), 2),
        "currency": "INR",
        "payment_method": random.choice([
            "upi",
            "card",
            "net_banking",
            "wallet"
        ]),
        "event_time": datetime.now(timezone.utc).isoformat()
    }