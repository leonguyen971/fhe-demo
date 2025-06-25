# test_encrypt.py

from encrypt import encrypt

def test_encrypt():
    assert encrypt("test") == "<enc>test</enc>"
