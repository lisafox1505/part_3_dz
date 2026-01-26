import requests


def http_client(url, method, data=None):
    try:
        if method.upper() == "GET":
            response = requests.request(method, url, params=data)
        else:
            response = requests.request(method, url, json=data)

        print(f"Status Code: {response.status_code}")

        print("\n\tHeaders\t")
        for key, value in response.headers.items():
            print(f"{key}: {value}")

        print("\n\tBody\t")
        print(response.text)
        print("-" * 30)

    except requests.exceptions.RequestException as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    http_client(
        url="https://httpbin.org/get",
        method="GET",
        data={"name": "Kira", "age": 23}
    )

    http_client(
        url="https://httpbin.org/post",
        method="POST",
        data={"login": "admin", "password": "123"}
    )
