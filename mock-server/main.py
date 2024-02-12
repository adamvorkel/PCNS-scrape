import os
from typing import Annotated
import asyncio
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

load_dotenv()

app = FastAPI()

templates = Jinja2Templates(directory="templates")

delay = float(os.getenv('RES_LATENCY', 2))

@app.get("/health")
async def get_html():
    return {'ok': True}

# hits for even ids, misses for odd 
@app.post("/", response_class=HTMLResponse)
async def get_html(request: Request, SearchValue: Annotated[int, Form()]):
    await asyncio.sleep(delay)
    if SearchValue % 2 == 0:
        return templates.TemplateResponse(name="data.html", request=request, context={"id": SearchValue})
    else:
        return templates.TemplateResponse(name="nodata.html", request=request, context={"id": SearchValue})


@app.post("/hit", response_class=HTMLResponse)
async def get_html(request: Request, SearchValue: Annotated[int, Form()]):
    await asyncio.sleep(delay)
    return templates.TemplateResponse(name="data.html", request=request, context={"id": SearchValue})

@app.post("/miss", response_class=HTMLResponse)
async def get_html(request: Request, SearchValue: Annotated[int, Form()]):
    await asyncio.sleep(delay)
    return templates.TemplateResponse(name="nodata.html", request=request, context={"id": SearchValue})