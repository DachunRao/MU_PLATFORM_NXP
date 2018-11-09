##
## Script to Build Ivanhoe UEFI firmware
##
##
## Copyright Microsoft Corporation, 2018
##
import os, sys
from MuEnvironemnt import CommonBuildEntry

#
#==========================================================================
# PLATFORM BUILD ENVIRONMENT CONFIGURATION
#
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_PATH = os.path.dirname(os.path.dirname(SCRIPT_PATH))
REQUIRED_REPOS = ('MU_BASECORE','Silicon/ARM/NXP', 'Common/MU','Common/MU_TIANO', 'Silicon/ARM/MU_TIANO')
PROJECT_SCOPE = ('imxfamily', 'imx8')

MODULE_PKGS = ('MU_BASECORE','Silicon/ARM/NXP', 'Common/MU','Common/MU_TIANO', 'Silicon/ARM/MU_TIANO')
MODULE_PKG_PATHS = os.pathsep.join(os.path.join(WORKSPACE_PATH, pkg_name) for pkg_name in MODULE_PKGS)
#
#==========================================================================
#

# Smallest 'main' possible. Please don't add unnecessary code.
if __name__ == '__main__':

  # Now that we have access to the entry, hand off to the common code.
  CommonBuildEntry.build_entry(SCRIPT_PATH, WORKSPACE_PATH, REQUIRED_REPOS, PROJECT_SCOPE, MODULE_PKGS, MODULE_PKG_PATHS)
