from pydantic import BaseModel

class Content(BaseModel):
    before : str | None = None
    tab : list[list[str]] | None = None 
    after : str | None = None
