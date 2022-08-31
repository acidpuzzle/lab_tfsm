from pathlib import Path

from .main import parse_output_to_dict

tempate_path = str(Path("templates/").absolute())

__all__ = ["parse_output_to_dict", "tempate_path"]
