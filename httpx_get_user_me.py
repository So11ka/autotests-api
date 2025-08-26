import httpx
import json

with httpx.Client(base_url='http://localhost:8000/api/v1', timeout=10.) as client:
    payload = {"email": "user34@example.com", "password": "qwer1234"}
    authentication_response = client.post('/authentication/login', json=payload)

    me_response = client.get('/users/me', headers={'Authorization': f"Bearer {authentication_response.json()['token']['accessToken']}"})
    print(f'Данные пользователя: {json.dumps(me_response.json(), indent=2)}')
    print(f'Статус-код ответа: {authentication_response.status_code}')

