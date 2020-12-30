# unoffice
Tiny read-only unlocker for MS Office documents

# Features
Unoffice can remove read-only protection of:
  - Full and partial protected Word files.
  - Full Excel file and partially protected sheets
  - PowerPoint protected files.

# Usage
  - via script:
```python
from unoffice import unlock

unlock('path\\to\\file.docx')
```
  - via terminal:
```
python unoffice.py "first-path" "second-path" ... "nth-path"
```

# Tests
You can `python tests.py` to see unoffice results

## Contributing
Please contribute! If you want to fix a bug, suggest improvements, or add new features to the project, just [open an issue](https://github.com/elmoiv/unoffice/issues) or send me a pull request.
