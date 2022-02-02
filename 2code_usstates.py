from flask import *
import json
import us
app = Flask(__name__)
@app.route('/', methods=['GET'])
def home_page():
  dataset =  {'Page': 'Home Page', 'Message': 'Welcome to home page'}
  json_dump = json.dumps(dataset)
  return json_dump
if __name__ == '__main__':
   app.run(port=7777)
@app.route('/state/', methods=['GET'])
def request_state():
  user_query = str(request.args.get('state')) #example /state/?state=OH
  result = {'Message': user_query}
  print(result)
if __name__ == '__main__':
   app.run(host='0.0.0.0', port=7777)