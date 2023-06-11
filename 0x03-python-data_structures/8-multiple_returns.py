#!/usr/bin/python3
def multiple_returns(sentence):
    strLen = len(sentence)
    first = sentence[0]
    if strLen == 0:
        first = None
    return (strLen, first)
