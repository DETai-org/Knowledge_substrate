"""Минималистичная конфигурация путей для ядра Uli."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Final, Iterable, Tuple

try:  # pragma: no cover - совместимость Python 3.10
    import tomllib  # type: ignore[attr-defined]
except ModuleNotFoundError:  # pragma: no cover - падение на Python < 3.11
    import tomli as tomllib  # type: ignore[import]


CONFIG_PATH: Final[Path] = Path(__file__).with_name("config.toml")


def _slug(value: str, fallback: str = "repository") -> str:
    cleaned = re.sub(r"[^0-9A-Za-z._-]+", "_", value.strip())
    cleaned = cleaned.strip("_")
    return cleaned or fallback


@dataclass(frozen=True)
class Paths:
    """Основные директории и файлы состояния UliCore."""

    base_dir: Path
    center_dir: Path
    cache_file: Path
    legacy_center_dirs: Tuple[Path, ...] = field(default_factory=tuple)
    legacy_cache_files: Tuple[Path, ...] = field(default_factory=tuple)

    @property
    def center(self) -> Path:
        """Базовая директория для кэшей GitHub."""

        return self.center_dir


def _load_local_config(config_path: Path) -> Dict[str, Any]:
    with config_path.open("rb") as fh:
        return tomllib.load(fh)


def load_base_dir(config_path: Path = CONFIG_PATH) -> Path:
    """Читает ``base_dir`` из локальной ``config.toml``."""

    config = _load_local_config(config_path)

    raw_base_dir = config.get("base_dir")
    if not raw_base_dir:
        raise RuntimeError("В config.toml отсутствует ключ base_dir")

    base_dir = Path(str(raw_base_dir)).expanduser()
    if not base_dir.is_absolute():
        base_dir = (config_path.parent / base_dir).resolve()
    else:
        base_dir = base_dir.resolve()
    return base_dir


def _build_paths(base_dir: Path) -> Paths:
    preferred_center = base_dir.parent / "uli" / "center"
    center_dir = preferred_center

    legacy_center_dirs: list[Path] = [base_dir / "center"]
    legacy_cache_files: list[Path] = []

    # Для обратной совместимости учитываем старую раскладку каталога Axiom.
    axiom_root = base_dir.parent / "axiom"
    axiom_center = axiom_root / "center"
    if axiom_center.exists():
        legacy_center_dirs.append(axiom_center)
        legacy_cache_files.append(axiom_center / "cache" / "github_meta.json")

    cache_dir = center_dir / "cache"
    repo_slug = _slug(base_dir.parent.name or "repository")

    return Paths(
        base_dir=base_dir,
        center_dir=center_dir,
        cache_file=cache_dir / f"{repo_slug}_github_meta.json",
        legacy_center_dirs=tuple(dict.fromkeys(legacy_center_dirs)),
        legacy_cache_files=tuple(
            dict.fromkeys(
                [
                    *legacy_cache_files,
                    base_dir / "center" / "cache" / "github_meta.json",
                    cache_dir / "github_meta.json",
                ]
            )
        ),
    )


PATHS: Final[Paths] = _build_paths(load_base_dir())


def ensure_parent(path: Path) -> Path:
    """Создаёт родительский каталог ``path`` если он отсутствует."""

    target = Path(path)
    parent = target.parent
    if parent and not parent.exists():
        parent.mkdir(parents=True, exist_ok=True)
    return target


def migrate_legacy_file(target: Path, candidates: Iterable[Path]) -> Path | None:
    """Переносит файл из старого расположения ``candidates`` в ``target``.

    Если файл уже существует по целевому пути, функция ничего не делает.
    Возвращает путь, откуда был перенесён файл, либо ``None`` если перенос
    не потребовался.
    """

    destination = Path(target)
    if destination.exists():
        return None

    for raw_candidate in candidates:
        candidate = Path(raw_candidate)
        if candidate == destination:
            continue
        if not candidate.exists():
            continue
        ensure_parent(destination)
        candidate.replace(destination)
        print(f"ℹ️ Перенёс файл из {candidate} в {destination}")
        return candidate

    return None
