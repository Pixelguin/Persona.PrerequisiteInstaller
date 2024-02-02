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
    Installer('.NET 7.0 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/00f765dd-f009-41b4-921f-bee1273f3638/3cb6ac95b2aa7eeb272c6179d56fd036/windowsdesktop-runtime-7.0.15-win-x64.exe', '9fcf6fe4a49ccac84fced899039522eee06210cb7d7add57d2c4f76560a4698f38ce22305d13f129a535fc105e3e7e132b90f9b9aadeaffae076f037c891813b'), 
    Installer('.NET 7.0 x86 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/fd3675e7-91e6-4fce-9c77-9336a4973e42/e970987509babd919e8ea29309054c8c/windowsdesktop-runtime-7.0.15-win-x86.exe', 'f749fbb22ae6daf5370f2d8c0961af049a723b742805a5a36dc2288f0318ceb600551ff72fa79aaa393b22a207165c92aa2de918c7215b6f4caa7fb679a3df69'),
    Installer('.NET 8.0 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/f18288f6-1732-415b-b577-7fb46510479a/a98239f751a7aed31bc4aa12f348a9bf/windowsdesktop-runtime-8.0.1-win-x64.exe', '233d98b280eb4353fff7e45fa45e0de510403853e881c0bdcd3eb2466df4930795a62fec14cb30d05e00bff37f17b4d6c9b95511ca71475b739d6d9be9d2ebab'),
    Installer('.NET 8.0 x86 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/ca725693-6de7-4a4d-b8a4-4390b0387c66/ce13f2f016152d9b5f2d3c6537cc415b/windowsdesktop-runtime-8.0.1-win-x86.exe', '1d2cdb417ff9d72e4766255a1d7568bc16348120c72db58a020f35917b47a0f39dd74e185371668419a9f8a4fc2e9aad4073b5dcb273d010fbf9b16a718d018d')
]