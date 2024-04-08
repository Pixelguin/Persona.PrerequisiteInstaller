import os
from urllib.parse import urlparse

# Version and repository info
web_version_latest_v2 = '2.3.1'
web_version_supported_v2 = '2.3.1'
web_repository = 'https://github.com/Pixelguin/Persona.PrerequisiteInstaller/releases/latest'

# Legacy version info (before packaging.version was implemented)
web_version_latest = 2.3
web_version_supported = 2.3

# Terms of use
web_terms = '''
=====TERMS OF USE=====

I am not responsible for anything that happens to any device this program runs on,
including anything that happens as a result of the installers this program downloads.
All responsibility resides with the user running the program.

By accepting these terms, you also agree to the Microsoft Software License Terms and the .NET Library EULA:
https://visualstudio.microsoft.com/license-terms/vs2022-cruntime/
https://dotnet.microsoft.com/en-us/dotnet_library_license.htm

Last updated: 20 December 2022
'''

# Installer class
'''
name: The full name of the prerequisite.
url: The URL from which to download the prerequisite.
checksum: The SHA-512 checksum of the prerequisite, provided by Microsoft.
'''
class Installer:
    def __init__(self, n, u, c):
        self.name = n
        self.url = u
        self.checksum = c

    def get_filename(self):
        return(os.path.basename(self.url))
    
    def get_host(self):
        return(urlparse(self.url).hostname)

# web_installers array
web_installers = [
    Installer('Visual C++ x64 Redistributable', 'https://aka.ms/vs/17/release/vc_redist.x64.exe', '70a05bde549e5a973397cd77fe0c6380807cae768aa98454830f321a0de64bd0da30f31615ae6b4d9f0d244483a571e46024cf51b20fe813a6304a74bd8c0cc2'),
    Installer('Visual C++ x86 Redistributable', 'https://aka.ms/vs/17/release/vc_redist.x86.exe', 'c08d1aa7e6e6215a0cee2793592b65668066c8c984b26675d2b8c09bc7fee21411cb3c0a905eaee7a48e7a47535fa777de21eeb07c78bca7bf3d7bb17192acf2'),
    Installer('.NET 8.0 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/51bc18ac-0594-412d-bd63-18ece4c91ac4/90b47b97c3bfe40a833791b166697e67/windowsdesktop-runtime-8.0.3-win-x64.exe', 'f4cf0300eb4e1750b75a9d973db2d100cd8fb244ef0c7bc5ab448dcc72091055c516d7fe6ea41215bdccec13fc08c5b3c444400c74b214af7f996e5780275f08'),
    Installer('.NET 8.0 x86 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/c629f243-5125-4751-a5ff-e78fa45646b1/85777e3e3f58f863d884fd4b8a1453f2/windowsdesktop-runtime-8.0.3-win-x86.exe', 'b9b14552661f35b173c1539ffb422f31b13926dcd0d7aeba5283a467288f4db288f6afeede2fe3e57ed7d3ef3847dba7bd2725b8791396a0633dd14d957b1d34')
]