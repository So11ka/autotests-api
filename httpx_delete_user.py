import httpx
import tools.fakers as fakers

user_create_payload = {
    "email": fake.email(),
    "password": fakers.random_password(),
    "lastName": 'None',
    "firstName": fakers.random_name(),
    "middleName": fakers.random_surname(),
}

create_user_response = httpx.post('http://localhost:8000/api/v1/users', timeout=10, json=user_create_payload)

print(create_user_response.json())
print(create_user_response.status_code)

authentication_payload = {"email": user_create_payload['email'], "password": user_create_payload['password']}
authentication_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=authentication_payload)

print(authentication_response.json())
print(authentication_response.status_code)

header = authentication_response.json()['token']['accessToken']
client_id = create_user_response.json()['user']['id']
get_user_response = httpx.get(f'http://localhost:8000/api/v1/users/{client_id}', headers={'Authorization': f"Bearer {header}"})

print(get_user_response.json())
print(get_user_response.status_code)

delete_user_headers = {"Authorization": f"Bearer {authentication_response.json()['token']['accessToken']}"}
delete_user_response = httpx.delete(f"http://localhost:8000/api/v1/users/{client_id}",headers=delete_user_headers)

print(delete_user_response.json())
print(delete_user_response.status_code)