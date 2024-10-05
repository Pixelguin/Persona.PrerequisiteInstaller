# Native libraries
import ctypes
import logging
import os
import subprocess
import sys
from pathlib import Path
import time

# External libraries
from packaging import version
import requests
from simple_file_checksum import get_checksum

DEV = False

if DEV:
    os.chdir(os.path.dirname(os.path.abspath(__file__))) # [DEV] Set working directory to the .py file's location
else:
    sys.path.append(os.path.dirname(sys.executable)) # Needed to import web file as module at runtime, see https://stackoverflow.com/a/47388482

PROGRAM_NAME = 'Persona Prerequisite Installer'
PROGRAM_NAME_SHORT = 'ppi'
VERSION = '3.0.0'

DIVIDER = '======================'

# Set directory paths
SETUP_DIR = Path(os.getcwd())
DOWNLOADS_DIR = SETUP_DIR.joinpath(f'{PROGRAM_NAME_SHORT}_downloads')
LOGS_DIR = SETUP_DIR.joinpath(f'{PROGRAM_NAME_SHORT}_logs')
INSTALL_LOGS_DIR = LOGS_DIR.joinpath('installers')

WEB_FILE = 'web_data.py'
LOGS_FILE = LOGS_DIR.joinpath(f"{PROGRAM_NAME_SHORT}Log_{time.strftime('%Y%m%d-%H%M%S')}.txt")

WEB_URL = f'https://raw.githubusercontent.com/MadMax1960/Persona.PrerequisiteInstaller/master/{WEB_FILE}'

# Create directories
os.makedirs(DOWNLOADS_DIR, exist_ok = True)
os.makedirs(LOGS_DIR, exist_ok = True)
os.makedirs(INSTALL_LOGS_DIR, exist_ok = True)

# Create logger
LOG_FILE_INDENT = 11

log = logging.getLogger('logger')
log.setLevel(logging.DEBUG)

class MultilineIndentFormatter(logging.Formatter):
    '''
    Custom log formatter for multiline messages.

    This formatter modifies logging.Formatter to add a fixed number of spaces to newline characters.
    This ensures multiline log messages in file_formatter are properly indented.

    Returns:
        str: The formatted message.
    '''
    def format(self, record):
        s = super().format(record)
        return s.replace('\n', '\n' + ' ' * int(LOG_FILE_INDENT + 1))

file_formatter = MultilineIndentFormatter(f'>%(levelname)-{LOG_FILE_INDENT}s%(message)s') # Show level in log file but not console
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
    Output a critical error message and the log file path, then end the program.

    This function outputs a critical error message to the console and log along with a path to the console log file.
    It then prompts the user to press Enter, which ends the program.

    Args:
        message (str): The critical error message to output.

    Returns:
        None
    '''

    log.critical(f'\n{message}\nA log is available at {LOGS_FILE}\n\nPress Enter to end the program...')
    input()
    sys.exit()

def prompt_complex(prompt, acceptable_responses):
    '''
    Prompt the user for a string response and verify it is in a list of acceptable responses.

    This function prompts the user for a string response, then checks if it is in a list of acceptable responses.
    If the response is acceptable, the function returns that response.
    Else, the user is shown a list of acceptable responses and the prompt is repeated until an acceptable response is given.
    
    Exceptions that end the program during input are handled by outputting a fatal error notifying the user what happened.

    Args:
        prompt (str): The prompt message to show the user
        acceptable_responses (list[str]): A list of acceptable responses

    Returns:
        str: The acceptable response given by the user
    '''

    response = ''
    while response not in acceptable_responses:
        try:
            log.info(f'{DIVIDER}\n\n{prompt}')
            response = input()
            log.debug(f'User response: {response}')

            if response in acceptable_responses:
                return response
            else:
                log.warning(f"\nSorry, I didn't understand '{response}'.\nAcceptable responses are: {acceptable_responses}\n")

        # Output a fatal error if the user escapes the program (Ctrl+D, Ctrl+C, etc.)    
        except (EOFError, KeyboardInterrupt):
            fatal_error('User exited the program while it was waiting for input - Cannot continue!')
            break

def prompt_yn(prompt):
    '''
    Prompts the user for a yes or no response using the prompt_complex function.

    This program prompts the user for a yes/no response, then checks if it is in a list of acceptable "yes" or "no" responses.
    If the response is acceptable, the function returns True (yes) or False (no).
    Else, the user is shown a list of acceptable responses and the prompt is repeated until an acceptable response is given.

    Args:
        prompt (str): The yes/no prompt message to show the user

    Returns:
        bool: True if the user responds with 'yes' or 'y', False if the user responds with 'no' or 'n'
    '''

    response = prompt_complex(prompt, ['y', 'n', 'yes', 'no'])
    return (response in {'y', 'yes'})

def download_file(path, url):
    '''
    Download and save a file from a URL.

    This function sends a GET request to a given file URL.
    If the request is successful, it downloads the file and saves it to a given path.
    If the request was redirected, it logs the final URL after redirection.
    If the request was unsuccessful, it logs a failure to download.

    In all cases, the function logs the response status code and reason.
    If an exception occurs at any point, it is caught.

    Args:
        path(str): The path to save the file to after downloading
        url(str): The URL to download the file from
    
    Returns:
        bool: True if the file was downloaded successfully, False otherwise.
    '''
    
    log.debug(f'Downloading {path} from {url}')

    try:
        # Send GET request
        response = requests.get(url, allow_redirects=True)
        
        # If request was successful, open file for writing and write content from the URL
        if response.ok:
            # Download file in 1KB chunks
            with open(path,'wb') as download:
                for chunk in response.iter_content(chunk_size = 1024):
                    if chunk:
                        download.write(chunk)
            log.debug(f'Finished downloading {path}!')
                
            # If redirect history is not empty, log redirect
            if response.history:
                log.debug(f'Download was redirected to {response.url}')

        # If request was unsuccessful, log failure
        else:
            log.debug(f'Response for {url} was not OK!')

        # Log response info and reason
        log.debug(f'Got status code {response.status_code} - {response.reason}')

        # Return True if successful, False if not
        return (response.ok)

    except:
        log.debug(f'Failed to download from {url}!')
        return False

def verify_checksum(file, checksum_correct):
    '''
    Verify a file's SHA-512 checksum is correct.

    This function calculates a file's SHA-512 checksum using the simple_file_checksum library and compares it to a known correct checksum.
    If the checksums match, the function returns True.
    Else, the function returns false.

    Args:
        file(Path): The path of the file to be verified
        checksum_correct: The known correct checksum to verify the file against

    Returns:
        bool: True if the checksums match, False if the checksums do not match
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
log.info(f'{PROGRAM_NAME} {VERSION}\nOriginal program by Pixelguin\nForked and maintained by MadMax1960\n')
if DEV:
    log.info('===! DEV IS ENABLED !===\n')

# Check for administrator elevation
try:
    is_admin = (os.getuid() == 0)
except AttributeError:
    log.debug('AttributeError thrown when using os.getuid(), trying ctypes.windll method')
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

if DEV:
    log.debug(f'[DEV] Using local {WEB_FILE}') # [DEV] Skip downloading web data and use local file
else:
    if os.path.exists(WEB_FILE):
        # Delete existing local file
        log.debug(f'{WEB_FILE} exists, deleting...')
        os.remove(WEB_FILE)  
    
    # Download new file 
    if not download_file(WEB_FILE, WEB_URL):
        fatal_error(f'Failed to download configuration data - Cannot continue!\nCheck your Internet connection and make sure you have the latest release of {PROGRAM_NAME}.')

from web_data import *

# Check if this version is supported
if version.parse(VERSION) < version.parse(web_version_supported_v2):
    fatal_error(f'This version of {PROGRAM_NAME} is too old - Cannot continue!\nDownload the latest release ({web_version_latest_v2}) at\n{web_repository}')
else:
    if version.parse(VERSION) < version.parse(web_version_latest_v2):
        log.warning(f'Version {web_version_latest_v2} of {PROGRAM_NAME} is available, but this version is still supported.\nIf something goes wrong during installation, try the latest release at\n{web_repository}\n')

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
log.info(f'''{PROGRAM_NAME} can run in Quiet Mode or Manual Mode.

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
    file = DOWNLOADS_DIR.joinpath(my_installer.get_filename())
    file_verified = False
    file_installed = False
    loop_count += 1

    # Print installer name and filename
    log.info(f'{DIVIDER}\n\n({loop_count}/{len(web_installers)}) {my_installer.name}\n')
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

        if download_file(file, my_installer.url):
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

        install_log = INSTALL_LOGS_DIR.joinpath(f'{my_installer.get_filename()}-Install.log') #Installation log
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
log.info(f'{DIVIDER}\n\nSuccessfully installed {success_count}/{len(web_installers)} prerequisite(s)!')

if restart_count > 0:
    log.warning(f'Please restart your PC to complete the installation of {restart_count} prerequisite(s).\n')

if success_count < len(web_installers):
    log.warning(f'{len(web_installers) - success_count} prerequisite(s) did not install correctly.\nTry running this program one more time in Manual Mode, and reach out for support if this message appears again.\n')
else:
    log.info('\nAll finished!')

log.info('Press Enter to end the program...')
input()
sys.exit()