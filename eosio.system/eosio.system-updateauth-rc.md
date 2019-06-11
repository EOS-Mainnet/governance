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

