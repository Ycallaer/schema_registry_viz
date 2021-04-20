import uvicorn
from fastapi import FastAPI, Request

from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from starlette.responses import JSONResponse, FileResponse, HTMLResponse
from starlette.middleware.cors import CORSMiddleware

from schema_reg_viz.config.settings import get_settings
from schema_reg_viz.pydantic_models.pydantic_classes import VizTopicSubjectInput
from schema_reg_viz.graph.graph_vizualiser import viz_sr_topic
from schema_reg_viz.json_logging.json_logger import JsonLogging

logapp = JsonLogging()
logger = logapp.get_logger()


def get_app() -> FastAPI:
    """
    Function to load the application configuration
    :return:
    """
    app_settings = get_settings()
    server = FastAPI()
    return server


app = get_app()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

schema_registry_base_url = "{}://{}:{}".format(get_settings().schema_registry.protocol,
                                               get_settings().schema_registry.url, get_settings().schema_registry.port)
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/health")
async def health():
    return {"app_name": "schema registry viz", "app_version": "1.0.0", "app_type": "Fastapi"}


@app.post("/viz_topic", response_class=JSONResponse)
async def viz_topic(viz_subject_name: VizTopicSubjectInput):
    logger.info("Requesting visualisation for subject {}".format(viz_subject_name.subjectname),
                extra={"severity": "info"})
    result = viz_sr_topic(subject_name=viz_subject_name, sr_base_url=schema_registry_base_url)
    return result


@app.get("/show/{graph_id}", response_class=HTMLResponse)
async def viz_d3(request: Request, graph_id: str):
    return templates.TemplateResponse("graphd3.html", {"request": request, "graph_id": graph_id})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)
