from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

'''
Authenticate
Authenticates your credentials and creates a client.
'''
subscription_key = "6622ef60-5f8d-419f-b647-d420ccdfe354"
endpoint = "https://ocr-leega-teste00010201.cognitiveservices.azure.com/" 

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key)) 

'''
OCR: Read File using the Read API, extract text - remote
This example will extract text in an image, then print results, line by line.
This API call can also extract handwriting style text (not shown).
'''
print("===== Read File - remote =====")
# Get an image with text
read_image_url = "https://github.com/BrunoSilvaSaba/ocr-azure/blob/main/VIVO_1638800597-899966869873.pdf"

# Call API with URL and raw response (allows you to get the operation location)
read_response = computervision_client.read(read_image_url,  raw=True)

