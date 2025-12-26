from pathlib import Path
from typing import Type

import yaml

from tools.validate_metadata.models.model import Model


class DeviceModelHandler:
    def __init__(self,
                 model_cls: Type[Model],
                 root_dir: Path):
        self.model_cls: Type[Model] = model_cls
        self.root_dir = root_dir

    @staticmethod
    def load_model(model_cls: Type[Model], yaml_path: Path) -> Model:
        data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
        if data is None:  # пустой файл
            data = {}
        model = model_cls(**data)
        return model

    @staticmethod
    def save_model(model: Model, yaml_path: Path):
        yaml_path.parent.mkdir(parents=True, exist_ok=True)
        with yaml_path.open("w", encoding="utf-8") as f:
            yaml.dump(model.model_dump(), f, sort_keys=False, allow_unicode=True)

    def update_models(self):
        for yaml_file in self.root_dir.rglob("*.yaml"):
            model = self.load_model(self.model_cls, yaml_file)

            # Перезаписываем YAML с недостающими атрибутами
            self.save_model(model, yaml_file)
            print(f"✅ {yaml_file} OK (обновлено)")
