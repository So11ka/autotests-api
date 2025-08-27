import httpx
import tools.fakers as fakers


with httpx.Client(base_url='http://localhost:8000/api/v1', timeout=10) as client:
    user_create_payload = {
        "email": fakers.random_email(),
        "password": fakers.random_password(),
        "lastName": 'None',
        "firstName": fakers.random_name(),
        "middleName": fakers.random_surname(),
    }
    create_user_response = client.post('/users', json=user_create_payload)
    user_id = create_user_response.json()['user']['id']
    print(f'Было: {create_user_response.json()}')

    authentication_payload = {"email": user_create_payload['email'], "password": user_create_payload['password']}
    authentication_response = client.post('/authentication/login', json=authentication_payload)
    header_token = {'Authorization': f"Bearer {authentication_response.json()['token']['accessToken']}"}

    patch_user_payload = {
        "email": fakers.random_email(),
        "lastName": 'None',
        "firstName": user_create_payload['firstName'],
        "middleName": user_create_payload['middleName']
    }

    patch_user_response = client.patch(f'/users/{user_id}', headers=header_token, json=patch_user_payload)

    get_user_response = client.get(f'/users/{user_id}', headers=header_token)
    print(f'Стало: {get_user_response.json()}')