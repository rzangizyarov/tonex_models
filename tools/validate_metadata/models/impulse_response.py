from pydantic import BaseModel


class ImpulseResponse(BaseModel):
    model_id: str = "UNKNOWN"
    source: str = ""
    notes: str = ""
