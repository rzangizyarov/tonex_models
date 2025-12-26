from uuid import uuid4

from pydantic import BaseModel, Field

from tools.validate_metadata.models.device import Device
from tools.validate_metadata.models.settings import Settings


class Model(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    name: str = ""
    device: Device
    settings: Settings
    tonex_version: str
    notes: str
