from pathlib import Path

from tools.validate_metadata.device_profile_handler import DeviceProfileHandler
from tools.validate_metadata.models.axe_profile import AxeAmpProfile

# Валидация и автоматическое добавление недостающих атрибутов
axe_profile_handler = DeviceProfileHandler(device_profile=AxeAmpProfile, root_dir=Path("../../models/Axe FX II/Amp"))
axe_profile_handler.update_profiles()
