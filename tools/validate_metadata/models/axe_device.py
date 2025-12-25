from typing import Optional

from pydantic import BaseModel


class AxeDevice(BaseModel):
    platform: str = "Fractal Audio Axe FX II"
    model: Optional[str] = None
