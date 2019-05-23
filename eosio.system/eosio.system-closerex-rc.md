---
spec_version: 0.1.1
title: Close Rex
summary: Free up any REX-related database entries in RAM from the account {{ owner }} 
icon: NEED TO ADD
---

The `closerex` action allows an account to delete unused REX-related database entries and frees occupied RAM associated with its storage.

As an authorized party, I {{ signer }}, wish to delete all unused REX-related database entries from the account {{ owner }}.

I will not be able to succesfully call `closerex` unless all checks for CPU loans, NET loans or refunds pending refunds are still processing on the account {{ owner }}.
