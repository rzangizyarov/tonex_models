from typing import Optional

from tools.validate_metadata.models.device import Device


class AxeDevice(Device):
    platform: str = "Fractal Audio Axe FX II"
    model: Optional[str] = None
