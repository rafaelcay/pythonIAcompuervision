from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time


endpoint= "inserta tu endpoint o extremo aqui"		#estos datos se encuentran en claves y punto de conexion
subscription_key= "inserta key o clave 1 o 2 aqui"

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

remote_image_url = input("Porfavor coloca el link de tu imagen a analizar :") 

print("===== Describe an image - remote =====")
# Call API
description_results = computervision_client.describe_image(remote_image_url )
print(description_results.as_dict()["captions"])
if len(description_results.as_dict()) > 0:
    print("Encontre lo siguiente: ")
    for elemento in description_results.as_dict()["captions"]:
        print("Descripcion: ", elemento["text"])
        print("Porcentaje de estar en lo correcto: ", elemento["confidence"]*100,"%")
else:
    print("No encontre nada.")


