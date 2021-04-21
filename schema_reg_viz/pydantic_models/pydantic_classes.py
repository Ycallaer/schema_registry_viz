from pydantic import BaseModel
from typing import Optional


class VizTopicSubjectInput(BaseModel):
    subjectname: str
    persist: Optional[bool] = False
