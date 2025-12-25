from pydantic import BaseModel
from typing import List, Optional
import yaml
from pathlib import Path

class Device(BaseModel):
    platform: Optional[str] = None
    type: Optional[str] = None
    model: Optional[str] = None

class Settings(BaseModel):
    input_drive: float = 0.0
    bass: float = 0.0
    mid: float = 0.0
    treble: float = 0.0
    presence: float = 0.0
    depth: float = 0.0
    gain: float = 0.0

class Profile(BaseModel):
    profile_id: str = "UNKNOWN"
    device: Device = Device()
    settings: Settings = Settings()
    tags: List[str] = []
    notes: str = ""

# ----------------------------
# Функции
# ----------------------------
def load_profile(yaml_path: Path) -> Profile:
    data = yaml.safe_load(yaml_path.read_text(encoding="utf-8"))
    if data is None:  # пустой файл
        data = {}
    profile = Profile(**data)
    return profile

def save_profile(profile: Profile, yaml_path: Path):
    yaml_path.parent.mkdir(parents=True, exist_ok=True)
    with yaml_path.open("w", encoding="utf-8") as f:
        yaml.dump(profile.dict(), f, sort_keys=False, allow_unicode=True)

def update_profiles(root_dir: Path):
    for yaml_file in root_dir.rglob("*.yaml"):
        profile = load_profile(yaml_file)

        # Перезаписываем YAML с недостающими атрибутами
        save_profile(profile, yaml_file)

        txp_file = yaml_file.with_suffix(".txp")
        if txp_file.exists():
            print(f"✅ {yaml_file} + {txp_file} OK (обновлено)")
        else:
            print(f"⚠ {yaml_file} VALID, но TXP не найден (обновлено)")


root_dir = Path("../models/Axe FX II/Amp")
example_yaml = Path("../tools/example.yaml")



# Валидация и автоматическое добавление недостающих атрибутов
update_profiles(root_dir)