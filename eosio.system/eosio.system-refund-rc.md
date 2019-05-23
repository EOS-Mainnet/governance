---
spec_version: 0.1.1
title: Refund
summary: Manually trigger a refund after the undelegation period for account {{ owner }}
icon: NEED TO ADD
---

The `refund` action will manually trigger a return of EOS tokens that should have been automatically allocated from `eosio.stake` to {{ owner }} at the end of the 72-hour undelegation period after calling `undelegatebw`. 

As an authorized party I, {{ signer }}, wish to have the any unstaked tokens due to {{ owner }} returned as liquid EOS tokens into the account {{ owner }}.
