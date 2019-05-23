---
title: Undelegate Bandwidth
summary: Undelegate {{ unstake_cpu_quantity }} CPU and {{ unstake_net_quantity }} Network bandwidth from account {{ receiver }}
icon: NEED TO ADD
--- 

As an authorized party I, {{ signer }}, wish to unstake {{ unstake_cpu_quantity }} from CPU and {{ unstake_net_quantity }} from Network bandwidth from the tokens owned by {{ from }} previously delegated for the use of delegatee {{ receiver }}. 

I acknlowedge that I do not expect to have access to these tokens until at least 72 hours have passed since calling the `undelegatebw` action.

The CPU and Network bandwidth resources that have been unstaked will be immediately revoked from {{ receiver }}. Any voting weights based on staked resources will become immediately effected. 

If I, {{ signer }} am not the beneficial owner of these tokens I stipulate I have been authorized to take this action by their beneficial owner(s). 
