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

Based on the GNU Affero General Public License (AGPL), version 3:

THIS PROGRAM IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED,
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.
SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

IN NO EVENT WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS THE PROGRAM AS PERMITTED ABOVE,
BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE
OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

======================

By accepting these terms, you also agree to the Microsoft Software License Terms and the .NET Library EULA:
https://visualstudio.microsoft.com/license-terms/vs2022-cruntime/
https://dotnet.microsoft.com/en-us/dotnet_library_license.htm

Last updated: 29 July 2024
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
    Installer('.NET 8.0 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/bb581716-4cca-466e-9857-512e2371734b/5fe261422a7305171866fd7812d0976f/windowsdesktop-runtime-8.0.7-win-x64.exe', '391ca05d7540c58f25047ae07b8c5656829f7fd32f6e88a4e34c5337525f574e5714657e1c4f4f4d48e006087f573f8c03f1fc8eab8c9b9dab4d5ca5c8ea1fd4'),
    Installer('.NET 8.0 x86 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/853ca8b3-f0d0-4aac-a33b-d93bb1c991e9/9664c41e36cffd82b4f04471020116a7/windowsdesktop-runtime-8.0.7-win-x86.exe', '5adf46498caa1f4ae10ea6327f5c89f424665e1fc471cc8ca18c43779058a37aa5441ce89f82d9b2a5a4b877ab7f448fb5c48193e628eb038956f82d71880942')
]
