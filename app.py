# LNMHacks 4.0
# Anubhav Natani

from flask import Flask, request, jsonify,render_template
import os
import traceback
#My library
from utils import get_face_image,get_embeddings,calc_dist,get_match_score
from azure_utils import get_face_id,face_compare

# API definition
app = Flask(__name__)

# Webpage to be made for this route
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/checkImagesV1",methods=["GET"])
def checkImages():
    try:
        databaseName = request.args.get('databaseName')
        imageId = request.args.get('imageId')
        #selecting important information from the user request
        
        #Accuring the database images based on the request
        #img1
        #img2 or vector2
        face1 = get_face_image(img1)
        face2 = get_face_image(img2)
        #can be skipped by the inclusion of the vectors time saved - 1s
        vector1 = get_embeddings(face1)
        vector2 = get_embeddings(face2)
        #getting the distance (distance measure can be changed)
        distOfImages = calc_dist(vector1,vector2)
        #getting the match score of the image
        score = get_match_score(distOfImages)
        #passing this as a api response to the client
        return jsonify({"Score":score})
    except:
        return jsonify({'trace': traceback.format_exc()})


@app.route("/checkImagesV2",methods=["GET","POST"])
def checkImages():
    try:
        #Api of checking for the android cliet
        faceId = request.args.get('faceId')
        #can be skipped by the inclusion of the vectors time saved - 1s
        a = []
        #take face ids from the original database
        #results array
        score = []
        boolArr = []
        for i in a:
            v = face_compare(i,faceId)
            score.append(v['confidence'])
            boolArr.append(v['isIdentical'])
        extract_max = score.index(max(score))
        if(boolArr[extract_max]==True):
            #call database route to store the array
            pass
        else:
            #else do not call the database route
            pass
        #passing this as a api response to the client
        return jsonify({"Feedback":"ThankYou"})
    except:
        return jsonify({"Feedback": "Error"})

@app.route("/getId",methods=["GET","POST"])
def getId():
    try:
        dbItemId = request.args.get('dbItemId')
        #generating the face id
        faceId = get_face_id(dbItemId)
        #get the temp database images using the database route
        a = []
        #results array
        score = []
        boolArr = []
        for i in a:
            v = face_compare(i,faceId)
            score.append(v['confidence'])
            boolArr.append(v['isIdentical'])
        extract_max = score.index(max(score))
        if(boolArr[extract_max]==True):
            #call database route to store the array
            return jsonify({"face_id":faceId,"matched_id":a[extract_max]})
        else:
            #else do not call the database route
            return jsonify({"face_id":faceId,"matched_id":""})
    except:
        return jsonify({'Feedback': "error"})


#App running code
if __name__ == '__main__':
    app.run(debug=False)
    


