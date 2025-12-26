from pathlib import Path

from tools.validate_metadata.device_profile_handler import DeviceModelHandler
from tools.validate_metadata.models.axe_amp_model import AxeAmpModel

# Валидация и автоматическое добавление недостающих атрибутов
axe_profile_handler = DeviceModelHandler(model_cls=AxeAmpModel, root_dir=Path("../../models/Axe FX II/Amp"))
axe_profile_handler.update_models()
