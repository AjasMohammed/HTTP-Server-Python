import requests
import threading


def make_request():
    response = requests.post("http://127.0.0.1:4221/files/hello.txt", data="hello world")

    # Print request details
    print("Request URL:", response.request.url)
    print("Request Headers:", response.request.headers)
    print("Request Method:", response.request.method)

    # Print response details
    print("\nResponse Status Code:", response.status_code)
    if response.headers:
        print("Response Headers:", response.headers)
        print("Response Content Type:", response.headers.get("Content-Type"))
        print("Response Content Length:", response.headers.get("Content-Length"))

    # Print response content
    print("\nResponse Content:")
    print(response.content)

    print("-" * 50)


req_1 = threading.Thread(target=make_request)
# req_2 = threading.Thread(target=make_request)
# req_3 = threading.Thread(target=make_request)

req_1.start()
# req_2.start()
# req_3.start()
