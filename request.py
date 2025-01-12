
# make a post request to this endpoint to get the current score

import requests

url = 'http://localhost:5000/update_posture'

data = {
    'posture': 35
}

response = requests.post(url, json=data)

print(response.json())