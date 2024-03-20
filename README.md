# list-imports

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

#### CLI

##### All imports
```bash
find . -type f -name "*.py" | xargs python -m list_imports
```

##### High level imports only
```bash
find . -type f -name "*.py" | xargs python -m list_imports | awk -F"." '{print $1}'
```

### Uninstallation
```bash
pip uninstall list_imports \
&& pip uninstall click
```
