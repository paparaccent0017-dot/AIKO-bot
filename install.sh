#!/usr/bin/env bash
pip install --upgrade pip
pip install --only-binary=:all: pydantic-core==2.14.6
pip install -r requirements.txt