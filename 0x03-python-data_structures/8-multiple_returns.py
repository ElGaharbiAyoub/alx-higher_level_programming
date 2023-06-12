#!/usr/bin/python3
def multiple_returns(sentence):
    strLen = len(sentence)
    if strLen <= 0:
        strLen = 0
        return (strLen, None)
    return (strLen, sentence[0])
