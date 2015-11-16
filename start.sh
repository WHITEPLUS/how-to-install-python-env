#! /usr/bin/env bash

python ./flask_sample.py&

sleep 1

open http://localhost:9123

wait