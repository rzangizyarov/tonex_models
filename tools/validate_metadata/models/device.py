from typing import Optional

from pydantic import BaseModel


class Device(BaseModel):
    platform: str
    model: Optional[str]
