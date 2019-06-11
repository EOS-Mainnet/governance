---
spec_version: 0.1.1
title: Remove Producer
summary: Remove {{ producer }} from the list of Block Producer Candidates
icon: NEED TO ADD
---

The `rmvproducer` action can only be executed with the authority of `eosio.prods`. As such, it takes approval of a multisig proposal
by 15 of the top 21 Block Producers. While they will not call this action directly themselves, this the description of what they are agreeing to.
The `rmvproducer` action should only be called if the rules described within the `regproducer` Ricardian are followed.

By executing the `rmvproducer` action, the account {{ producer }} will no longer be considered a Block Producer Candidate. Any votes
that they have received will still be attached to their account, but they will be unable to call `claimrewards` or produce any blocks
until such time that they have successfully called `regproducer` again.

Before approving the multisig proposal to execute the `rmvproducer` action, the requested actor stipulates that they will only do so with
the best interests of the blockchain in mind, and not for any malicious purpose. The requested actors shall adhere to guidelines found 
within `regproducer`, or any other governing documents which may make reference to `rmvproducer`.