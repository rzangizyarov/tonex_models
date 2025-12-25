from pydantic import BaseModel
import yaml
from pathlib import Path

from tools.validate_metadata.models.axe_profile import AxeProfile


def load_axe_profile(yaml_path: Path) -> BaseModel:
    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    if data is None:  # пустой файл
        data = {}
    profile = AxeProfile(**data)
    return profile


def save_profile(profile: BaseModel, yaml_path: Path):
    yaml_path.parent.mkdir(parents=True, exist_ok=True)
    with yaml_path.open("w", encoding="utf-8") as f:
        yaml.dump(profile.dict(), f, sort_keys=False, allow_unicode=True)


def update_profiles(root_dir: Path):
    for yaml_file in root_dir.rglob("*.yaml"):
        profile = load_axe_profile(yaml_file)

        # Перезаписываем YAML с недостающими атрибутами
        save_profile(profile, yaml_file)

        txp_file = yaml_file.with_suffix(".txp")
        if txp_file.exists():
            print(f"✅ {yaml_file} + {txp_file} OK (обновлено)")
        else:
            print(f"⚠ {yaml_file} VALID, но TXP не найден (обновлено)")


root_dir = Path("../../models/Axe FX II/Amp")
example_yaml = Path("../example.yaml")

# Валидация и автоматическое добавление недостающих атрибутов
update_profiles(root_dir)
