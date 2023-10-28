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
    Installer('.NET 7.0 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/515cc796-e9f2-4b5c-be7f-b42f115a65a7/b0b146fcbf1d1c135807ff24b3d88093/windowsdesktop-runtime-7.0.13-win-x64.exe', '66b252ea80571d29be668511c131f03c2d4d0d99c018ad21471048c96c5d41b175443910099e8579c4356562d7ba92793e971b510e4372d709b1ef549c0cc523'), 
    Installer('.NET 7.0 x86 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/84986c79-dd13-4bbc-abef-294638d5864a/75d29754580986fef26b5d64ec880075/windowsdesktop-runtime-7.0.13-win-x86.exe', '8dc11bb954eaeb67c67f118754872c58d30dce82f39f83fa4b4fd808c4aa4e249eb3fbe18f1ffbd4af39d8bdbb44a0a1a08232d02d4cbbba456f7e531bfbe3c7'),
    Installer('.NET 8.0 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/9c540179-a75c-4418-94fd-3bfe580e4251/6560fb0d71bf6434a4fe17b5cfa00a45/windowsdesktop-runtime-8.0.0-rc.2.23479.10-win-x64.exe', '480cd2cd85b10383b1d25ac1e03f060e7c491cf62ac9173ef83f52953e1fb282cdf29f64655d0436eb4a4ffd75333de180e19fa7deb93ea794d70e74296a026e'),
    Installer('.NET 8.0 x86 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/c2d2d578-40f2-4055-bf2f-77aec390e710/5dd9089e2fc23e7e87e8a691489cf617/windowsdesktop-runtime-8.0.0-rc.2.23479.10-win-x86.exe', '6d0dd5f9dfd53377eaef423c7887f78836099aee7848d74124724c34e5a9928621d2c6784e621ecd5d653f546b52cbbc564d12981b9b42addf6b20d10e7a85c3')
]