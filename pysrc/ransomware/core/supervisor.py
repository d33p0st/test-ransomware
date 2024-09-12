from .runtime import Runtime

from multiprocessing import Process
import subprocess, os, time

class Supervisor:
    def __init__(self, directories: list[str] = [os.getcwd()], types: list[str] = []):
        self.d = directories
        self.t = types

        # define commands
        encrypt = f"rw --start-runtime --directories {' '.join(self.d)} --types {' '.join(self.t)}"
        decrypt = f"rw --rec --directories {' '.join(self.d)} --types {' '.join(self.t)}"

        # define osascripts
        self.encrypt_script = f"""
        tell application "Terminal"
            do script "{encrypt}"
        end tell
        """

        self.decrypt_script = f"""
        tell application "Terminal"
            do script "{decrypt}"
        end tell
        """
    
    @property
    def launch(self):
        subprocess.run(['osascript', '-e', self.encrypt_script])
    
    @property
    def recover(self):
        subprocess.run(['osascript', '-e', self.decrypt_script])
    
    @property
    def running(self) -> bool:
        ps = subprocess.run(['ps', '-A'], capture_output=True, text=True)
        return "rw --start-runtime" in ps.stdout
    
    @property
    def launch_and_protect(self):
        while True:
            if not self.running:
                print(". Starting,")
                self.launch
            else:
                print(". Running,")
            
            time.sleep(7)

def selfstart(directories: list[str] = [os.getcwd()], types: list[str] = []):
    superviser = Supervisor(directories=directories, types=types)
    self = Process(target=superviser.launch_and_protect)
    self.start()

def recover(directories: list[str] = [os.getcwd()], types: list[str] = []):
    supervisor = Supervisor()
    supervisor.recover