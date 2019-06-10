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

---
spec_version: 0.1.1
title: Set ABI
summary: Set an ABI file on the account {{ acnt }}
icon: NEED TO ADD
---

As an authorized party I, {{ signer }}, would like to set the ABI file corresponding to the sha256 hash {{ abi }} to the account {{ acnt }}.
The ABI data will be stored in the RAM of {{ acnt }}.

---
spec_version: 0.1.1
title: Set Code
summary: Set the contract code for account {{ account }}
icon: NEED TO ADD
---

As an authorized party I, {{ signer }}, would like to set the Smart Contract file corresponding to the sha256 hash {{ code }} to the account {{ account }}.
The ABI data will be stored in the RAM of {{ acnt }}.

When calling `setcode`, I shall produce suitable Ricaridan Contracts within the ABI file when calling `setabi` for the account {{ account }}.

---
spec_version: 0.1.1
title: Unlink Authority
summary: Unlink authority for {{ code }}::{{ type }} on account {{ account }}
icon: NEED TO ADD
---

As an authorized party I, {{ signer }}, would like to unlink the authority attached to {{ code }}::{{ type }} for the account {{ account }}.
This will remove any restrictions that may have previously existed for other authority permission's of {{ account }} to call {{ code }}::{{ type }}.

---
spec_version: 0.1.1
title: Update Authroity
summary: Update the authority structure of {{ account }} by adding the permission {{ permission }}
icon: NEED TO ADD
---

As an authorized party I, {{ signer }}, wish to add the new authority permission {{ permission }}, which will be a child to the permission
{{ parent }}. The authority of permission {{ permission }} shall match the provided information in {{ auth }}. 

The authority {{ permission }} will not be able to call any actions linked specifically to any authorities to which it is a child of, or
a sibling to.

