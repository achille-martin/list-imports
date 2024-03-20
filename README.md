[![](https://img.shields.io/pypi/v/list-imports.svg?maxAge=3600)](https://pypi.org/project/list-imports/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/list-imports.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/list-imports.py/actions)

### Installation
```bash
pip install git+https://github.com/achille-martin/list-imports
```

### Examples
```python
import list_imports
imports = list_imports.get("file.py")
```

#### From string
```python
imports = list_imports.parse(open("file.py").read())
```

#### Absolute imports only
```python
list(filter(lambda i:i[0]!='.',list_imports.get("file.py")))
```

#### cli
```bash
find . -type f -name "*.py" | xargs python -m list_imports
find . -type f -name "*.py" | xargs python -m list_imports | awk -F"." '{print $1}'
```

### Uninstallation
```bash
pip uninstall list_imports
pip uninstall click
```
