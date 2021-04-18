import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from starlette.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from schema_reg_viz.config.settings import get_settings
from schema_reg_viz.pydantic_models.pydantic_classes import VizTopicSubjectInput
from schema_reg_viz.graph.graph_vizualiser import viz_sr_topic


def get_app() -> FastAPI:
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

schema_registry_base_url = "http://{}:{}".format(get_settings().schema_registry.url, get_settings().schema_registry.port)


@app.get("/health")
async def health():
    return {"app_name": "schema registry viz", "app_version": "1.0.0", "app_type": "Fastapi"}


@app.post("/viz_topic", response_class=JSONResponse)
async def viz_topic(viz_subject_name: VizTopicSubjectInput):
    print("hi")
    result = viz_sr_topic(subject_name=viz_subject_name,sr_base_url=schema_registry_base_url)
    return result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8888)