---
spec_version: 0.1.1
title: Buy RAM Bytes
summary: Account {{ payer }} will purchase {{ bytes }} bytes of RAM for account {{ receiver }}
icon: NEED TO ADD
---

This action will purchase {{ bytes }} bytes of RAM for account {{ receiver }} by using EOS tokens from account {{ payer }}, at the rate determined by the system's RAM market.

There will be a fee of 0.5% added to the purchase price determined by the system's RAM market. This fee will be sent to the account `eosio.ramfee`.

Only the account {{ receiver }} will be able to authorize a sale of this RAM in the future, and that it is completely non-transferable.

The price of RAM is determined by the RAM market, and I, {{ payer }}, acknowledge that this price can fluctuate between time of purchase and time of sale.

{{ payer }} accepts that the quantity of RAM available in the network can be modified by the network's Block Producers.

{{ receiver }} will be unable to sell any utilized RAM until any information stored in that RAM has been freed. Ths process of freeing RAM will be subject to the terms of the other smart contracts with which {{ receiver }} will interact.

{{ receiver }} accepts that rounding errors resulting from limits of computational precision may result in less RAM being allocated.
