###### Setup Hyper-Grep
from global_defuns import *

base_dir = '/var/app/hyper-grep'

def setup_hypergrep(base_dir):
    os_name = os_distro() 
    pip_install(hyperscan)
    if 'arch' in os_name.lower():
        aurman_install('boost ragel cmake python2 hyperscan')
#</# 
# still need to figure outout how to build hyperscan on each flavor
        #  pacman('boost ragel cmake python2')
        #  os.system('cd ' + base_dir + '/core/hyperscan & ' + )
    #  elif 'debian' or 'ubuntu' in os_name.lower():
        #  apt('boost ragel cmake python2')
        #  os.system('cd ' + base_dir + '/core/hyperscan & ' + )
    #  elif 'fedora' or 'redhat' in os_name.lower():
        #  yum('boost ragel cmake python2')
        #  os.system('cd ' + base_dir + '/core/hyperscan & ' + )
#/>#
    else: 
        sys.exit('Automated package installs for ' + os_name + ' are not yet supported.')
    ### 

