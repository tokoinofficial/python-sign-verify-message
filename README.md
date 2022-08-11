# sign-verify-message

This repos shows the way to sign/verify an ethereum message. It's used for backend of third party where interacts with Tokoin Payment System.

### Tokoin Payment System [WIP]

### How to use
- Sign message
```python
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
```

- Verify message
```python
def verify(from_address='', types=[], values=[], signature=None):
    assert (is_address(from_address)
            is True and signature is not None)
    hash = Web3.soliditySha3(
        types,
        values,
    )
    message = encode_defunct(bytes(hash))
    return from_address == w3.eth.account.recover_message(message, signature=signature)

```

### How to run sample
- pip3 install virualenv
- virtualenv .venv
- source .venv/bin/activate
- pip3 install -r requirements.txt
- python3 main.py

### Demo
- [x] golang (https://github.com/tokoinofficial/go-sign-verify-message)
- [x] python

### Created & Maintained By

[Trong Dinh](https://github.com/trongdth)
