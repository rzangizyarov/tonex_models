from pydantic import BaseModel


class ImpulseResponse(BaseModel):
    id: str = "UNKNOWN"
    name: str = ""
    source: str = ""
    notes: str = ""
