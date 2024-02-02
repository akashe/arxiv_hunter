from pydantic import BaseModel, HttpUrl

class Paper(BaseModel):
    id: str
    title: str
    pdf_link: HttpUrl

class PaperSearch(BaseModel):
    query: str = "LLAMA, Mamba"
    days: int = 60

class PaperRecommend(BaseModel):
    paper_id: str
