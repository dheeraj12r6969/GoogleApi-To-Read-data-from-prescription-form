# import os, io
# from google.cloud import vision
# from google.cloud.vision import types
#
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'AllSpark-e020170b81b4.json'
#
# client = vision.ImageAnnotatorClient()
#
# file_name = "report1.jpg"
# folder_path = r'C:\Users\Dheeraj\PycharmProjects\All'
#
# with io.open(os.path.join(folder_path,file_name), 'rb') as image_file:
#     content = image_file.read()
#
# image = vision.types.Image(content=content)
#
# response = client.text_detection(image=image)


import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'AllSpark-e020170b81b4.json'

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    'report1.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
    print(label.description)

