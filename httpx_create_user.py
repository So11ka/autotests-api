import httpx
import tools.fakers as faker

payload = {
    "email": faker.random_email(),
    "password": faker.random_password(),
    "lastName": 'None',
    "firstName": faker.random_name(),
    "middleName": faker.random_surname(),
}

user_response = httpx.post('http://localhost:8000/api/v1/users', timeout=10, json=payload)

print(user_response.json())
print(user_response.status_code)