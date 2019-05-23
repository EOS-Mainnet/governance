---
spec_version: 0.1.1
title: Delegate Bandwidth
summary: {{ from }} stakes EOS tokens for the account {{ receiver }}, {{ stake_net_quantity }} for Network and {{ stake_cpu_quantity }} for CPU
icon: NEED TO ADD
---

As an authorized party I, {{ signer }}, wish to stake {{ stake_net_quantity }} EOS for Network and {{ stake_cpu_quantity }} EOS for CPU from the liquid tokens of {{ from }} for the use of {{ receiver }}.

By including the `--transfer` flag, {{ from }} would like to permanently transfer the tokens to {{ receiver }} and not just temporarily delegate their resources.

I understand that should I wish to unstake these tokens and relinquish the claim on resources that I shall be restricted by the wait period as described in `undelegatebw`.
