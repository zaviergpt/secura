
import os
import sys
import time

class Secura:

    def __init__(self):
        filename = "main.py"
        text = list(open(filename, "r").read())
        hashed = self.hashed(text, 32)
        key = self.key(input("\nPassword: "))
        os.system("cls")
        selected = input("\nFile Selected: {}\n\nYour options ([E]ncrypt, [D]ecrypt): ".format(filename)).lower()
        print("")
        if selected == "e":
            encrypted = self.encrypt(text, key, hashed)
            for index, character in enumerate(encrypted):
                sys.stdout.flush()
                sys.stdout.write(character)
                time.sleep(1/(len(encrypted)-index))
        elif selected == "d":
            decrypted = self.decrypt(encrypted, key, hashed)

    def encrypt(self, text, key, hashed):
        result = []
        while len(key) < len(text):
            key.extend(key)
        while len(hashed) < len(text):
            hashed.extend(hashed)
        for index, character in enumerate(text):
            result.append(chr(ord(character) ^ (key[index] ^ hashed[index])))
        return result

    def decrypt(self, text, key, hashed):
        result = []
        while len(key) < len(text):
            key.extend(key)
        while len(hashed) < len(text):
            hashed.extend(hashed)
        for index, character in enumerate(text):
            result.append(chr(ord(character) ^ (key[index] ^ hashed[index])))
        return result

    def hashed(self, text, length=(2 ** 5)):
        periods = {}
        for index, character in enumerate(text):
            period = round((index/len(text)) * length)
            if periods.get(period) is None:
                periods[period] = []
            periods[period].append(ord(character))
        return [int(str(round(sum(period[1])/len(period[1])))[-1]) for period in periods.items()]

    def key(self, text):
        return [int(str(ord(character))[-1]) for character in text]

if __name__ in "__main__":
    Secura()
