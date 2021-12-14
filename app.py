from logging import debug
from flask import Flask, render_template,request,redirect
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
api = IAMAuthenticator("TiItDCMool9G0BFGmU84BhX0hzeraUNqSJWqKe94OQuN")
speech_2_text = SpeechToTextV1(authenticator=api)
speech_2_text.set_service_url("https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/c984422c-f03a-47b4-8c12-79a6925f10e6")

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])

def index():
    transcript=""
    if request.method=="POST":
        print("Form data recieved")

    print(request.headers,request.method)

    # if "file" not in request.files:
    #     return redirect(request.url)

    try:
        file=request.files["file"]
        result = speech_2_text.recognize(
        audio=file).get_result()
        print(result)
        transcript=(result.get('results')[0].get('alternatives')[0].get('transcript'))
        

    except:
        pass
    

    return render_template('index.html', transcript=transcript)

if __name__=="__main__":
    app.run(debug=True, threaded=True)

