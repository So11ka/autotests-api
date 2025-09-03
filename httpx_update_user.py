import httpx
from tools.fakers import fake
with httpx.Client(base_url='http://localhost:8000/api/v1', timeout=10) as client:

    user_create_payload = {
        "email": fake.email(),
        "password": fake.password(),
        "lastName": fake.last_name(),
        "firstName": fake.first_name(),
        "middleName": fake.middle_name(),
    }
    create_user_response = client.post('/users', json=user_create_payload)
    user_id = create_user_response.json()['user']['id']
    print(f'Было: {create_user_response.json()}')

    authentication_payload = {"email": user_create_payload['email'], "password": user_create_payload['password']}
    authentication_response = client.post('/authentication/login', json=authentication_payload)
    header_token = {'Authorization': f"Bearer {authentication_response.json()['token']['accessToken']}"}

    patch_user_payload = {
        "email": fake.email(),
        "lastName": 'None',
        "firstName": user_create_payload['firstName'],
        "middleName": user_create_payload['middleName']
    }

    patch_user_response = client.patch(f'/users/{user_id}', headers=header_token, json=patch_user_payload)
    print(f'Стало: {patch_user_response.json()}')