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
    Installer('.NET 8.0 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/84ba33d4-4407-4572-9bfa-414d26e7c67c/bb81f8c9e6c9ee1ca547396f6e71b65f/windowsdesktop-runtime-8.0.2-win-x64.exe', '62cd6be9ea5c397b607c75a3a9da332476b456482e20a3e786e964eae352965678c979792f3e0577d76205761b9c53da86c3aea6ae122934e4be7cf38648e950'),
    Installer('.NET 8.0 x86 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/9b77b480-7e32-4321-b417-a41e0f8ea952/3922bbf5538277b1d41e9b49ee443673/windowsdesktop-runtime-8.0.2-win-x86.exe', '3700642786b3f9a67218b6a834a8472c31d8e5ae6c2436c752e2ade37d9cb0ff808e35bb9fc3207ecbdb6e4e934c1dc77796d47ed0b2d228755f9876d4e0af0a')
]