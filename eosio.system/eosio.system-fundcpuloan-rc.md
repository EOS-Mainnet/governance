---
spec_version: 0.1.1
title: Fund CPU Loan
summary: Assign {{ payment }} EOS tokens for the renewal of CPU loan {{ loan_num }} upon expiry.
icon: NEED TO ADD
---

The `fundcpuloan` action allows an account to transfer tokens from its REX fund to the fund of a specific CPU loan in order for those tokens to be used for loan renewal at the loan's expiry.

As an authorized party I, {{ signer }}, wish to transfer the amount of {{ payment }} tokens into the CPU loan fund of the loan identified by loan number {{ loan_num }} from the account {{ from }} to be used for loan renewal at the expiry of {{ loan_num }}.
