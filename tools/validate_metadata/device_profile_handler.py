from pathlib import Path
from typing import Type

import yaml
from pydantic import BaseModel

from tools.validate_metadata.models.profile import Profile


class DeviceProfileHandler:
    def __init__(self,
                 device_profile: Type[Profile],
                 root_dir: Path):
        self.device_profile: Profile = device_profile
        self.root_dir = root_dir

    @staticmethod
    def load_model(base_model: BaseModel, yaml_path: Path) -> BaseModel:
        data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
        if data is None:  # пустой файл
            data = {}
        model = base_model(**data)
        return model

    @staticmethod
    def save_profile(base_model: BaseModel, yaml_path: Path):
        yaml_path.parent.mkdir(parents=True, exist_ok=True)
        with yaml_path.open("w", encoding="utf-8") as f:
            yaml.dump(base_model.model_dump(), f, sort_keys=False, allow_unicode=True)

    def update_profiles(self):
        for yaml_file in self.root_dir.rglob("*.yaml"):
            profile = self.load_model(self.device_profile, yaml_file)

            # Перезаписываем YAML с недостающими атрибутами
            self.save_profile(profile, yaml_file)

            txp_file = yaml_file.with_suffix(".txp")
            if txp_file.exists():
                print(f"✅ {yaml_file} + {txp_file} OK (обновлено)")
            else:
                print(f"⚠ {yaml_file} VALID, но TXP не найден (обновлено)")
