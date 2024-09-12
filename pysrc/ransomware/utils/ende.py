#!/usr/bin/env python3

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
from base64 import urlsafe_b64encode
from os.path import abspath
import sys

# two arguments only
# -enc and -dec
# follow a strict rule

class EncrypterDecrypter:
    def __init__(self, args: list[str]):
        self.arguments = args
        self.plan: str = ""
    
    def analyseTask(self):
        if len(self.arguments[1:]) != 2:
            print("Invalid Arguments")
            sys.exit(1)
        else:
            # get plan
            self.plan = self.arguments[0]
    
    def carryOutTask(self):
        if self.plan == "":
            print("Execution Error")
            sys.exit(1)
        elif self.plan == "-enc":
            try:
                __kdf = PBKDF2HMAC(
                    algorithm=SHA256(),
                    length=32,
                    salt="This text is just a salt to be added into food".encode("ascii"),
                    iterations=480000,
                )
            except KeyboardInterrupt:
                print("Error creating kdf object!")
                sys.exit(1)

            try:
                __key = urlsafe_b64encode(__kdf.derive(self.arguments[2].encode("ascii")))
            except KeyboardInterrupt:
                print("Error creating key!")
                sys.exit(1)

            try:
                __fernet = Fernet(__key)
            except KeyboardInterrupt:
                print("Error creating cipher!")
                sys.exit(1)

            try:
                with open(abspath(self.arguments[1]), "rb") as file_in_bytes:
                    content = file_in_bytes.read()
            except KeyboardInterrupt:
                print("Error reading contents!")
                sys.exit(1)
            
            try:
                content = __fernet.encrypt(content)
            except Exception as e:
                print("Error encrypting file!")
                raise e

            try:
                with open(abspath(self.arguments[1]), "wb") as file_to_be_written:
                    file_to_be_written.write(content)
            except KeyboardInterrupt:
                print("Error writing encrypted data!")
                sys.exit(1)
            
        elif self.plan == "-dec":
            try:
                __kdf = PBKDF2HMAC(
                    algorithm=SHA256(),
                    length=32,
                    salt="This text is just a salt to be added into food".encode("ascii"),
                    iterations=480000,
                )
            except KeyboardInterrupt:
                print("Error creating kdf object!")
                sys.exit(1)

            try:
                __key = urlsafe_b64encode(__kdf.derive(self.arguments[2].encode("ascii")))
            except KeyboardInterrupt:
                print("Error creating key!")
                sys.exit(1)

            try:
                __fernet = Fernet(__key)
            except KeyboardInterrupt:
                print("Error creating cipher!")
                sys.exit(1)

            try:
                with open(abspath(self.arguments[1]), "rb") as file_in_bytes:
                    content = file_in_bytes.read()
            except KeyboardInterrupt:
                print("Error reading contents!")
                sys.exit(1)
            
            try:
                content = __fernet.decrypt(content)
            except Exception as e:
                raise e
            
            try:
                with open(abspath(self.arguments[1]), "wb") as file_to_be_written:
                    file_to_be_written.write(content)
            except KeyboardInterrupt:
                print("Error writing decrypted data!")
                sys.exit(1)
        else:
            print("Invalid Argument")
            sys.exit(1)

def main():
    enc_dec = EncrypterDecrypter(sys.argv[1:])
    enc_dec.analyseTask()
    enc_dec.carryOutTask()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nKEYBOARD INTERRUPT")
        sys.exit(1)