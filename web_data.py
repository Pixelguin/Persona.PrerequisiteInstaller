import os
from urllib.parse import urlparse

# Version and repository info
web_version_latest_v2 = '2.3'
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
    Installer('.NET 3.1 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/b92958c6-ae36-4efa-aafe-569fced953a5/1654639ef3b20eb576174c1cc200f33a/windowsdesktop-runtime-3.1.32-win-x64.exe', '426add7ee806ff3e50e348bd294d406594c44d2a2894b037b1f871999ed9cce685f4fefac3828cd814897a2e40147647d03ba521d952a66bfe18c85767b40603'),
    Installer('.NET 5.0 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/3aa4e942-42cd-4bf5-afe7-fc23bd9c69c5/64da54c8864e473c19a7d3de15790418/windowsdesktop-runtime-5.0.17-win-x64.exe', 'f7eb69a953ff6346a180e5200075120b4b47cb89a75bc36c76a9e468c037bb2376f497dbf8e0bada152bc3ec35dceaad55d0a811586569575bf5b201d1e32baf'),
    Installer('.NET 5.0 x86 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/b6fe5f2a-95f4-46f1-9824-f5994f10bc69/db5ec9b47ec877b5276f83a185fdb6a0/windowsdesktop-runtime-5.0.17-win-x86.exe', '74a379323e52172f563cd996880f58d58a19303ae59b3f55ff52625dfe8a4a602609785b1174b38f2da97282f90f1ade53194354f48773512943eae249926ee8'),
    Installer('.NET 7.0 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/747f4a98-2586-4bc6-b828-34f35e384a7d/44225cfd9d365855ec77d00c4812133c/windowsdesktop-runtime-7.0.10-win-x64.exe', 'e69fc0f0577dd2c255257521b11cbc5507847d2a092bacf6a7fa3b4b0493390f709fa3cae785dcb7afb271ceb83b804196578f4a6931f9a3f635cae114bb53ec'), 
    Installer('.NET 7.0 x86 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/9812249d-fc42-41ab-bd2e-6e858d5dd5a7/95fa5a1a77eace4482bcb98ede190003/windowsdesktop-runtime-7.0.10-win-x86.exe', '6a3dd2540b4766187925ad01c25337bd697856f9d8078fc902fff3c61961420d6832bc5e4d2691c284815b4a323e7c0dd619d5b4b954e54fd13bbbed29a8cc7c'),
    Installer('.NET 8.0 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/3c2be57d-f02c-4317-a2cf-1d9ac406bfb8/3277392bf76f06d8cd597cdf8f124c4b/windowsdesktop-runtime-8.0.0-rc.1.23420.5-win-x64.exe', '9b430c3593f0dc7364aa8cf9f8d1793b396294695b751dbf5e9ed0147203657883c5f9da870bfe4595272372efe9b1238660c3818f72a80924e3473b5152635c'),
    Installer('.NET 8.0 x86 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/3bacce43-d067-4abf-8ac8-15eeb144a104/23475f771b28a14e652657205b855ce7/windowsdesktop-runtime-8.0.0-rc.1.23420.5-win-x86.exe', '0c6a41d2006fc485c6a42bd80059524eddc67c03bda78c5382b12fcb814169d76574abb984517fa736e66762e9ecbbc68406970ca7f3c45a323ed95667c98059')
]