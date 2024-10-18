# Persona.PrerequisiteInstaller
 
Public domain archive of Persona Prerequisite Installer 2.3.1

Now forked and maintained at [MadMax1960/Persona.PrerequisiteInstaller](https://github.com/MadMax1960/Persona.PrerequisiteInstaller/)

----
 
## Build

```bat
pip install -r dependencies.txt
pyinstaller -F --uac-admin --exclude-module web_data Persona.PrerequisiteInstaller.py
```
