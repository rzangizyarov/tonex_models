from typing import Optional

from tools.validate_metadata.models.settings import Settings


class AxeDriveSettings(Settings):
    drive: Optional[float] = None
    tone: Optional[float] = None
    level: Optional[float] = None
