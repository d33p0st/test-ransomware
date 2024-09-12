from .core.supervisor import selfstart, recover, Runtime
from .utils.arguments import Arguments

import sys

def main():
    arguments = Arguments().get
    fetchtype = Arguments().fetchtypes

    if arguments.__there__('--directories'):
        directories = arguments.__fetch__('--directories', fetchtype.TILL_NEXT)
    else:
        print("-err: --directories is a mandatory field.")
        sys.exit(1)
    
    if arguments.__there__("--types"):
        types = arguments.__fetch__("--types", fetchtype.TILL_NEXT)
    else:
        types = []
    
    if arguments.__there__("--start"):
        selfstart(directories=directories, types=types)
    elif arguments.__there__("--recover"):
        recover(directories=directories, types=types)
    elif arguments.__there__("--start-runtime"):
        runtime = Runtime(directories=directories, types=types)
        runtime.start()
    elif arguments.__there__("--rec"):
        runtime = Runtime(directories=directories, types=types)
        runtime.recover()
    