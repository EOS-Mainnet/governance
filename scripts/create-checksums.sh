#!/bin/bash

# Create sha256 checksums
shasum -a 256 \
  ./eosio.system/eosio.system.abi \
  ./eosio.token/eosio.token.abi > checksums.txt
