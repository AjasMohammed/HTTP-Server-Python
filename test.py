import requests
import threading


def make_request():
    response = requests.get("http://127.0.0.1:4221/")

    # Print request details
    print("Request URL:", response.request.url)
    print("Request Headers:", response.request.headers)
    print("Request Method:", response.request.method)

    # Print response details
    print("\nResponse Status Code:", response.status_code)
    print("Response Headers:", response.headers)
    print("Response Content Type:", response.headers["Content-Type"])

    # Print response content
    print("\nResponse Content:")
    print(response.content)

    print('-'*50)

req_1 = threading.Thread(target=make_request)
req_2 = threading.Thread(target=make_request)
req_3 = threading.Thread(target=make_request)

req_1.start()
req_2.start()
req_3.start()