from tools.validate_metadata.models.axe_amp_settings import AxeAmpSettings
from tools.validate_metadata.models.axe_device import AxeDevice
from tools.validate_metadata.models.model import Model


class AxeAmpModel(Model):
    device: AxeDevice = AxeDevice()
    settings: AxeAmpSettings = AxeAmpSettings()
    tonex_version: str = "UNKNOWN"
    notes: str = ""
