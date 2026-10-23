from pydantic import BaseModel, Field, field_validator

class Note (BaseModel):
    id: str 
    text: str

class NoteText (BaseModel):
    text: str = Field(..., min_length=1, max_length=500)

    @field_validator('text')
    @classmethod
    def text_must_not_be_empty(cls, value: str) -> str:
        if not value.strip():
            raise ValueError('Text nesmí být prázdný nebo obsahovat pouze mezery.')
        return value

class NoteCreate (NoteText):
    pass

class NoteResponse (BaseModel):
    id:str
    text: str

class NoteUpdate (NoteText):
    pass