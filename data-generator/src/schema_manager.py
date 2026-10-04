import random


def inject_schema_change(transaction, schema_change_rate):

    if random.random() < schema_change_rate:

        change_type = random.choice([
            "ADD_FIELD",
            "RENAME_FIELD",
            "TYPE_CHANGE"
        ])

        if change_type == "ADD_FIELD":

            transaction["device_type"] = random.choice([
                "mobile",
                "desktop",
                "tablet"
            ])

        elif change_type == "RENAME_FIELD":

            transaction["customer_id"] = transaction.pop("user_id")

        elif change_type == "TYPE_CHANGE":

            transaction["quantity"] = str(transaction["quantity"])

        transaction["schema_version"] = "v2"

    else:

        transaction["schema_version"] = "v1"

    return transaction