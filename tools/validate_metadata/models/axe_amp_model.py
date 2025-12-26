from tools.validate_metadata.models.axe_amp_settings import AxeAmpSettings
from tools.validate_metadata.models.axe_device import AxeDevice
from tools.validate_metadata.models.model import Model


class AxeAmpModel(Model):
    profile_id: str = "UNKNOWN"
    device: AxeDevice = AxeDevice()
    settings: AxeAmpSettings = AxeAmpSettings()
    notes: str = ""
