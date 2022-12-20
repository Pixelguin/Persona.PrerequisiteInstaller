import os
from urllib.parse import urlparse

# Version and repository info
web_version_latest = 2.0
web_version_supported = 2.0
web_repository = 'https://github.com/Pixelguin/P4GPC.PrerequisiteInstaller/releases/latest'

# Terms of use
web_terms = '''
=====TERMS OF USE=====

I am not responsible for anything that happens to any device this program runs on,
including anything that happens as a result of the installers this program downloads.
All responsibility resides with the user running the program.

By accepting these terms, you also agree to the Microsoft Software License Terms and the .NET Library EULA:
https://visualstudio.microsoft.com/license-terms/vs2022-cruntime/
https://dotnet.microsoft.com/en-us/dotnet_library_license.htm

Last updated: 14 December 2022
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
    Installer('Visual C++ x64 Redistributable', 'https://aka.ms/vs/17/release/vc_redist.x64.exe', 'a66ea382d8bdd31491627fd698242d2eda38b1d9df762c402923ef40bbca6aa2f43f22fa811c5fc894b529f9e77fcdd5ced9cd8af4a19f53845fce3780e8c041'),
    Installer('Visual C++ x86 Redistributable', 'https://aka.ms/vs/17/release/vc_redist.x86.exe', '02b959b3f008e70674f3fbb119601701057a0b3620e897a1b514a93ef22e930841d776d81506c0dc1d5d17899188ff489772ea5f9ae2f263fc1e304ebb7a491f'),
    Installer('.NET 3.1 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/b92958c6-ae36-4efa-aafe-569fced953a5/1654639ef3b20eb576174c1cc200f33a/windowsdesktop-runtime-3.1.32-win-x64.exe', '426add7ee806ff3e50e348bd294d406594c44d2a2894b037b1f871999ed9cce685f4fefac3828cd814897a2e40147647d03ba521d952a66bfe18c85767b40603'),
    Installer('.NET 5.0 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/3aa4e942-42cd-4bf5-afe7-fc23bd9c69c5/64da54c8864e473c19a7d3de15790418/windowsdesktop-runtime-5.0.17-win-x64.exe', 'f7eb69a953ff6346a180e5200075120b4b47cb89a75bc36c76a9e468c037bb2376f497dbf8e0bada152bc3ec35dceaad55d0a811586569575bf5b201d1e32baf'),
    Installer('.NET 5.0 x86 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/b6fe5f2a-95f4-46f1-9824-f5994f10bc69/db5ec9b47ec877b5276f83a185fdb6a0/windowsdesktop-runtime-5.0.17-win-x86.exe', '74a379323e52172f563cd996880f58d58a19303ae59b3f55ff52625dfe8a4a602609785b1174b38f2da97282f90f1ade53194354f48773512943eae249926ee8'),
    Installer('.NET 7.0 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/5b2fbe00-507e-450e-8b52-43ab052aadf2/79d54c3a19ce3fce314f2367cf4e3b21/windowsdesktop-runtime-7.0.0-win-x64.exe', 'e6281f475a58c8dc7b103d0cfd895e0f27235e25731b473514c82b77d8e555ea294f66ab3e119c5fd38c5a8f18b4a4d8508938d7cff70ab2186b47417349ea1e'), 
    Installer('.NET 7.0 x86 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/d05a833c-2cf9-4d06-89ae-a0f3e10c5c91/c668ff42e23c2f67aa3d80227860585f/windowsdesktop-runtime-7.0.0-win-x86.exe', '8904a454d07360ee1a4d75fb856afabf5192695602053f11f598650defe9acf5cb40ff20d70999af99971bac621dcfb01c63cb16014f93b3a498ab504ec9bbb1')
]