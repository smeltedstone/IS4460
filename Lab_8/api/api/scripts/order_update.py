import requests
import json

id = 1

api_url = f'http://localhost:8000/api/orders/{id}/'

order_data = {
    "customer": 1,
    "order_total": "399.99", 
    "notes": "Urgent delivery not requested.",
    "status": "pending" 
}

response = requests.put(api_url, data=json.dumps(order_data), headers={'Content-Type': 'application/json'})

if response.status_code == 200:
    print("Order updated successfully.")
else:
    print(f"Error updating the order.")