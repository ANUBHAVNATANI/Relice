import requests

#Some variables
subscription_key = "674d6648b56249649069b64cc83ed9a2"
face_api_url = 'https://relice.cognitiveservices.azure.com/face/v1.0/detect'
face_api_url_verify = 'https://relice.cognitiveservices.azure.com/face/v1.0/verify'
headers = {'Ocp-Apim-Subscription-Key': subscription_key}

def get_face_id(image_url):
    """
    This function take the face id of the preson from the image url
    Args:
        image_url: image_url from the blob storage of the person
    Returns:
        face_id : Azure generated face id
    """
    params = {
        'returnFaceId': 'true'
    }
    response = requests.post(face_api_url, params=params,
                         headers=headers, json={"url": image_url})
    faceId = response.json()[0]['faceId']
    return faceId


def face_compare(id_1, id_2):
    """ Determine if two faceIDs are for the same person   
    Args:
        id_1: faceID for person 1
        id_2: faceID for person 2
        
    Returns:
        json response: Full json data returned from the API call
        
    """
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': subscription_key
    }

    body = {"faceId1": id_1, "faceId2": id_2}

    params = {}
    response = requests.post(face_api_url_verify,
                             params=params,
                             headers=headers,
                             json=body)
    return response.json()

