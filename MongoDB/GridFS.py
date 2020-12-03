# importaciones
import base64
from pymongo import MongoClient
import gridfs

from io import BytesIO
import numpy as np
import matplotlib.pyplot as plt

import cv2
from PIL import Image

# Conexion
client = MongoClient('localhost', 27017)
database = client.image
img = r'D:\Imágenes\Saved Pictures\AnyWall\Microsoft_WindowsInsider.PNG'
fid = ""

# Lectura
with open(img, "rb") as image_file:
	encoded_string = base64.b64encode(image_file.read())

# Carga de la imagen
filename = "test"
fs = gridfs.GridFS(database)
fileid = fs.put(encoded_string, filename=filename)
database.image.insert_one({"filename":filename,"fileid":fileid})

# Consulta
for item in database.image.find({"filename":filename}):
	print(item)
	fid = item["fileid"]

if fid != "":
	output = fs.get(fid).read()
	print(output)










# Construccion de la imagen
# file = fs.find_one({"filename":filename})
# bytedata = file.read()

# # Pillow
# # ima_IO = BytesIO(base64.b64decode(bytedata))
# # img_PIL = Image.open(ima_IO)
# # img_PIL.show()

# # CV2
# data = np.frombuffer(base64.b64decode(bytedata), np.uint8)
# img_CV2 = cv2.imdecode(data, 3)
# img_CV2 = cv2.cvtColor(img_CV2, cv2.COLOR_BGR2RGB)
# plt.imshow(img_CV2)
# plt.show()

# client.close()