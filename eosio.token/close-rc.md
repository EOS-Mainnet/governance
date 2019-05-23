---
spec_version: 0.1.1
title: Close
summary: Close the balance row of account {{ owner }}
icon: NEED TO ADD
---

By calling the `close` action, the RAM used to store the balance information for {{ owner }} for the token {{ symbol }} shall be freed.

The `close` action can only be executed if the balance row for {{ owner }} is 0.0000.
