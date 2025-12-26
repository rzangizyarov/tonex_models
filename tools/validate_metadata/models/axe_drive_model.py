from tools.validate_metadata.models.axe_device import AxeDevice
from tools.validate_metadata.models.axe_drive_settings import AxeDriveSettings
from tools.validate_metadata.models.model import Model


class AxeDriveModel(Model):
    model_id: str = "UNKNOWN"
    device: AxeDevice = AxeDevice()
    settings: AxeDriveSettings = AxeDriveSettings()
    tonex_version: str = "UNKNOWN"
    notes: str = ""
