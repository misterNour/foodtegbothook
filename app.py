# import hashlib
# import hmac
# import json
# import requests

# from flask import Flask, request, jsonify

# app = Flask(__name__)

# # Your Chargily Pay Secret key, will be used to calculate the Signature
# api_secret_key = 'test_sk_nu2KF22Dc60fD6LdkIoAwlp3WgfCj5rqn15atqeB'

# # URL of your Google Apps Script endpoint
# google_apps_script_url = 'https://script.google.com/macros/s/AKfycbwT_caEFY2AZJHpyzviLNm0KJVEGtK35qA7fVWecXq9hslWj-fDwTcGMYfG0vfICyF3/exec'


# @app.route('/webhook', methods=['POST'])
# def webhook():
#     # Extracting the 'signature' header from the HTTP request
#     signature = request.headers.get('signature')

#     # Getting the raw payload from the request body
#     payload = request.data.decode('utf-8')

#     # If there is no signature, ignore the request
#     if not signature:
#         return '', 400

#     # Calculate the signature
#     computed_signature = hmac.new(api_secret_key.encode('utf-8'), payload.encode('utf-8'), hashlib.sha256).hexdigest()

#     # If the calculated signature doesn't match the received signature, ignore the request
#     if not hmac.compare_digest(signature, computed_signature):
#         return '', 403

#     # If the signatures match, proceed to decode the JSON payload
#     event = json.loads(payload)

#     # Send event data to Google Apps Script
#     send_event_data_to_google_apps_script(event)

#     # Respond with a 200 OK status code to let us know that you've received the webhook
#     return '', 200

# def send_event_data_to_google_apps_script(event):
#     # Extract required data
#     event_id = event.get('id')
#     data_id = event.get('data', {}).get('id')

#     # Create data payload
#     payload = {
#         'id': event_id,
#         'data_id': data_id,
#         'status': 'paid'
#     }

#     # Make a POST request to Google Apps Script URL
#     response = requests.post(google_apps_script_url, json=payload)

#     if response.status_code == 200:
#         print('Event data sent to Google Apps Script successfully.')
#     else:
#         print('Failed to send event data to Google Apps Script. Status code:', response.status_code)

# if __name__ == '__main__':
#     app.run(debug=True)


from Flask import Flask, request
import requests

app = Flask(__name__)

# Replace with your Google Apps Script web app URL
GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbwT_caEFY2AZJHpyzviLNm0KJVEGtK35qA7fVWecXq9hslWj-fDwTcGMYfG0vfICyF3/exec"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json  # Assuming the incoming data is in JSON format
    
    # Send the data to Google Apps Script
    response = requests.post(GOOGLE_SCRIPT_URL, json=data)
    
    # Handle the response from the Google Apps Script if needed
    if response.status_code == 200:
        return "Data sent to Google Apps Script successfully"
    else:
        return "Failed to send data to Google Apps Script"

if __name__ == '__main__':
    app.run(debug=True)

