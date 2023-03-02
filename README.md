# IMAGE FILTER API <sup>(fast api base)</sup>
<img src="https://img.shields.io/badge/PYTHON-3.11-blue"> <img src="https://img.shields.io/badge/V-1.0.0-yellow"> <img src="https://img.shields.io/badge/license-GPL--3.0%20license-red">  <img src="https://img.shields.io/badge/FASTAPI-orange"> <br>

## # Start up 🐱‍🏍
#### install requirement 
```commandline
pip install -r requirements.txt
```

## # Usage 🚀
#### run  server
```commandline
$ uvicorn main:app --reload
```

#### code example 
```commandline
file = {"image":open("sample.jpg","rb")}
header = {"type":"multypart/image"}
url = "http://127.0.0.1:5000"
filter = "blur"
respo = requests.post("{}/{}".format(url,filter),headers=header, files=file)
respo.raise_for_status

from PIL import Image
import io
image = Image.open(io.BytesIO(respo.content))
image.save("respo1253.jpg","JPEG")
image
```

 insert filter name to 'filter' variable
## # Available filter 📸

### 📷 Blur
<img src="img/blur.jpeg">

<hr >

### 📷 Contour
<img src="img/Contour.jpeg">

<hr >

### 📷 Detail
<img src="img/detail.jpeg">

<hr >

### 📷 Edge_enhance
<img src="img/edge_enhance.jpeg">

<hr >

### 📷 Edge_enhance_more
<img src="img/edge_enhance_more.jpeg">

<hr >

### 📷 Emboss
<img src="img/emboss.jpeg">

<hr >

### 📷 find_edges
<img src="img/find_edges.jpeg">

<hr >

### 📷 Sharpen
<img src="img/sharpen.jpeg">

<hr >

### 📷 smooth
<img src="img/smooth.jpeg">

<hr >

### 📷 smooth_more
<img src="img/smooth_more.jpeg">

<hr >
