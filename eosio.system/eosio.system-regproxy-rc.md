---
spec_version: 0.1.1
title: Register Proxy
summary: Register account {{ proxy }} as a proxy
icon: NEED TO ADD
---

As an authorized party I, {{ signer }}, would like to register the account {{ proxy }} as a proxy by having the {{ isproxy }} value updated to `1`.

As a proxy, the vote weight of all accounts who proxy to {{ proxy }} will be delegated along with its own. For all proposals created within `eosio.forum`, their vote weight will also be delegated to {{ proxy }}, unless that account chooses to cast their own vote for a proposal.
