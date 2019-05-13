---
title: Buy RAM
summary: Account {{ payer }} will purchase RAM for account {{ receiver }} using {{ quant }} EOS as payment.
icon: NEED TO ADD
---

This action will purchase RAM for account {{ receiver }} by using {{ quant }} EOS from account {{ payer }}.

The purchase amount of {{ quant }} EOS will have 0.5% removed as a fee, to be sent to the account `eosio.ramfee`.

The remaining portion of the purchase amount will be sent to the account `eosio.ram`.

Only the account {{ receiver }} will be able to authorize a sale of this RAM in the future, and that it is completely non-transferable.

The price of RAM is determined by the RAM market, and I, {{ payer }}, acknowledge that this price can fluctuate between time of purchase and time of sale.

{{ payer }} accepts that the quantity of RAM available in the network can be modified by the network's Block Producers.

{{ receiver }} will be unable to sell any utilized RAM until any information stored in that RAM has been freed. Ths process of freeing RAM will be subject to the terms of the other smart contracts with which {{ receiver }} will interact.

{{ receiver }} accepts that rounding errors resulting from limits of computational precision may result in less RAM being allocated.
