#!/bin/bash
curl -so /dev/null -Iw "%{http_code}" $@
