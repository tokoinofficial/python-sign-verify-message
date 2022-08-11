#!/usr/bin/python
# -*- coding: utf-8 -*-
from web3 import Web3
from web3.auto import w3
from eth_account.messages import encode_defunct
from eth_utils import is_address, is_hex

import web3


def sign(pk='', types=[], values=[]):
    '''
        - Web3.py only accepts checksum addresses
    '''
    assert (is_hex(pk) is True)
    hash = Web3.soliditySha3(
        types,
        values,
    )
    message = encode_defunct(bytes(hash))
    signed_message = w3.eth.account.sign_message(
        message, private_key=pk)
    return signed_message.signature


def verify(from_address='', types=[], values=[], signature=None):
    assert (is_address(from_address)
            is True and signature is not None)
    hash = Web3.soliditySha3(
        types,
        values,
    )
    message = encode_defunct(bytes(hash))
    return from_address == w3.eth.account.recover_message(message, signature=signature)
