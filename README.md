# P4GPC.PrerequisiteInstaller
 
## Build

```bat
pip install simple-file-checksum
pip install pyinstaller
pyinstaller -F --uac-admin --exclude-module web_data P4GPC.PrerequisiteInstaller.py
```