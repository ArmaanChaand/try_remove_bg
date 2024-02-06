import base64
import json
import requests
from django.conf import settings

function_url = settings.REMOVE_BG_API

def _remove(file_content):
    try:
        load_data = {
            'the_image': base64.b64encode(file_content.read()).decode('utf-8')
        }
        response = requests.post(function_url, json=json.dumps(load_data))
        if(response.status_code == 200):
            response_data = response.json()
            return response_data['the_image']
        else:
            print('REQUEST ERROR: ',  response.json())
            raise Exception('some error ocurred')
    except Exception as error:
        print("BG_REMOVE_ERROR:  ", error)
        raise error
