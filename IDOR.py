import requests

url_base = "://ec2310-16161ap-south1.compute.amazonaws./api/get-customer?id=1"

for i in range(1, 5001):
    
    url = url_base + str(i)
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Requested URL: {url}")