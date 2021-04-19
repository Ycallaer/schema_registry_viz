from pydantic import BaseModel


class VizTopicSubjectInput(BaseModel):
    subjectname: str
