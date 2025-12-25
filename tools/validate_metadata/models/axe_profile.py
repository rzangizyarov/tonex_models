from typing import List

from pydantic import BaseModel

from tools.validate_metadata.models.axe_settings import AxeSettings
from tools.validate_metadata.models.axe_device import AxeDevice


class AxeProfile(BaseModel):
    profile_id: str = "UNKNOWN"
    device: AxeDevice = AxeDevice()
    settings: AxeSettings = AxeSettings()
    notes: str = ""
