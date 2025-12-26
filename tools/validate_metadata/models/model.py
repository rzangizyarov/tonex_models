from pydantic import BaseModel

from tools.validate_metadata.models.device import Device
from tools.validate_metadata.models.settings import Settings


class Model(BaseModel):
    model_id: str
    device: Device
    settings: Settings
    tonex_version: str
    notes: str
