from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
# Set up templates folder (same as Flask's 'templates')
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    # Pass 'request' to the template (required by FastAPI)
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info")