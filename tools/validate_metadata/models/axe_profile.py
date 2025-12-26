from pydantic import BaseModel

from tools.validate_metadata.models.axe_amp_settings import AxeAmpSettings
from tools.validate_metadata.models.axe_device import AxeDevice


class AxeAmpProfile(BaseModel):
    profile_id: str = "UNKNOWN"
    device: AxeDevice = AxeDevice()
    settings: AxeAmpSettings = AxeAmpSettings()
    notes: str = ""
