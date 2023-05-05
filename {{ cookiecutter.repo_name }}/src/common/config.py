from pathlib import Path

import {{ cookiecutter.repo_name }}

PACKAGE_ROOT = Path({{ cookiecutter.repo_name }}.__file__).resolve().parent.parent