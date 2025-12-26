from pathlib import Path

from tools.validate_metadata.model_handler import ModelHandler
from tools.validate_metadata.models.axe_amp_model import AxeAmpModel

# Валидация и автоматическое добавление недостающих атрибутов
axe_amp_model_handler = ModelHandler(model_cls=AxeAmpModel, root_dir=Path("../../models/Axe FX II/Amp"))
axe_amp_model_handler.update_models()
