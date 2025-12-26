from typing import Optional

from tools.validate_metadata.models.settings import Settings


class AxeAmpSettings(Settings):
    input_drive: Optional[float] = None
    overdrive: Optional[float] = None
    bass: Optional[float] = None
    mid: Optional[float] = None
    treble: Optional[float] = None
    bright: Optional[float] = None
    presence: Optional[float] = None
    depth: Optional[float] = None
    master_volume: Optional[float] = None
    input_trim: Optional[float] = None
    input_trim: Optional[bool] = None
    boost: Optional[bool] = None
    cut: Optional[bool] = None
    fat: Optional[bool] = None
    bright_switch: Optional[bool] = None
    bright_cap: Optional[float] = None
    saturation_switch: Optional[str] = None
    saturation_drive: Optional[float] = None
    master_volume_trim: Optional[float] = None
    level: Optional[float] = None
