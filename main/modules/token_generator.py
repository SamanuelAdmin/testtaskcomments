import random


def generateToken(lenth=16):
    allowedSymbols = 'ABCDEFJHIGKLMNOPQRSTUVWXYZ'
    allowedSymbols += allowedSymbols.lower()

    return ''.join(random.choice(allowedSymbols) for _ in range(lenth))