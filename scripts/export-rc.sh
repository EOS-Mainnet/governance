#!/bin/bash

# Export RC markdown directly from ABIs

# eosio.token
python3 scripts/ricardeos/ricardeos.py export \
  eosio.token/eosio.token.abi

# eosio.system
python3 scripts/ricardeos/ricardeos.py export \
  eosio.system/eosio.system.abi
