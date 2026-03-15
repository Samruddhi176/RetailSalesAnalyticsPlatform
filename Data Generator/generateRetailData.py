import json
import random
import uuid
from datetime import datetime
import time

products = ["Laptop", "Phone", "Headphones", "Shoes", "Watch"]
stores = ["STORE_1", "STORE_2", "STORE_3", "STORE_4"]

def generate_transaction():
    return {
        "transaction_id": str(uuid.uuid4()),
        "store_id": random.choice(stores),
        "product": random.choice(products),
        "quantity": random.randint(1, 5),
        "price": round(random.uniform(10, 500), 2),
        "timestamp": datetime.utcnow().isoformat()
    }

while True:
    transaction = generate_transaction()
    print(json.dumps(transaction))
    time.sleep(1)
