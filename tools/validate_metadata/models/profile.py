from pydantic import BaseModel

from tools.validate_metadata.models.device import Device
from tools.validate_metadata.models.settings import Settings


class Profile(BaseModel):
    profile_id: str
    device: Device
    settings: Settings
    notes: str
