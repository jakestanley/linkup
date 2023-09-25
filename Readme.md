# Linkup

Tool for managing dedicated servers for linkup games

# Dependencies

- python
- [pysteamcmd](https://github.com/f0rkz/pysteamcmd)
- pyinstaller (build only)

# Build

## Windows

Tested on Windows 11 with Python 3.11.4

### Dependencies

- powershell
- python3
- pyinstaller
- git

### Commands

From PowerShell

```
pip install -r requirements.txt
pyinstaller linkup.py
New-Item -ItemType Directory releases -Force
$tag=$(git describe --exact-match --tags || git rev-parse --short HEAD)
Compress-Archive .\dist\linkup\* "releases\linkup_win_$($tag).zip"
```