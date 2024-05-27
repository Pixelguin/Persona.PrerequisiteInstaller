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

This program is provided "as-is" without any warranty, expressed or implied.

I am not responsible for anything that happens to any device this program runs on,
including anything that happens as a result of the installers this program downloads.
All responsibility resides with the user running the program.

By accepting these terms, you also agree to the Microsoft Software License Terms and the .NET Library EULA:
https://visualstudio.microsoft.com/license-terms/vs2022-cruntime/
https://dotnet.microsoft.com/en-us/dotnet_library_license.htm

Last updated: 06 May 2024
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
    Installer('Visual C++ x64 Redistributable', 'https://aka.ms/vs/17/release/vc_redist.x64.exe', '5935b69f5138ac3fbc33813c74da853269ba079f910936aefa95e230c6092b92f6225bffb594e5dd35ff29bf260e4b35f91adede90fdf5f062030d8666fd0104'),
    Installer('Visual C++ x86 Redistributable', 'https://aka.ms/vs/17/release/vc_redist.x86.exe', '91a6283f774f9e2338b65aa835156854e9e76aed32f821b13cfd070dd6c87e1542ce2d5845beb5e4af1ddb102314bb6e0ad6214d896bb3e387590a01eae0c182'),
    Installer('.NET 8.0 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/c1d08a81-6e65-4065-b606-ed1127a954d3/14fe55b8a73ebba2b05432b162ab3aa8/windowsdesktop-runtime-8.0.4-win-x64.exe', '8a0b1ab3a774c33f46cd042783cf785c33f2d9e0bdeee4ff8bf96cfa90a2101a5711231840ef93eab101409e7f3f3770d86e1a55bd52709af08d1a6c908cc194'),
    Installer('.NET 8.0 x86 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/1fbf5c5f-9770-402d-8971-83da662d8cf9/4e37b3c24bcb6004875b9f8b08024303/windowsdesktop-runtime-8.0.4-win-x86.exe', 'edeee99d70e776e21f84af1e6c63690f43fa5c89d4ac2e3de4e376eede0c8b2aedea8b7c890e1b8e1136d44c8f4a103be68c972b3d6a771b88d4f3adda75e1b5')
]