# Action - `sellrex`

## Description

The `sellrex` action allows an account to sell REX tokens held by the account.

As an authorized party I, {{ signer }}, wish to sell {{ rex }} REX tokens held on the account {{ from }} in exchange for core EOS tokens. If there is an insufficient amount of EOS tokens available at this time, I acknowledge that my order will be placed in a queue to be processed. 

If there is an open `sellrex` order for the account {{ from }}, then this amount of {{ rex }} REX shall be added to the existing order and the order shall move to the back of the queue. 
