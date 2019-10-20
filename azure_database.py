import requests
import json

def get_database(name):
    """
    This function returns the database faceId 
    Returns:
        array of the face ids
    """
    if(name=="temp"):
        url = "https://reliceapi.azurewebsites.net/api/get/reports"
    else:
        url = "https://reliceapi.azurewebsites.net/api/get/complaints"
    r = requests.get(url=url)
    data = r.json()
    arr = [data[i]['face_id'] for i in range(len(data))]
    if(name == "temp"):
        return arr
    else:
        name = [data[i]['victim_name'] for i in range(len(data))]
    return [arr,name]

def post_matched_images(face_id1,face_id2,victim_name):
    """
    This function post two images to the database which are matched
    Args:
        face_id : face_id of the person
    Returns:
        post_resp : this says if it was succesfull in posting the images
    """
    url = "https://reliceapi.azurewebsites.net/api/post/matched"
    data = {
        "complaint_id":face_id1,
        "report_id":face_id2,
        "victim_name":victim_name
    }
    r = requests.post(url = url, data = data)
    return r 
