#!/usr/bin/env bash

# TODO: Fix the CfP script for 2020.

sed -i 's/"duration": 120,/"duration": 110,/' talks.json
sed -i 's/"duration": 55,/"duration": 50,/' talks.json
sed -i 's/"duration": 25,/"duration": 20,/' talks.json
