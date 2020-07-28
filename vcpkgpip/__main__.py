import os
import sys
from pathlib import Path
from subprocess import check_call


def bootstrap():
    root      = Path(os.path.dirname(os.path.abspath(__file__)))
    vcpkg     = root / "vcpkg"
    bootstrap = vcpkg / "bootstrap-vcpkg.bat"
    try:
        check_call(f"git clone https://github.com/microsoft/vcpkg {vcpkg}".split())
    except:
        print('git is not installed')
    check_call(f"{bootstrap}".split())

def main():
    root      = Path(os.path.dirname(os.path.abspath(__file__)))
    vcpkg     = root / "vcpkg" / "vcpkg"
    os.system(f'{vcpkg} {" ".join(sys.argv[1:])}')