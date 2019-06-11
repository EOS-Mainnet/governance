---
spec_version: 0.1.1
title: Set Code
summary: Set the contract code for account {{ account }}
icon: NEED TO ADD
---

As an authorized party I, {{ signer }}, would like to set the Smart Contract file corresponding to the sha256 hash {{ code }} to the account {{ account }}.
The ABI data will be stored in the RAM of {{ account }}.

When calling `setcode`, I shall produce suitable Ricaridan Contracts within the ABI file when calling `setabi` for the account {{ account }}.