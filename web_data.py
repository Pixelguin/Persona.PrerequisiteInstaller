import os
from urllib.parse import urlparse

# Version and repository info
web_version_latest_v2 = '3.0.0'
web_version_supported_v2 = '3.0.0'
web_repository = 'https://github.com/MadMax1960/Persona.PrerequisiteInstaller/releases/latest'

# Terms of use
web_terms = '''
=====TERMS OF USE=====

Based on the GNU Affero General Public License (AGPL), version 3:

THIS PROGRAM IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED,
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.

THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU.
SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

IN NO EVENT WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS THE PROGRAM AS PERMITTED IN
THE LICENSE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING
OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED
INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

======================

By accepting these terms, you also agree to the Microsoft Software License Terms and the .NET Library EULA:
https://visualstudio.microsoft.com/license-terms/vs2022-cruntime/
https://dotnet.microsoft.com/en-us/dotnet_library_license.htm

Last updated: 31 August 2024
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
    Installer('.NET 8.0 x64 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/907765b0-2bf8-494e-93aa-5ef9553c5d68/a9308dc010617e6716c0e6abd53b05ce/windowsdesktop-runtime-8.0.8-win-x64.exe', '27484ffb1e9ce5e6290cda8f5f49563cf4a9e2692aa57429fcd0d3de4f30fc2fce204b1b120349ed50712e95d3fa51037ebaf9b7fd60c41856857b1372e0eac7'),
    Installer('.NET 8.0 x86 Desktop Runtime',   'https://download.visualstudio.microsoft.com/download/pr/bd1c2e28-44dd-47bb-a55c-aedd1f3e8cc4/0a15fac821e64cf7b8ec6d99e54e0997/windowsdesktop-runtime-8.0.8-win-x86.exe', '3101e64ab772cef8081ca5f441f599d1906c9a3869e7ff20ee1725e121a54dd0569e55dfd842e748a0dd6bff902562834922681c9bb43ede6760aed1206c7966')
]
