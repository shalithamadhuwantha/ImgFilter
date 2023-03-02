
from fastapi import FastAPI, File, UploadFile
from fastapi.encoders import jsonable_encoder
from fastapi.responses import StreamingResponse
import io
from PIL import Image, ImageFilter


app = FastAPI()

# Read the PIL document to find out which filters are available out-of the box
filters_available = [
    "blur",
    "contour",
    "detail",
    "edge_enhance",
    "edge_enhance_more",
    "emboss",
    "find_edges",
    "sharpen",
    "smooth",
    "smooth_more",
]


@app.api_route("/", methods=["GET", "POST"])
def index():
    """
    Return the usage instructions that specifies
    1. which filters are available, and
    2. the method format
    """
    response = {
        "filters_available": filters_available,
        "usage": {"http_method": "POST", "URL": "/<filter_available>/"},
    }
    return jsonable_encoder(response)


@app.post("/{filter}")
def image_filter(filter: str, img: UploadFile = File(...)):
    """
    TODO:
    1. Checks if the provided filter is available, if not, return an error
    2. Check if a file has been provided in the POST request, if not return an error
    3. Apply the filter using apply_filter() method from bin.filters
    4. Return the filtered image as response
    """
    if filter not in filters_available:
        response = {"error": "incorrect filter"}
        return jsonable_encoder(response)

    filtered_image = apply_filter(img.file, filter)

    return StreamingResponse(filtered_image, media_type="image/jpeg")

def apply_filter(file: object, filter: str) -> object:
    """
    TODO:
    1. Accept the image as file object, and the filter type as string
    2. Open the as an PIL Image object
    3. Apply the filter
    4. Convert the PIL Image object to file object
    5. Return the file object
    """
    image = Image.open(file)
    image = image.filter(eval(f"ImageFilter.{filter.upper()}"))

    file = io.BytesIO()
    image.save(file, "JPEG")
    file.seek(0)

    return file
