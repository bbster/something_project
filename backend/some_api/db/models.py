from pydantic import BaseModel


class Resolution(BaseModel):
    email = str
    message = str
