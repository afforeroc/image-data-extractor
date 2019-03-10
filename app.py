# Libraries
from watson_developer_cloud import CompareComplyV1, WatsonApiException
from os.path import abspath
import json

# SDK init
compareAndComply = CompareComplyV1(
    version='2018-10-15',
    iam_apikey='jxO4d55gzPyREYxBhkBdbKPQ-5LRm-StocqJ1XovEXmV',
    url='https://gateway.watsonplatform.net/compare-comply/api'
)
compareAndComply.set_detailed_response(False)

# Open image from resources' path
input_path = abspath('resources/imagen.jpg')
input_file = open(input_path, 'rb')
data = input_file.read()

# API Request
response = compareAndComply.classify_elements(data, model_id='contract', file_content_type='image/jpeg', filename='imagen.jpg')

# Print response with nice json format
#print(json.dumps(response, indent=2, sort_keys=True))

# Response to json data
json_data = json.loads(json.dumps(response, ensure_ascii=False))
    
# Extract elements section from 
siz = len(json_data['elements'])
elements = json_data['elements']

# Obtain text
text = ''
for i in range(siz):
    text += elements[i]['text']+'\n'
print(text)

# Save text to txt file
outputfile = open("resources/output.txt", "w+")
outputfile.write(text)
outputfile.close()