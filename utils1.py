import json
import os
from datetime import datetime

DATA_FILE = 'data1.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_item(item, qty, user):
    data = load_data()
    item = item.lower()
    if item not in data:
        data[item] = {"quantity": qty, "log": []}
    else:
        return "Item already exists. Use /updateitem."

    data[item]["log"].append({"time": str(datetime.now()), "change": qty, "by": user})
    save_data(data)
    return f"Added {item} with quantity {qty}."

def update_item(item, qty, user):
    data = load_data()
    item = item.lower()
    if item not in data:
        return "Item not found. Use /additem first."

    data[item]["quantity"] += qty
    data[item]["log"].append({"time": str(datetime.now()), "change": qty, "by": user})
    save_data(data)
    return f"Updated {item} to {data[item]['quantity']}."

def check_stock(item):
    data = load_data()
    item = item.lower()
    if item not in data:
        return "Item not found."
    return f"{item}: {data[item]['quantity']} units"

def stock_summary():
    data = load_data()
    if not data:
        return "Inventory is empty."
    return "\n".join([f"{k}: {v['quantity']} units" for k, v in data.items()])

def get_log(item):
    data = load_data()
    item = item.lower()
    if item not in data:
        return "Item not found."
    logs = data[item]['log'][-5:]
    return "\n".join([f"{x['time']} | {x['change']} by {x['by']}" for x in logs])
