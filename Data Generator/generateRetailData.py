import json
import random
import time
from datetime import datetime

products = ["Laptop", "Phone", "Headphones", "Tablet"]

def generate_event():
    return {
        "transaction_id": random.randint(1000, 9999),
        "product": random.choice(products),
        "price": round(random.uniform(50, 2000), 2),
        "timestamp": str(datetime.utcnow())
    }

while True:
    event = generate_event()
    print(json.dumps(event))
    time.sleep(1)
