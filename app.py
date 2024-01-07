from fastapi import FastAPI
from fastapi.responses import HTMLResponse, Request
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

# Mount the 'static' directory to serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def read_root():
    return "<h4>FastAPI Image List</h4>"

@app.get("/images/", response_class=HTMLResponse)
def read_images_list():
    image_list = get_image_list()
    html_content = "<h2>Image List:</h2><ul>"
    for image in image_list:
        html_content += f"<li>{image}</li>"
    html_content += "</ul>"
    return HTMLResponse(content=html_content, status_code=200)

def get_image_list():
    image_path = Path("static/images")
    image_list = [image.name for image in image_path.glob("*.jpg")]
    return image_list

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

