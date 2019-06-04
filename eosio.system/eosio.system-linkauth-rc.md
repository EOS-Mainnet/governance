---
spec_version: 0.1.1
title: Link Authority
summary: Link permission authority {{ requirement }} of account {{ account }} to a specific contract's action
icon: NEED TO ADD
---

I, {{ signer }}, wish to link the permission authority {{ requirement }} of {{ account }} to the action {{ type }} of the smart contract {{ code }}.

I can only remove this link by calling the `unlinkauth` action, and will need to do so before being able to call `deleteauth`.

I can specify a specific action from contract {{ code }}, or I can use a wildcard to link all actions within a contract to the authority {{ requirement }}. If new actions are added to contract {{ code }}, my account {{ account }} will be able to call those new actions.

I acknowledge that I cannot use `linkauth` for the following actions: `updateauth`, `deleteauth`, `linkauth`, `unlinkauth`, and `canceldelay`.
