import ctypes, logging, os, requests, subprocess, sys, time
from pathlib import Path
from simple_file_checksum import get_checksum
DEV = False

if DEV:
    os.chdir(os.path.dirname(os.path.abspath(__file__))) # [DEV] Set working directory to the .py file's location
else:
    sys.path.append(os.path.dirname(sys.executable)) # Needed to import web file as module at runtime, see https://stackoverflow.com/a/47388482

PROGRAM_NAME = 'All-In-One Prerequisite Installer'
PROGRAM_NAME_SHORT = 'pi'
VERSION = 2.1

# Set directory paths
SETUP_DIR = Path(os.getcwd())
DOWNLOADS_DIR = SETUP_DIR / f'{PROGRAM_NAME_SHORT}_downloads'
LOGS_DIR = SETUP_DIR / f'{PROGRAM_NAME_SHORT}_logs'
INSTALL_LOGS_DIR = LOGS_DIR / 'installers'

WEB_FILE = 'web_data.py'
LOGS_FILE = LOGS_DIR / f"{PROGRAM_NAME_SHORT}Log_{time.strftime('%Y%m%d-%H%M%S')}.txt"

WEB_URL = f'https://raw.githubusercontent.com/Pixelguin/Persona.PrerequisiteInstaller/master/{WEB_FILE}'

# Create directories
if not os.path.exists(DOWNLOADS_DIR):
    os.makedirs(DOWNLOADS_DIR)

if not os.path.exists(LOGS_DIR):
    os.makedirs(LOGS_DIR)

if not os.path.exists(INSTALL_LOGS_DIR):
    os.makedirs(INSTALL_LOGS_DIR)

# Create logger
log = logging.getLogger('logger')
log.setLevel(logging.DEBUG)

file_formatter = logging.Formatter('>%(levelname)-10s %(message)s') # Show level in log file but not console
console_formatter = logging.Formatter('%(message)s')

file_handler = logging.FileHandler(LOGS_FILE, mode = 'w', encoding = 'utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(file_formatter)
log.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(console_formatter)
log.addHandler(console_handler)

# First log message
log.debug(f'Created {LOGS_FILE}\n')

def fatal_error(message):
    '''
    Output critical error message and log file path.
    Prompt user to press Enter, then end the program.
    '''

    log.critical(f'\n{message}\nA log is available at {LOGS_FILE}\n\nPress Enter to end the program...')
    input()
    sys.exit()

def prompt_complex(prompt, acceptable_responses):
    '''
    Prompt user for a string response.
    If the response is one of the acceptable responses in a given array, return that response.
    Else, inform the user of acceptable responses and repeat the prompt.
    '''

    response = ''
    while response not in acceptable_responses:
        log.info(f'======================\n\n{prompt}')
        response = input()
        log.debug(f'User response: {response}')

        if response in acceptable_responses:
            return response
        else:
            log.warning(f"\nSorry, I didn't understand '{response}'.\nAcceptable responses are: {acceptable_responses}\n")

def prompt_yn(prompt):
    '''
    Run prompt_complex with pre-defined acceptable responses for yes/no.
    Return True for 'yes' or False for 'no'. 
    '''

    response = prompt_complex(prompt, ['y', 'n', 'yes', 'no'])
    return (response in {'y', 'yes'})

def download_file(path, url):
    '''
    Download a file from a given URL and save it to a given path.
    Return the response status code.
    '''
    
    log.debug(f'Downloading {path} from {url}')

    with open(path,'wb') as download:
        try:
            response = requests.get(url, allow_redirects=True)
            download.write(response.content)
        except:
            log.debug(f'Failed to download {path}!')
            return 9999

        if response.is_redirect:
            log.debug(f'Download was redirected to {response.url}')
        
        log.debug(f'Got response status {response.status_code}')
        return response.status_code

def verify_checksum(file, checksum_correct):
    '''
    Calculate a file's SHA-512 checksum and compare it to a known correct checksum.
    Return true if checksums match, or false if checksums do not match.
    '''

    checksum_calculated = get_checksum(file, algorithm = 'SHA512')
    log.debug(f'{os.path.basename(file)} has checksum {checksum_calculated}')

    if checksum_calculated == checksum_correct:
        log.debug('Checksum is valid')
        return True
    else:
        log.debug(f'Checksum is invalid, expected {checksum_correct}')
        return False

'''
PROGRAM START
'''
log.info(f'Persona Modding: {PROGRAM_NAME} {VERSION}\nby Pixelguin\n')
if DEV:
    log.info('===! DEV IS ENABLED !===\n')

# Check for administrator elevation
try:
    is_admin = (os.getuid() == 0)
except AttributeError:
    log.debug('AttributeError thrown when using os.getuid(), trying ctypes method')
    is_admin = (ctypes.windll.shell32.IsUserAnAdmin() != 0)

log.debug(f'is_admin returned {is_admin}')

if DEV:
    log.debug('[DEV] Skipping admin check')
elif is_admin:
    log.debug('Program is admin')
else:
    log.debug('Program is NOT admin')
    fatal_error('This program must be run with administrator privileges.')

# Download and import latest web data
log.info('Downloading the latest configuration data...\n')

if os.path.exists(WEB_FILE):
    if DEV:
        log.debug(f'[DEV] Using local {WEB_FILE}')
    else:
        log.debug(f'{WEB_FILE} exists, deleting...')
        os.remove(WEB_FILE)

if download_file(WEB_FILE, WEB_URL) >= 400:
    fatal_error(f'Failed to download configuration data - Cannot continue!\nCheck your Internet connection and make sure you have the latest release of {PROGRAM_NAME}.')

from web_data import *

# Check if this version is supported
if VERSION < web_version_supported:
    fatal_error(f'This version of {PROGRAM_NAME} is too old - Cannot continue!\nDownload the latest release ({web_version_latest}) at {web_repository}')
else:
    if VERSION < web_version_latest:
        log.warning(f'Version {web_version_latest} of {PROGRAM_NAME} is available, but this version is still supported.\nIf something goes wrong during installation, try the latest release at {web_repository}\n')

    log.info('Ready! Press Enter to begin...')
    input()
    os.system('cls')

# Show user what will be installed
log.info(f'This program will download and install {len(web_installers)} prerequisites needed for Persona modding:\n')
for my_installer in web_installers:
    log.info(my_installer.name)

log.info('\nPress Enter to continue...')
input()

# Prompt user to accept terms
log.info(web_terms)

if prompt_yn('Do you accept these terms? (y/n)') == True:
    log.debug('Terms of use accepted')
else:
    fatal_error('Terms of use were denied - Cannot continue!')

# Prompt user to choose between Quiet and Manual Mode
os.system('cls') # Clear screen
log.info(f'''{PROGRAM_NAME} has the option to run in Quiet Mode or Manual Mode.

Quiet Mode will automatically install each prerequisite after it is downloaded.
All you need to do is sit back and watch the installer work its magic!

Manual Mode will open the installation window for each prerequisite after it is downloaded.
You will need to manually confirm the installation by clicking Install or Repair.

Regardless of which option you choose, an installation log for each prerequisite will be saved in the 
{INSTALL_LOGS_DIR} folder.
''')

install_mode = prompt_complex(f"Would you like to use Quiet Mode or Manual Mode?\nType 'quiet' or 'manual' and press Enter.", ['quiet', 'manual'])
os.system('cls')

# Set variables and flags
loop_count = 0
success_count = 0
restart_count = 0

# Download and run installers
for my_installer in web_installers:
    # Variables and flags
    file = DOWNLOADS_DIR / my_installer.get_filename()
    file_verified = False
    file_installed = False
    loop_count += 1

    # Print installer name and filename
    log.info(f'======================\n\n({loop_count}/{len(web_installers)}) {my_installer.name}\n')
    log.debug(f'success_count = {success_count}')

    # Check if file already exists and verify checksum
    if (os.path.exists(file)):
        log.info(f'{my_installer.get_filename()} already exists, verifying checksum...')

        if verify_checksum(file, my_installer.checksum):
            log.info('Checksum is OK, skipping download.\n')
            file_verified = True
        else:
            log.info('Checksum does not match, will need to redownload.\n')
            os.remove(file)

    # If file doesn't exist, download it from URL
    if not file_verified:
        log.info(f'Downloading {my_installer.get_filename()} from {my_installer.get_host()}...')

        if download_file(file, my_installer.url) < 400:
            log.info('Verifying checksum...')
            if verify_checksum(file, my_installer.checksum):
                log.info('Checksum is OK.\n')
                file_verified = True
            else:
                log.error(f'{my_installer.get_filename()} checksum is incorrect!\n{my_installer.name} may not have downloaded properly.\n')
        else:
            log.error(f'Failed to download {my_installer.name}! Check your Internet connection.\n')

    # If file is verified, execute the installer
    if file_verified:
        log.info(f'{install_mode[0].upper()}{install_mode[1:]}ly installing {my_installer.name}...')

        install_log = INSTALL_LOGS_DIR / f'{my_installer.get_filename()}-Install.log' #Installation log
        log.debug(f'A log is available at {install_log}')

        install_args = [file, '/install', '/norestart', '/log', install_log]
        if install_mode == 'quiet':
            install_args.insert(2, '/quiet') #Add /quiet argument for Quiet Mode

        try:
            exit_status = subprocess.check_call(install_args, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) #Don't output anything to the console window
            log.debug(f'Subprocess returned exit status {exit_status}')
        except subprocess.CalledProcessError as e:
            if e.returncode == 1602:
                log.error('Installation failed - The installation window was closed by the user or administrator permissions were not given!\n')
            elif e.returncode == 1638:
                log.info(f'Installation skipped - A newer version of {my_installer.name} is already installed. (This is not an error!)\n')
                success_count += 1
            elif e.returncode == 3010:
                log.info(f'{my_installer.name} installed successfully!\nYou must restart your PC to complete the installation.')
                success_count += 1
                restart_count += 1
            else:
                log.error(f'Installation failed - Unknown error! (Subprocess returned exit status {e.returncode})\n')
        else:
            log.info(f'{my_installer.name} installed successfully!\n')
            success_count += 1

# Finished
log.info(f'======================\n\nSuccessfully installed {success_count}/{len(web_installers)} prerequisite(s)!')

if restart_count > 0:
    log.warning(f'Please restart your PC to complete the installation of {restart_count} prerequisite(s).\n')

if success_count < len(web_installers):
    log.warning(f'{len(web_installers) - success_count} prerequisite(s) did not install correctly.\nTry running this program one more time in Manual Mode, and reach out for support if this message appears again.\n')
else:
    log.info('\nAll finished!')

log.info('Press Enter to end the program...')
input()
sys.exit()