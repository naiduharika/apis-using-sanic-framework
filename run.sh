#!/bin/sh

# Server
export REQUEST_TIMEOUT=300
export RESPONSE_TIMEOUT=300

# Web
export WEB_HOST=0.0.0.0
export WEB_PORT=8000

python3 main.py
