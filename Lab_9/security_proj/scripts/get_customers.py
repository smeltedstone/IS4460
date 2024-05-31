import requests

api_url = 'http://localhost:8000/api/customers/'

token = '2e206b0491ee2d320ff13aeebc0873c9a5784e95'

headers = {
    'Authorization': f'Token {token}'
}

response = requests.get(api_url,headers=headers)

print(response.status_code)

if response.status_code == 200:
    print(f"Customers retrieval successful. {response.text}")
else:
    print(f"Customers retrieval failed. {response.text}")