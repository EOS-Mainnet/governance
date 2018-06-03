#!/bin/bash

# Import RC markdown directly to ABIs

# eosio.token
python3 scripts/ricardeos/ricardeos.py import \
  eosio.token/eosio.token.abi \
  eosio.token/eosio.token.abi

# eosio.system
python3 scripts/ricardeos/ricardeos.py import \
  eosio.system/eosio.system.abi \
  eosio.system/eosio.system.abi
