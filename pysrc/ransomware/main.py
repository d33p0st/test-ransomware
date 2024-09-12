from .core.supervisor import selfstart, recover, Runtime
from .utils.arguments import Arguments
from .utils.helptext import HelpText

import sys

__version__ = "0.1.0"

def main():
    arguments = Arguments().get
    fetchtype = Arguments().fetchtypes

    if arguments.__there__("--help"):
        print(HelpText.text.format(__version__))
        sys.exit(0)

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
