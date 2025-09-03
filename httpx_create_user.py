import httpx
from tools.fakers import fake
payload = {
    "email": fake.email(),
    "password": fake.password(),
    "lastName": fake.last_name(),
    "firstName": fake.first_name(),
    "middleName": fake.middle_name(),
}

user_response = httpx.post('http://localhost:8000/api/v1/users', timeout=10, json=payload)

print(user_response.json())
print(user_response.status_code)