###### Setup Hyper-Grep
from global_defuns import *
import re
# Temp Vars
base_dir = '/var/app/hyper-grep'

def setup_hypergrep(base_dir):
    os_name = os_distro() 
    pip_install(hyperscan)
    if re.search(r'arch', os_name.lower()):
        aur_tool = input('Do you use a AUR Tool? If so enter the install command for your Tool. /n I.E. "pacaur -S": ')
        if len(aur_tool) > 0:
            os.system(aur_tool + " hyperscan-git")
############# 
    elif re.search(r'(fedora 30|fedora 29|fedora 28)', os_name.lower()):
        yum('hyperscan')
############# 
    elif re.search(r'(ubuntu 19|ubuntu 18)', os_name.lower()):
        apt('hyperscan')
    elif re.search(r'(debian gnu/linux 9|debian gnu/linux 10)', os_name.lower()):
        apt('libhyperscan5')
############# 
    elif re.search(r'(centos)', os_name.lower()):

    else: 
        sys.exit('Automated package installs for ' + os_name + ' are not yet supported.')
    ### 

