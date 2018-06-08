#!/bin/bash

# Upload to ipfs
ipfs add ./eosio.system/eosio.system.abi > ipfs.txt
ipfs add ./eosio.token/eosio.token.abi >> ipfs.txt

