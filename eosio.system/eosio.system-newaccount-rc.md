---
title: Create New Account
summary: Account {{ creator }} creates the account {{ name }}.
icon: NEED TO ADD
---

The `newaccount` action creates a new account.

As an authorized party I, {{ signer }}, wish to exercise the authority of {{ creator }} to create a new account on this blockchain named {{ name }}, such that the new account's `owner` permission's public key shall be {{ owner }} and the `active` permission's public key shall be {{ active }}.

The account name {{ name }} must conform to the standards of only utilizing lowercase characters `a` through `z`, and `1` through `5`. 

Should there be a `.` in {{ name }}, then only the account who has won the `bidname` auction for that suffix may call the `newaccount` action.

Should the account name {{ name }} be fewer than 12 characters and not contain a `.`, the `newaccount` action may only be called by the winner of the `bidname` auction for that suffix by using the same account that cast the winning bid.
