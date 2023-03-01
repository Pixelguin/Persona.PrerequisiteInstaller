# Persona.PrerequisiteInstaller
 
## Build

```bat
pip install -r dependencies.txt
pyinstaller -F --uac-admin --exclude-module web_data Persona.PrerequisiteInstaller.py
```