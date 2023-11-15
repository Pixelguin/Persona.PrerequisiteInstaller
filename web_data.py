import os
from urllib.parse import urlparse

# Version and repository info
web_version_latest_v2 = '2.3.1'
web_version_supported_v2 = '2.3'
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
    Installer('Visual C++ x64 Redistributable', 'https://aka.ms/vs/17/release/vc_redist.x64.exe', '70a888d5891efd2a48d33c22f35e9178bd113032162dc5a170e7c56f2d592e3c59a08904b9f1b54450c80f8863bda746e431b396e4c1624b91ff15dd701bd939'),
    Installer('Visual C++ x86 Redistributable', 'https://aka.ms/vs/17/release/vc_redist.x86.exe', 'ec70786704ead0494fab8f7a9f46554feaca45c79b831c5963ecc20243fa0f31053b6e0ceb450f86c16e67e739c4be53ad202c2397c8541365b7252904169b41'),
    Installer('.NET 7.0 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/8f5b0079-2bb4-49cd-874e-0f58703eff6e/7010b5f213a2c436a307eb385dbb16ff/windowsdesktop-runtime-7.0.14-win-x64.exe', 'cb43e9852e719cc2b42a7e3f265e816e20629980f3f0eee6b655558efefb7c8749aedcc9cd7c1f7cbaed5e228ff6d7d2a9fe3cc5434c9a19869dd50921c3bea5'), 
    Installer('.NET 7.0 x86 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/3a87d4cf-87c7-4432-89af-37f21dc651a7/7996e26d189d21afa4fe54a02062df5d/windowsdesktop-runtime-7.0.14-win-x86.exe', '6784176e4e341c66fb49321acef2261a4067360dee11a1c51989c701eac707bc58848abce8ef6cd934135924317e1432dcb1504f03c184648685545c9356f1f5'),
    Installer('.NET 8.0 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/b280d97f-25a9-4ab7-8a12-8291aa3af117/a37ed0e68f51fcd973e9f6cb4f40b1a7/windowsdesktop-runtime-8.0.0-win-x64.exe', 'd2e92f8bdb2b840c3fee170f2ca3baa3237a6a56c7b86589f7e4d7a0d51d2605bafe045adbd14a0c43e946a8a895a621748418d1a2cb9c44370eafd1d1a8ffa9'),
    Installer('.NET 8.0 x86 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/f9e3b581-059d-429f-9f0d-1d1167ff7e32/bd7661030cd5d66cd3eee0fd20b24540/windowsdesktop-runtime-8.0.0-win-x86.exe', '711134538d6e7dc827c99914e7ae74cb2a0c41ce2b1b4fd2b6323032c05db31737a4370f613621bc04787e7ab4b6d377e62dd777c2b51db6636afd751e874ae4')
]