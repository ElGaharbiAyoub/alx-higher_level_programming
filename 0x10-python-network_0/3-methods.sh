#!/bin/bash
curl -sI $@ | grep -i Allow | cut -d ' ' -f2-
