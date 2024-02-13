import requests
import os
from PIL import Image

# from Ipython.display import IFrame

url = "https://www.ibm.com/"
r = requests.get(url)
print(r.status_code)
print(r.request.headers)
print("Request body = " + str(r.request.body))


# Request de uma imagem

url_img = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png"
r_img = requests.get(url_img)
path = os.path.join(os.getcwd(), "image.png")

with open(path, "wb") as f:
    f.write(r_img.content)
Image.open(path)