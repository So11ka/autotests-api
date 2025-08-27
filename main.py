import httpx

payload = {"email": "user34@example.com", "password": "qwer1234"}

response1 = httpx.post('http://localhost:8000/api/v1/authentication/login', json=payload, timeout=10)
response2 = httpx.post('http://localhost:8000/api/v1/authentication/refresh', json={'refreshToken': response1.json()['token']['refreshToken']}, timeout=10)
print(response2.json())
