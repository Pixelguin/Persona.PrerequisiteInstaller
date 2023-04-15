import os
from urllib.parse import urlparse

# Version and repository info
web_version_latest_v2 = '2.2.1'
web_version_supported_v2 = '2.1'
web_repository = 'https://github.com/Pixelguin/Persona.PrerequisiteInstaller/releases/latest'

# Legacy version info (before packaging.version was implemented)
web_version_latest = 2.2
web_version_supported = 2.1

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
    Installer('Visual C++ x64 Redistributable', 'https://aka.ms/vs/17/release/vc_redist.x64.exe', '9be541f26b5d43cee1766239d8880ab7d30d18fea2f17e28d63a498b30b7dd0918f389805398cb56b0df0df17c8633cb73f9e46672c93b21be04b85bda7a2648'),
    Installer('Visual C++ x86 Redistributable', 'https://aka.ms/vs/17/release/vc_redist.x86.exe', '28cf976fa51e4c7abb57fd8fcde6381f1e140407924ef265fde6e59546fb6fdeb803f388a5d1e9e74fb80d47ce5fd9f275aaf41258a09002fba27c2cbbc2df4d'),
    Installer('.NET 3.1 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/b92958c6-ae36-4efa-aafe-569fced953a5/1654639ef3b20eb576174c1cc200f33a/windowsdesktop-runtime-3.1.32-win-x64.exe', '426add7ee806ff3e50e348bd294d406594c44d2a2894b037b1f871999ed9cce685f4fefac3828cd814897a2e40147647d03ba521d952a66bfe18c85767b40603'),
    Installer('.NET 5.0 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/3aa4e942-42cd-4bf5-afe7-fc23bd9c69c5/64da54c8864e473c19a7d3de15790418/windowsdesktop-runtime-5.0.17-win-x64.exe', 'f7eb69a953ff6346a180e5200075120b4b47cb89a75bc36c76a9e468c037bb2376f497dbf8e0bada152bc3ec35dceaad55d0a811586569575bf5b201d1e32baf'),
    Installer('.NET 5.0 x86 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/b6fe5f2a-95f4-46f1-9824-f5994f10bc69/db5ec9b47ec877b5276f83a185fdb6a0/windowsdesktop-runtime-5.0.17-win-x86.exe', '74a379323e52172f563cd996880f58d58a19303ae59b3f55ff52625dfe8a4a602609785b1174b38f2da97282f90f1ade53194354f48773512943eae249926ee8'),
    Installer('.NET 7.0 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/b6a55627-12de-482a-aea8-17d635f4b775/d8798c0c796a945c657d04438cf9b84d/windowsdesktop-runtime-7.0.4-win-x64.exe', '03b1164beccec1421e46ed9bc6bc35c9b746a580b33cb71112a41f6e3b94e37d8f02cbcf0ada74e250f29286f7301828fc6f9dd78d11f0b7cacea4604414401b'), 
    Installer('.NET 7.0 x86 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/9c8d474f-e58f-4ab2-ab3c-f6c2c8616910/41b492e1c41083c823d56162c700de57/windowsdesktop-runtime-7.0.4-win-x86.exe', '2b31ad155f146ae802a7232d3511e910e95d46f00c4c39b0ffe521d53f4f2ef0d74adb3c9455ef5c86e0331d696ecca4eab0a2832f74b9942db8060497199e89')
]