#!/usr/bin/python
# -*- coding: utf-8 -*-
from web3 import Web3
from helpers.eth_message import sign, verify

if __name__ == "__main__":
    # sign message
    types = ["address", "uint256"]
    values = [Web3.toChecksumAddress(
        '0x45f7967926e95fd161e56ed66b663c9114c5226f'), 4685]
    signature = sign(
        "0x16870e97136d178735994d9ed537742276db9f30d80b2b35a05a798895679049", types, values)
    print(signature)

    # verify message
    print(verify('0xfE91b1E07b93fdfae1E02A985266fA3414aB844A', types, values, signature))
