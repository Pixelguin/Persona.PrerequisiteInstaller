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
    Installer('.NET 7.0 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/2ce1cbbe-71d1-44e7-8e80-d9ae336b9b17/a2706bca3474eef8ef95e10a12ecc2a4/windowsdesktop-runtime-7.0.11-win-x64.exe', 'c5f042dadd878e2cbd1833a73141e64fba2fae10ba5770daac8faf24bb56d7bc61cae8f7664c37fa822db71d0bf05b97733126db396e97e9ceeced596b9a63c1'), 
    Installer('.NET 7.0 x86 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/8390b217-55b7-497e-ba1b-b70f0a93cf29/39ab1928787ffc939d95e97c1f5a33e4/windowsdesktop-runtime-7.0.11-win-x86.exe', 'b7583409ea718d60ac81e8d28ab7511850d0b43e9bb9ea8488dd473b1ca904afe99d1ab298b1c5ab5271d8584baed65653196d3caf0ad9737e70f2eccbb9be4c'),
    Installer('.NET 8.0 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/3c2be57d-f02c-4317-a2cf-1d9ac406bfb8/3277392bf76f06d8cd597cdf8f124c4b/windowsdesktop-runtime-8.0.0-rc.1.23420.5-win-x64.exe', '9b430c3593f0dc7364aa8cf9f8d1793b396294695b751dbf5e9ed0147203657883c5f9da870bfe4595272372efe9b1238660c3818f72a80924e3473b5152635c'),
    Installer('.NET 8.0 x86 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/3bacce43-d067-4abf-8ac8-15eeb144a104/23475f771b28a14e652657205b855ce7/windowsdesktop-runtime-8.0.0-rc.1.23420.5-win-x86.exe', '0c6a41d2006fc485c6a42bd80059524eddc67c03bda78c5382b12fcb814169d76574abb984517fa736e66762e9ecbbc68406970ca7f3c45a323ed95667c98059')
]