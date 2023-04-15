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
    Installer('.NET 7.0 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/dffb1939-cef1-4db3-a579-5475a3061cdd/578b208733c914c7b7357f6baa4ecfd6/windowsdesktop-runtime-7.0.5-win-x64.exe', '8907aa0e934a31c63f0a840bf9e734c2f5ba109b766c1a775f8adbb169049753664790c0a15b216f02a942392819a3500e4a33918df10fb967341dc167f82d11'), 
    Installer('.NET 7.0 x86 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/eb64dcd1-d277-4798-ada1-600805c9e2dc/fc73c843d66f3996e7ef22468f4902e6/windowsdesktop-runtime-7.0.5-win-x86.exe', 'a2f776cfabcfbd4b9278198301d289ed1c56febd47259520c50b8b8d130a79d0ea99c857aec96865cc635ddf078fd575368c030ce11d61bb9991d296df87a4a7')
]