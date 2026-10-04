import random


def inject_null_values(transaction, null_rate):

    if random.random() < null_rate:

        field = random.choice([
            "user_id",
            "product_id",
            "quantity",
            "amount",
            "payment_method"
        ])

        transaction[field] = None
        transaction["anomaly_type"] = "NULL_VALUE"

    return transaction