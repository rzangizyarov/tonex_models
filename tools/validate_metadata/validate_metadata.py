from pathlib import Path

from tools.validate_metadata.model_handler import ModelHandler
from tools.validate_metadata.models.axe_amp_model import AxeAmpModel
from tools.validate_metadata.models.axe_drive_model import AxeDriveModel
from tools.validate_metadata.models.impulse_response import ImpulseResponse

# Валидация и автоматическое добавление недостающих атрибутов
axe_amp_model_handler = ModelHandler(model_cls=AxeAmpModel, root_dir=Path("../../models/Axe FX II/Amp"))
axe_amp_model_handler.update_models()

axe_drive_model_handler = ModelHandler(model_cls=AxeDriveModel, root_dir=Path("../../models/Axe FX II/Drive"))
axe_drive_model_handler.update_models()

ir_handler = ModelHandler(model_cls=ImpulseResponse, root_dir=Path("../../models/IR"))
ir_handler.update_models()