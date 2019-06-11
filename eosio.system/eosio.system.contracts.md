---
spec_version: 0.1.1
title: Bidname
summary: Place a bid of {{ bid }} EOS by account {{ bidder }} on the account name {{ newname }}
icon: NEED TO ADD
---

As an authorized party I, {{ bidder }}, wish to bid the amount of {{ bid }} toward purchase of the account name {{ newname }}.

I am aware that I cannot revoke my bid of {{ bid }} EOS. I will only receive it back if I am outbid by at least 10% by another user. 

My bid of {{ bid }} EOS for the account name {{ newname }} will only be awarded if it holds the highest bid for any new account name, for a period of consecutive 24 hours.

---
spec_version: 0.1.1
title: Buy RAM
summary: Account {{ payer }} will purchase RAM for account {{ receiver }} using {{ quant }} EOS as payment
icon: NEED TO ADD
---

This action will purchase RAM for account {{ receiver }} by using {{ quant }} EOS from account {{ payer }}.

The purchase amount of {{ quant }} EOS will have 0.5% removed as a fee, to be sent to the account `eosio.ramfee`.

The remaining portion of the purchase amount will be sent to the account `eosio.ram`.

Only the account {{ receiver }} will be able to authorize a sale of this RAM in the future, and that it is completely non-transferable.

The price of RAM is determined by the RAM market, and I, {{ payer }}, acknowledge that this price can fluctuate between time of purchase and time of sale.

{{ payer }} accepts that the quantity of RAM available in the network can be modified by the network's Block Producers.

{{ receiver }} will be unable to sell any utilized RAM until any information stored in that RAM has been freed. Ths process of freeing RAM will be subject to the terms of the other smart contracts with which {{ receiver }} will interact.

{{ receiver }} accepts that rounding errors resulting from limits of computational precision may result in less RAM being allocated.

---
spec_version: 0.1.1
title: Buy RAM Bytes
summary: Account {{ payer }} will purchase {{ bytes }} bytes of RAM for account {{ receiver }}
icon: NEED TO ADD
---

This action will purchase {{ bytes }} bytes of RAM for account {{ receiver }} by using EOS tokens from account {{ payer }}, at the rate determined by the system's RAM market.

There will be a fee of 0.5% added to the purchase price determined by the system's RAM market. This fee will be sent to the account `eosio.ramfee`.

Only the account {{ receiver }} will be able to authorize a sale of this RAM in the future, and that it is completely non-transferable.

The price of RAM is determined by the RAM market, and I, {{ payer }}, acknowledge that this price can fluctuate between time of purchase and time of sale.

{{ payer }} accepts that the quantity of RAM available in the network can be modified by the network's Block Producers.

{{ receiver }} will be unable to sell any utilized RAM until any information stored in that RAM has been freed. Ths process of freeing RAM will be subject to the terms of the other smart contracts with which {{ receiver }} will interact.

{{ receiver }} accepts that rounding errors resulting from limits of computational precision may result in less RAM being allocated.

---
spec_version: 0.1.1
title: Buy REX
summary: Exchange {{ amount }} EOS from the REX fund of {{ from }} account for REX tokens
icon: NEED TO ADD
---

The `buyrex` action allows an account to exchange EOS tokens from their REX fund for REX tokens.

As an authorized party I, {{ signer }}, wish to buy REX on the account {{ from }} with {{ amount }} EOS.

I am aware of, and have fulfilled, all voting requirements needed to participate in the REX marketplace.

I am aware that I will need to satify the maturing period before being able to transfer these REX tokens back into EOS tokens.

---
spec_version: 0.1.1
title: Cancel Delay
summary: Cancel a pending deferred transaction with ID {{ trx_id }}
icon: NEED TO ADD
---

As an authorized party I, {{ signer }}, wish to invoke the authority of {{ canceling_auth }} to cancel the transaction with ID {{ trx_id }}.

---
spec_version: 0.1.1
title: Claim Rewards
summary: Claim Block Rewards and Vote Rewards due to Block Producer {{ owner }} 
icon: NEED TO ADD
---

As an authorized party I, {{ signer }}, wish to have the rewards earned by {{ owner }} deposited into the account {{ owner }}.

By calling the `claimrewards` action, I, {{ owner }} agree to abide by any and all rules described in the Constitution, or any other governing documents, that are in effect at this time.

---
spec_version: 0.1.1
title: EOS User Agreement
summary: EOS User Agreement
icon: NEED TO ADD
---

# EOS User Agreement

## Definitions

 All capitalized, italicized, or inline code terms in *The EOS User Agreement* will be given the same effect and meaning as in *Definitions*.

* EOS User Agreement: This document (*EUA*)

* Chain ID: `chain_id` - aca376f206b8fc25a6ed44dbdc66547c36c6c33e3a119ffbeaef943642f0e906

* User: Any person or organization of persons who maintain(s) direct or indirect ownership of an EOS account, or EOS-based property connected to an EOS account.

* Ownership: Direct or indirect access to an EOS account through one or more valid permissions checks. Ownership may be partially shared between Users through the use of multi-signature permissions.

* Block Producer: Users who have called `regproducer` and receive rewards from eosio.vpay.

* `eosio.prods`: An EOS account with a dynamic permissions structure that can assume the privileges of the `eosio` account when 15/21 Block Producers agree to do so.

* Network Funds: Tokens contained within the following accounts: `eosio.names`, `eosio.ramfee`, `eosio.saving`.

* Governing Documents: *regproducer* is considered a governing document.

* On-Chain: Any transaction, smart contract, or Ricardian contract which is located within a block that is irreversible and appended to the EOS blockchain `chain_id`.

* EOS-based Property: Anything that requires a valid permission in order to directly manipulate, alter, transfer, influence, or otherwise effect on the EOS Blockchain 

* Call: To submit an action to the EOS Blockchain `chain_id`.

* Authorizations & Permissions: Permissions are arbitrary names used to define the requirements for a transaction sent on behalf of that permission. Permissions can be assigned for authority over specific contract actions.

* Ricardian Contract: A contract that places the defining elements of a legal agreement in a format that can be expressed and executed in software.

## Article I -  User Acknowledgement of Risks 
If User loses access to their EOS account on `chain_id` and has not taken appropriate measures to secure access to their EOS account by other means, the User acknowledges and agrees that that EOS account will become inaccessible. Users acknowledge that the User has an adequate understanding of the risks, usage and intricacies of cryptographic tokens and blockchain-based software. The User acknowledges and agrees that the User is using the EOS blockchain at their sole risk.

## Article II - Special User Types
Users who call `regproducer` agree to, and are bound by, the *regproducer* Ricardian Contract.

## Article III - Consent of the EUA
The nature of the *EOS User Agreement* is such that it serves as a description of the current EOS Mainnet governance functions that are in place. These functions, enforced by code, do not require the consent of Users as these functions are inherent and systemic to the EOS Mainnet itself.

## Article IV - Governing Documents
Any modifications to the *EUA* and *governing documents* may be made by `eosio.prods`. It is admonished that a statement be crafted and issued through `eosio.prods` via eosio.forum referendum contract describing such a modification in advance.

## Article V - Native Unit of Value
The native unit of value on EOS chain_id shall be the EOS token as defined and created by the `eosio.token` smart contract.

## Article VI - Maintaining the EOS blockchain
`eosio.prods` will maintain the active blockchain codebase which includes, but is not limited to, the implementation of all modifications of all features, optimizations, and upgrades: present and future. 

## Article VII - Network Funds
It is admonished that any altering of the state of any tokens contained within network fund accounts, or altering any pre-existing code that directly or indirectly governs the allocation, fulfillment, or distribution of any *network funds* be preceded by a statement crafted and issued by `eosio.prods` to the *eosio.forum* referendum system contract describing the effect in advance.

## Article VIII - Freedom of Account Creation
Any current or future User is able to create an EOS Account without the permission by any other User. `eosio.prods` may never affect an EOS User Account(s) without valid permission(s) which have been shared with `eosio.prods` by an EOS account. `eosio.prods` may charge a fee for any actions that are requested by other Users pertaining to an EOS account where permissions are shared. 

## Article IX - No Fiduciary
No User shall have a fiduciary purpose to support the value of the EOS token. No User can authorize anyone to hold assets, borrow, speak, contract on behalf of other EOS Users or the EOS blockchain `chain_id` collectively. This EOS blockchain shall have no owners, managers, or fiduciaries.

## Article X - User Security
All items pertaining to personal account security, including but not limited to the safekeeping of private keys, is solely the responsibility of the User to secure. 

## Article XI - `eosio.prods` Limited Liability
The User acknowledges and agrees that, to the fullest extent permitted by any applicable law, this disclaimer of liability applies to any and all damages or injury whatsoever caused by or related to risks of, use of, or inability to use, the EOS token or the EOS blockchain `chain_id` under any cause of action whatsoever of any kind in any jurisdiction, including, without limitation, actions for breach of warranty, breach of contract or tort (including negligence) and that `eosio.prods`, nor the individual permissions that operate it, shall not be liable for any indirect, incidental, special, exemplary or consequential damages, including for loss of profits, goodwill or data. 

# EOS 사용자 동의서

## 정의

EOS 사용자 동의서의 모든 대문자, 기울임 꼴, 또는 인라인 코드 용어는 정의에서와 동일한 효과와 의미가 부여됩니다.

-   EOS 사용자 동의서: 본 문서 (EUA)
-   체인 ID: chain_id --- aca376f206b8fc25a6ed44dbdc66547c36c6c33e3a119ffbeaef943642f0e906
-   사용자: EOS 계정을 직접 또는 간접적으로 소유하거나 EOS 계정에 연결된 EOS 기반 속성을 유지하거나 관리하는 사람, 조직, 또는 조직의 모든 사람.
-   소유권: 하나 이상의 유효한 사용권한 확인을 통해 EOS 계정에 직접 또는 간접적으로 접근합니다. 소유권은 다중 서명권한을 사용하여 사용자간에 부분적으로 공유 될 수 있습니다.
-   블록 프로듀서: regproducer를 실행하고 eosio.vpay로부터 보상을 받는 사용자.
-   eosio.prods: 15/21 블록 프로듀서들이 동의 할 때 eosio 계정의 권한을 가질 수 있는 동적 권한 구조를 가진 EOS 계정.
-   네트워크 자금: 다음 계정에 포함 된 토큰: eosio.names, eosio.ramfee, eosio.saving.
-   관리 문서: regproducer는 관리 문서로 간주됩니다.
-   온체인: EOS 블록체인 chain_id에 비가역적이며 추가 할 수 있는 블록 내에 위치한 모든 거래, 스마트 계약 또는 리카르디안 계약.
-   EOS 기반 속성: EOS 블록체인을 직접 조작, 변경, 전송, 영향 또는 달리 적용하기 위해 유효한 사용 권한이 필요한 모든 것
-   콜: EOS 블록체인 chain_id에 작업을 신청하는 것.
-   허가 및 권한: '허가'는 해당 권한을 대신하여 전송되는 트랜잭션의 요구사항을 정의하는 데 사용됩니다. '권한'은 특정 계약 조치에 대한 권한을 부여합니다.
-   리카르디안 계약: 합법적 계약의 정의 요소를 소프트웨어로 표현하고 실행할 수 있는 형식으로 배치하는 계약.

## 제 1조 --- 위험에 대한 사용자들의 인지

사용자가 chain_id에서 EOS 계정에 대한 접근 권한을 잃고, 다른 방법으로 EOS 계정에 대한 접근을 보호하기 위해 적절한 조치를 취하지 않는 경우에는 EOS 계정에 접근할 수 없게 된다는 것을 인정하고 동의합니다. 사용자는 암호화 토큰과 블록체인 기반 소프트웨어의 위험, 사용법, 그리고 복잡성에 대해 충분히 이해하고 있음을 인정합니다. 사용자는 EOS 블록체인의 사용에 대한 전적인 책임을 진다는 것에 인정하고 동의합니다.

## 제 2조 --- 특별한 사용자 유형

regproducer를 실행하는 사용자는 regproducer 리카르디안 계약에 동의하고, 이에 구속됩니다.

## 제 3조 --- EUA의 동의

EOS 사용자 동의서는 현재 시행중인 EOS 메인넷 거버넌스에 대한 설명으로 사용됩니다. 코드에 의해 시행되는 이러한 기능은 EOS 메인넷 자체의 체계적이고 고유한 기능이므로 사용자의 동의를 필요로 하지 않습니다.

## 제 4조 --- 관리 문서

EUA와 관리 문서는 eosio.prods를 통해 수정이 가능합니다. 특정 변경사항을 사전에 설명하는 eosio.forum 투표 계약을 통해 eosio.prods가 성명서를 작성하고 발급할 것을 권고합니다.

## 제 5조 --- 가치의 기본 단위

EOS chain_id의 기본 단위는 eosio.token 스마트 계약에 의해 정의되고 작성된 EOS 토큰입니다.

## 제 6조 --- EOS 블록체인 유지

eosio.prods는 모든 기능, 최적화, 그리고 업그레이드의 현재와 미래의 모든 수정사항을 구현하는 것을 포함하되, 이에 국한되지 않는 활성화된 블록체인 코드베이스를 유지합니다

## 제 7조 --- 네트워크 자금

네트워크 자금 계정에 포함된 토큰의 상태를 변경하거나, 네트워크 자금의 배분, 이행, 또는 배포를 직/간접적으로 관리하는 기존 코드를 변경하는 경우에는 eosio.prods를 eosio.forum 총 투표 시스템 계약에 추가하여 사전에 충분한 설명이 이루어져야 합니다.

## 제 8조 --- 계정 생성의 자유

현재, 또는 미래의 사용자는 다른 사용자의 허가 없이 EOS 계정을 만들 수 있습니다. eosio.prods는 EOS 계정에 의해 공유된 유효한 허가 없이는 EOS 사용자 계정에 영향을 줄 수 없습니다. eosio.prods는 권한이 공유되는 EOS 계정과 관련하여 다른 사용자가 요청한 모든 작업에 대해 요금을 부과할 수 있습니다.

## 제 9조 --- 신탁 불가

사용자는 EOS 토큰의 가치를 뒷받침할 수 있는 신탁 목적을 가져서는 안됩니다. 사용자는 EOS 사용자 또는 EOS 블록체인 chain_id를 대표하여 누구에게도 자산을 보유하거나, 대여하거나, 자산에 대해 얘기하거나, 계약을 맺을 권한을 부여할 수 없습니다. EOS 블록체인에는 소유자, 관리자, 그리고 수탁자가 없어야 합니다.

## 제 10조 --- 사용자 보안

비공개 키의 보관을 포함하되, 이에 국한되지 않는 개인 계좌 보안과 관련된 모든 항목들 또한 전적으로 사용자가 안전하게 보관해야 합니다.

## 제 11조 --- eosio.prods 유한책임

사용자는 법률이 허용하는 한도 내에서 EOS 토큰의 위험, 사용, 또는 사용 불가로 인해 발생하는 모든 손해에 대해 책임의 면책 조항이 적용된다는 것을 인정하고, 동의합니다. 계약 위반, 불법 행위, 그리고 위반 행위 (관리 태만 포함)와 eosio.prods 또는 이를 운영하는 개별 사용 권한을 포함하되, 이에 국한하지 않고 모든 관할 지역에서의 모든 종류의 사유로 인한 EOS 블록체인 chain_id 이익, 영업권, 또는 데이터의 손실을 포함하여 간접적, 우발적, 특수한, 대표적, 그리고 파생적인 손해에 대한 책임을 지지 않습니다.

# EOS用户协议

## **定义**

EOS用户协议中的所有大写，斜体或内联代码术语将具有与以下定义相同的效果和含义。

- EOS用户协议：即本文档（EUA）

- 链上ID: chain_id - aca376f206b8fc25a6ed44dbdc66547c36c6c33e3a119ffbeaef943642f0e906

- 用户：任意满足下列要求的个人或组织：直接或者间接拥有EOS账户或与EOS账户关联的基于EOS发行的财产。

- 所有权：直接或者间接通过一个或多个有效的权限检查访问一个EOS账户。所有权可以通过多签权限许可在用户间共享。

- 执行了regproduce，并且从eosio.vpay领取收入的用户。

- eosio.prods:具有动态权限结构的EOS帐户，当15/21 Block Producers同意时，该帐户可以承担eosio帐户的权限。

- 网络资产：包含在以下账户中的代币：eosio.names、eosio.ramfee、  eosio.saving。

- 治理文档：regproducer是治理文档。

- 任何交易、智能合约或者李嘉图合约，它们已经位于一个区块中，并且这个区块是不可逆转的、已附加到名为chain_id的EOS区块链中。

- 基于EOS资产：任何需要有效许可来操作、改变、转移、影响或者进行其他操作的东西。

- 执行：在名为chain_id的EOS区块链中提交一个行动。

- 授权和权限：权限（Permissions）是用来定义代表该权限发送的交易的要求的任意名字。可以给特定的合约操作的授权（Authorizations）分配权限（Permissions）。

- 李嘉图合约：将法律协议中的定义要素以能在软件中表达和执行的格式表达的合约。

## **条款一****用****户风险确认**

如果用户丢失账户访问权限或者没有采取合适的方式保护账户访问权限，用户应知悉并同意，EOS账户将无法访问。用户应确认用户对加密代币和区块链软件的风险、用法和复杂性有充分了解。用户承认并同意用户自行承担使用EOS区块链的风险。

## **条款二****特殊用****户类型**

执行regproduce，同意并且受regproducer李嘉图合约约束的用户。

## **条款三****同意****EOS****用****户协议**

EOS用户协议的实质是对当前EOS主网治理功能的描述。由代码强制执行的功能不需要用户的同意，因为这些功能是EOS主网系统自带的。

## **条款四** - **治理文档**

eosio.prods可以对EOS用户协议和治理文档进行任何修改。严正提醒，提前用eosio.forum公投合约，通过eosio.prods编写、发布一个声明来描述那个修改。

## **条款五****原生价****值单位**

EOS公链上的原生价值单位应为eosio.token智能合约定义和创建的EOS通证。

## **条款六****维护****EOS****区****块链**

无论现在或将来将来，eosio.prods将维护活跃的区块链代码库，包括但不限于所有功能、优化、升级的所有修改、实现。

## 条款七 - ****定****义****EOS****网络资产

更改网络资产账户中的任何代币的状态，更改任何现存的直接或间接管理任何网络资产的分配、实现或分发的代码，需要事先用eosio.prods在eosio.forum公投合约上编写和发布效果描述的声明。

## **条款八-创建账户自由**

任何现在或将来的用户都可以在未经任何其他用户许可的情况下创建EOS帐户。  如何没有收到EOS帐户的有效许可（permission），eosio.prods永远不会影响EOS用户帐户。  对于共享权限的EOS帐户的其他用户请求的任何操作，eosio.prods可能会收取费用。

## **条款九没有受托人**

没有用户承担信托责任来维持EOS代币的价值。没有用户可以代表EOS用户或者代表名为chain_ID的EOS区块链授权任何人共同持有资产、借款、发言或定合同。此区块链不存在拥有者、管理者或者受托人。

## **条款十个人安全**

所有有关个人账户安全的事项，包括但不限于私钥的安全保存，都由用户自己负责。

## **条款十一 eosio.prods的有限责任**

用户应知悉和同意，在任何适用法律允许的最大范围内，本免责声明适用于与EOS代币风险，使用或无法使用EOS代币有关或导致的任何或所有损害或伤害，也适用于任何司法管辖区内的任何任何行为下的EOS区块链chain_id，包括但不限于违反担保、违反合同或侵权行为（包括疏忽）。eosio.prods以及操作它的个人权限对于任何间接的，偶然的，特殊的，示例性的或后果性的损害，包括利润损失，商誉或数据，不承担任何责任。

---
spec_version: 0.1.1
title: Close Rex
summary: Free up any REX-related database entries in RAM from the account {{ owner }} 
icon: NEED TO ADD
---

The `closerex` action allows an account to delete unused REX-related database entries and frees occupied RAM associated with its storage.

As an authorized party, I {{ signer }}, wish to delete all unused REX-related database entries from the account {{ owner }}.

I will not be able to succesfully call `closerex` unless all checks for CPU loans, NET loans or refunds pending refunds are still processing on the account {{ owner }}.

---
spec_version: 0.1.1
title: Cancel REX Order
summary: Cancel any queued REX sell orders for account {{ owner }}
icon: NEED TO ADD
---

The `cnclrexorder` action cancels a queued REX sell order if one exists for an account.

As an authorized party I, {{ signer }}, wish to cancel any unfilled and queued REX sell orders that exist for the account {{ owner }}. 

---
spec_version: 0.1.1
title: Consolidate Maturity Buckets
summary: Consolidate any open maturity buckets for account {{ owner }}
icon: NEED TO ADD
---
 
The `consolidate` action will consolidate all REX maturity buckets for an account into one that matures 4 days from 00:00 UTC.
 
As an authorized party I, {{ signer }}, wish to consolidate any open REX maturity buckets for the account {{ owner }} into one that matures 4 days from the following 00:00 UTC.

---
spec_version: 0.1.1
title: Defund CPU Loan
summary: Remove {{ amount }} EOS tokens previously assigned by {{ from }} to renew CPU loan {{ loan_num }}
icon: NEED TO ADD
---

The `defcpuloan` action allows an account to withdraw tokens from the fund of a specific CPU loan and adds them to REX fund.

As an authorized party I, {{ signer }}, wish to withdraw from the CPU loan fund identified by loan number {{ loan_num }} on the account {{ from }} in the amount of {{ amount }} EOS and have those tokens allocated to the REX fund of {{ from }}.

---
spec_version: 0.1.1
title: Defund Network Loan
summary: Remove {{ amount }} EOS tokens previously set by {{ from }} to renew Network loan {{ loan_num }}
icon: NEED TO ADD
---

The `defnetloan` action allows an account to withdraw tokens from the fund of a specific Network loan and adds them to REX fund.

As an authorized party I, {{ signer }}, wish to withdraw from the Network loan fund identified by loan number {{ loan_num }} on the account {{ from }} in the amount of {{ amount }} and have those tokens allocated to the REX fund of {{ from }}.

---
spec_version: 0.1.1
title: Delegate Bandwidth
summary: {{ from }} stakes EOS tokens for the account {{ receiver }}, {{ stake_net_quantity }} for Network and {{ stake_cpu_quantity }} for CPU
icon: NEED TO ADD
---

As an authorized party I, {{ signer }}, wish to stake {{ stake_net_quantity }} EOS for Network and {{ stake_cpu_quantity }} EOS for CPU from the liquid tokens of {{ from }} for the use of {{ receiver }}.

By including the `--transfer` flag, {{ from }} would like to permanently transfer the tokens to {{ receiver }} and not just temporarily delegate their resources.

I understand that should I wish to unstake these tokens and relinquish the claim on resources that I shall be restricted by the wait period as described in `undelegatebw`.

---
spec_version: 0.1.1
title: Delete Authority
summary: Delete the permission authority {{ permission }} of account {{ account }}
icon: NEED TO ADD
---

As an authorized party I, {{ signer }}, wish to delete the permission authority {{ permission }} of account {{ account }}.

I understand that this action, once called, cannot be revoked.

---
spec_version: 0.1.1
title: Deposit to REX Fund
summary: Deposit {{ amount }} EOS tokens from the liquid balance of {{ owner }} into their REX Fund.
icon: NEED TO ADD
---

The `deposit` action allows an account to deposit EOS tokens into their REX fund by transfering from their liquid token balance.

As an authorized party I, {{ signer }}, wish to deposit {{ amount }} EOS tokens into the REX fund of the account {{ owner }} from the liquid token balance of {{ owner }}.

---
spec_version: 0.1.1
title: Fund CPU Loan
summary: Assign {{ payment }} EOS tokens for the renewal of CPU loan {{ loan_num }} upon expiry.
icon: NEED TO ADD
---

The `fundcpuloan` action allows an account to transfer tokens from its REX fund to the fund of a specific CPU loan in order for those tokens to be used for loan renewal at the loan's expiry.

As an authorized party I, {{ signer }}, wish to transfer the amount of {{ payment }} tokens into the CPU loan fund of the loan identified by loan number {{ loan_num }} from the account {{ from }} to be used for loan renewal at the expiry of {{ loan_num }}.

---
spec_version: 0.1.1
title: Fund Network Loan
summary: Assign {{ payment }} EOS tokens for the renewal of Network loan {{ loan_num }} upon expiry.
icon: NEED TO ADD
---

The `fundnetloan` action allows an account to transfer tokens from its REX fund to the fund of a specific Network loan in order for those tokens to be used for loan renewal at the loan's expiry.

As an authorized party I, {{ signer }}, wish to transfer the amount of {{ payment }} tokens into the Network loan fund of the loan identified by loan number {{ loan_num }} from the account {{ from }} to be used for loan renewal at the expiry of {{ loan_num }}.

---
spec_version: 0.1.1
title: Link Authority
summary: Link permission authority {{ requirement }} of account {{ account }} to a specific contract's action
icon: NEED TO ADD
---

I, {{ signer }}, wish to link the permission authority {{ requirement }} of {{ account }} to the action {{ type }} of the smart contract {{ code }}.

I can only remove this link by calling the `unlinkauth` action, and will need to do so before being able to call `deleteauth`.

I can specify a specific action from contract {{ code }}, or I can use a wildcard to link all actions within a contract to the authority {{ requirement }}. If new actions are added to contract {{ code }}, my account {{ account }} will be able to call those new actions.

I acknowledge that I cannot use `linkauth` for the following actions: `updateauth`, `deleteauth`, `linkauth`, `unlinkauth`, and `canceldelay`.

---
spec_version: 0.1.1
title: Move REX From Savings
summary: Commence maturing {{ rex }} REX tokens from the savings bucket of account {{ owner }}.
icon: NEED TO ADD
---

The `mvfrsavings` action allows an account to move REX tokens from its savings bucket to a bucket with a maturity date that is 4 days after 00:00 UTC.

As an authorized party I, {{ signer }}, wish to move {{ rex }} tokens from the savings bucket of the account {{ owner }}. Those tokens shall become available to {{ owner }} 4 days from 00:00 UTC.

---
spec_version: 0.1.1
title: Move REX to savings
summary: Move {{ rex }} REX tokens into the savings bucket of account {{ owner }}
icon: NEED TO ADD
---

The `mvtosavings` action allows an account to move REX tokens into a savings bucket.

As an authorized party I, {{ signer }}, wish to move {{ rex }} tokens to a savings bucket associated to the account {{ owner }}. I acknowledge that those tokens will then be subject to any maturity restrictions described in the `mvfrsavings` action. 

---
spec_version: 0.1.1
title: Create New Account
summary: Account {{ creator }} creates the account {{ name }}
icon: NEED TO ADD
---

The `newaccount` action creates a new account.

As an authorized party I, {{ signer }}, wish to exercise the authority of {{ creator }} to create a new account on this blockchain named {{ name }}, such that the new account's `owner` permission's public key shall be {{ owner }} and the `active` permission's public key shall be {{ active }}.

The account name {{ name }} must conform to the standards of only utilizing lowercase characters `a` through `z`, and `1` through `5`. 

Should there be a `.` in {{ name }}, then only the account who has won the `bidname` auction for that suffix may call the `newaccount` action.

Should the account name {{ name }} be fewer than 12 characters and not contain a `.`, the `newaccount` action may only be called by the winner of the `bidname` auction for that suffix by using the same account that cast the winning bid.

---
spec_version: 0.1.1
title: Refund
summary: Manually trigger a refund after the undelegation period for account {{ owner }}
icon: NEED TO ADD
---

The `refund` action will manually trigger a return of EOS tokens that should have been automatically allocated from `eosio.stake` to {{ owner }} at the end of the 72-hour undelegation period after calling `undelegatebw`. 

As an authorized party I, {{ signer }}, wish to have the any unstaked tokens due to {{ owner }} returned as liquid EOS tokens into the account {{ owner }}.

---
spec_version: 0.1.1
title: Register Producer
summary: Register a Block Producer Candidate on the account {{ producer }}
icon: NEED TO ADD
---
 
### 1. The intent of regproducer
The intent of the `regproducer` action is to register a block producer candidacy. This contract is considered a governing document as defined by the EOS User Agreement (EUA).

regproducer의 목적

`regproducer` 작업의 목적은 블록생산자 입후보 등록을 하는 것입니다. 이 계약은 EOS 사용자 계약서 (EUA)에 정의된 바와 같이 관리 문서로 간주됩니다.

regproducer 的目的

`regproducer`操作的目的是注册成为出块节点候选者。根据 EOS 用户协议(EUA)的定义，本合约属于治理文本(governing document)

### 2. Nomination
I, {{ producer }}, hereby nominate myself for consideration as a block producer candidate. This nomination includes agreement to the terms of this contract by my block producer candidate entity, including all of its shareholders, owners, employees, staff, members, and any individual working in official, direct, or affiliated capacity for my Block Producer entity.

지명

나, {{ producer }}는 블록프로듀서 후보로 고려되도록 자신을 지명합니다. 이 지명에는 블록프로듀서회사의 모든 주주, 소유자, 직원, 멤버, 회원 및 공식인원, 직접 또는 계열사에서 일하는 모든 개인을 포함한 블록프로듀서 회사가 계약 조건에 대해 동의함을 인정합니다.

提名

本人，{{ producer }}，特此提名本人为出块节点候选人。本提名包括了本出块节点候选人实体对本合约中所有条款的明确同意，包含其所有者、雇员、员工、成员，以及任何以正式方式、直接或附属方式为本出块节点实体工作的个人。

### 3. Resignation and Removal for Inability to Perform Obligations.

If I, {{ producer }}, am unable to perform any of the obligations stipulated in this contract, I will resign my position by calling the `unregprod` action.

If I, {{ producer }}, fail to resign when unable to perform said obligations, I understand that procedures enumerated in this contract shall be enacted.

의무의 불이행에 대한 사임 및 철회

{{ producer }}가 본 계약서에 명시된 의무를 수행 할 수 없는 경우, 생산자 키를 null 로 함으로써 본인의 지위를 사임합니다.

만약 내가 {{producer}}의 의무를 이행 할 수 없을 때 사임하지 않는다면, 나는 본 계약에 열거된 절차가 집행됨을 동의합니다.

因不能履行义务而退出或被取消出块资格
 
如果我，{{ producer }}，不能履行本合约中所规定的所有义务，我将使用 `unregprod` 操作来自我退出（resign）。

如果我 {{ producer }}, 在无法履行上述义务时未能退出(resign)，我知晓本合约将会按照所有列举的程序对我实行制裁或处罚程序。

### 4. EOS Accounts

Block Producers may never affect an account on the EOS blockchain, except for the reasons specifically cited in this contract that pertain to Block Producer accounts. User accounts can only be affected on the basis of Article VIII in the EOS User Agreement.
 
EOS 계정

블록프로듀서는 본 계약에서 해당하는 블록프로듀서의 계정 차단에 관련하여 특별히 언급한 이유를 제외하고는 EOS 블록체인의 계정에 결코 영향을 미치지 않습니다. 사용자 계정은 EOS 사용자 계약서의 8조에 근거할 때만 영향을 받을 수 있습니다.

EOS 账号

出块节点永远不会对 EOS 区块链上的帐户造成影响，除非是本合约中特别提到与出块节点帐户有关的原因。只有基于 EOS用户协议中的第八条的情形下，用户的账号才会受到影响. 

### 5. Producer Key

I, {{ producer }}, will sign blocks with {{ producer_key }}

If I, {{ producer }} suspect my key has been compromised I will alert the other Block Producers immediately.

I, {{ producer }}, acknowledge that any and all actions executed with my {{ producer_key }} is my responsibility, regardless of the account being compromised.

프로듀서 키

나, {{ producer }}는 {{ producer _ key }} 로 블록에 서명 할 것입니다. 
만약 내, {{producer}} 가 본인의 키가 손상되었다고 의심되면 즉시 다른 블록프로듀서에게 알려줄 것입니다.
나, {{producer}}는 EOS 블록체인에서 본인의 블록프로듀서 계정이 실행하는 모든 작업에 대해, 계정 이상 유무와 관련 없이, 책임이 있음을 인정합니다.

出块节点公钥

 我, {{ producer }}, 将使用 {{ producer_key }} 对区块签名。
如果我, {{ producer }}, 怀疑我的密钥已被泄露，我将立即通知其他节点。
我，{{ producer }}，承认我的出块节点帐户在EOS区块链上所执行的任何操作都是我的责任，无论该帐户是否被盗。

### 6. API Endpoints
 
If I, {{ producer }}, qualify for, and choose to claim rewards due to votes received, and/or blocks produced, I, {{ producer }}, will provide functioning and queryable public P2P and API endpoints to maintain synchronization with the blockchain and submit transactions to be included. API endpoints must be updated to a recent functional version that does not have known security vulnerabilities.
 
I, {{ producer }}, hereby acknowledge that if I am unable to do so within 30 minutes of being alerted by another block producer candidate, I can be removed by use of the `rmvproducer` action.

API 엔드포인트

만약 내, {{ producer }} 가 투표를 받아 블록 보상을 청구할 수 있는 자격을 얻으면, 나 {{ producer }}는 작동 및 쿼리 가능한 공개 P2P 및 API 엔드포인트를 블록체인과의 동기화 및 트랜잭션을 제출할 수 있게 유지관리합니다. API 엔드포인트는 알려진 보안 취약성이 없는 최신버전으로 업데이트해야 합니다.
 
나, {{ producer }} 는 다른 block producer candidate 가 경고 ​​한 후, 30분 이내에 바로잡을 수 없다면 `rmvproducer` 조치를 통해 자격이 제거 될 수 있음을 인정합니다.

API 端点
 
如果我，{{ producer }} 由于得到投票和/或出块的原因，符合领取奖励的条件并选择接受奖励，那么我， {{ producer }}，将提供功能正常的公共 P2P 和 API 端点来维护与区块链的同步，并提交要打包入块的事务。API 端点必须更新到最新的可用版本，并且该版本没有已知的安全漏洞

我，{{producer}}，在此确认，如果我在收到另一个 block producer candidate的警告后30分钟内仍不能符合上述要求，可以使用`rmvproducer`操作移除我的账户。
 
### 7. Execution time
 
I, {{ producer }}, will deploy and run network infrastructure capable of maintaining 2ms or less CPU execution times.
 
I, {{ producer }}, hereby acknowledge that if I am unable to do so within 30 minutes of being alerted by another block producer candidate, I can be removed by use of the `rmvproducer` action.

실행 시간
 
나, {{ producer }}는 2ms 또는 그 이하의 CPU 실행 시간을 유지할 수 있는 네트워크 인프라를 배포하고 실행합니다.

 나, {{ producer }} 는 다른 block producer candidate가 경고 ​​한 후, 30분 이내에 바로잡을 수 없다면 `rmvproducer` 조치를 통해 자격이 제거 될 수 있음을 인정합니다.

执行时间

我， {{ producer }}，将部署和运行网络基础设施，能够将 CPU 执行时间维持在 2ms 或更少的水平。

我，{{ producer }}，在此确认，如果我在收到另一个block producer candidate的警告后30分钟内不能符合上述条件，可以使用 `rmvproducer` 操作将我移除。
 
### 8. Ordering
I {{ producer }} agree to process transactions on a first-in-first-out (FIFO) basis, and not to manipulate the contents of blocks in order to derive profit from the order in which transactions are included: the hash of the block that is produced.

생산
나, {{ producer }}는 선입 선출법 (FIFO) 방식으로 거래를 처리하고 거래가 블록의 해시에 포함되는 순서에서 이익을 얻으려는 목적으로 생산하는 블록의 내용을 조작하지 않기로 동의합니다.
 
顺序

我， {{ producer }} ，同意根据先进先出(FIFO)的方式处理事务，并且绝不会为了牟利而利用区块内容、操纵区块中交易处理的顺序。
 
### 9. Random Rotation of Standbys
I, {{ producer }}, agree that if I am in a paid standby position, I can be randomly called into a producing position. Upon failure to produce blocks, code may self-execute penalties regarding future vpay rewards.

유급 대기 블록프로듀서의 무작위 로테이션

나, {{ producer }}는 본인이 유급 대기직에 있을 때, 무작위로 생산직으로 부름 받을 수 있다는 것에 동의합니다. 이때 블록을 생성하지 못하면 코드는 향후 vpay 보상에 대한 처벌을 집행할 수 있습니다.

备选节点随机轮换

我，{{ producer }}，同意若本节点处于有偿备选状态，可被随机调入出块状态。如果我无法出块，合约代码可能会自动执行就未来的 vpay 报酬进行处罚。

### 10. Missing Two or More Rounds of Blocks
I, {{ producer }}, acknowledge that if after missing 2 or more rounds of blocks in succession I am unable to be contacted within 20 minutes, I, {{ producer }}, acknowledge that I may be removed from a producing position by use of the `rmvproducer` action.
 
I, {{ producer }}, acknowledge that after missing two or more rounds of blocks in succession, standard practice stipulates removing my producer by using the `unregprod` action until the given issue is resolved. 
  
두 라운드 이상의 블록 누락

나, {{ producer }}는 두 라운드 이상 연속하여 블록을 누락 한 후, 20분 이내에 연락 할 수 없다면 {{ producer }} 가 `rmvproducer` 액션의 사용되어 생산 위치에서 제거 될 수 있음을 인정합니다.

{{ producer }}는 두 라운드 이상으로 블록을 연속적으로 누락한다면, 주어진 문제가 해결 될 때까지 `unregprod` 작업을 사용하여 본인이 생산 위치에서 제거됨이 표준 관행으로 규정되어 있음을 인정합니다.

两轮或更多轮丢块的情形
 
我，{{ producer }}, 确认如果连续两轮或更多轮丢块且无法在20分钟内联系到我，我，{{ producer }}, 同意可能会用 `rmvproducer` 操作将我移除。
我，{{ producer }}, 如果连续两轮或更多轮丢块，根据标准实践会发起 `unregprod` 操作将我移除出块资格，直到问题解决。
 
### 11. Urgent Security Patches
I, {{ producer }}, acknowledge that if I am not able to be contacted in any form after an urgent security patch is announced, I may be removed by use of the `rmvproducer` action.

긴급 보안 패치
긴급 보안 패치가 발표 된 후, 어떤 형태로든 연락 할 수 없는 경우 `rmvproducer` 작업을 사용하여 제거 될 수 있음을 나, {{ producer }}는 인정합니다.

紧急安全补丁

我，{{ producer }}，确认如果在紧急安全补丁发布后用任何方式都无法联系到我，可能会用 `rmvproducer` 指令将我移除。
 
### 12. Disclosure of Entity and Server Information
I, {{ producer }}, attest that I have disclosed the approximate geolocation for my main production node as being {{ location }}.

법인 및 서버 정보의 공개

나, {{ producer }} 는 주 생산 노드에 대한 위치 정보를 공개했음을 증명합니다.

实体和服务器的信息披露

我，{{ producer }}，确认我已经披露了主出块节点服务器地理位置的准确信息。其地址为 {{ location }}。

### 13. Establishes the penalty and procedure for unwillingness to comply with penalties or procedures

I, {{ producer }}, acknowledge that failing to comply with penalties or procedures enacted against me will result in Block Producers executing the `rmvproducer` contract to remove me. 

I, {{ producer }}, will not execute the `regproducer` contract until serving or fulfilling the requirements from a penalty or procedure that results in having the `rmvproducer` contract executed to remove me.

I, {{ producer }}, acknowledge that if I continue to call the `regproducer` action without serving or fulfilling the requirements from breach of `regproducer`, my account keys associated with the registered Block Producer in question may be nulled by Block Producers by using `eosio.wrap`.

페널티를 준수하지 않을 경우 벌칙

나, {{ producer }} 는 나에게 제재된 처벌을 준수하지 않으면 블록프로듀서들이 `rmvproducer` 계약을 집행하게 될 것이라고 인정합니다. 나, {{ producer }} 는 `rmvproducer` 계약이 집행된다면 요구 사항을 충족될 때까지 `regproducer` 계약을 이행하지 않을 것입니다.
`regproducer` 계약 위반으로 인한 요구 사항을 충족시키지 않고 `regproducer` 계약을 계속 호출하면 해당 블록프로듀서와 관련된 계정 키가 `eosio.wrap` 을 사용하여 블록프로듀서들에 의해 무효화 될 수 있음을 인정합니다. 

对不愿遵守处罚的行为予以处罚
 
我，{{ producer }}，承认若不遵守对本人制裁的处罚，BP 可以实施 `rmvproducer` 合约，我接受投票的资格将被取消。若有针对我实施 `rmvproducer` 合约的情况发生，我, {{ producer }} 在遵守/履行所收到的处罚之前，不会再次执行 `regproducer` 合约。

我，{{ producer }}，在履行惩罚程序的要求之前，不会执行 `regproducer` 合同。我知晓如不履行此程序， `rmvproducer` 合同将会再次将我移除。

我,{{ producer }}, 承认如果没有遵守或履行因违反 `regproducer` 而受到的惩罚要求却继续调用`regproducer`操作，BP 可以调用 `eosio.wrap` 合约将我用来注册出块节点的账号密钥设置为无效值。

---
spec_version: 0.1.1
title: Register Proxy
summary: Register account {{ proxy }} as a proxy
icon: NEED TO ADD
---

As an authorized party I, {{ signer }}, would like to register the account {{ proxy }} as a proxy by having the {{ isproxy }} value updated to `1`.

As a proxy, the vote weight of all accounts who proxy to {{ proxy }} will be delegated along with its own. For all proposals created within `eosio.forum`, their vote weight will also be delegated to {{ proxy }}, unless that account chooses to cast their own vote for a proposal.

---
spec_version: 0.1.1
title: Rent CPU
summary: Rent CPU for account {{ receiver }} using payment of {{ loan_payment }} EOS tokens
icon: NEED TO ADD
---

The `rentcpu` action allows an account to rent CPU bandwidth for 30 days at a market-determined price.

As an authorized party I, {{ signer }}, wish to rent CPU bandwidth for 30 days for the use of the account {{ receiver }} in exchange for the loan payment of {{ loan_payment }}, which shall be taken from the account {{ from }}. The loan fund amount {{ loan_fund }} is set for automatic renewal of the loan at the expiry of said loan.

The amount of CPU bandwidth shall be determined by the market at time of loan execution and shall be recalculated at time of renewal, should I wish to automatically renew the loan at that time. I acknowledge that the amount of CPU bandwidth received in exchange of {{ loan_payment }} for the benefit of {{ receiver }} at loan renewal may be different from the current amount of bandwidth received. 

---
spec_version: 0.1.1
title: Rent Network
summary: Rent Network for account {{ receiver }} using payment of {{ loan_payment }} EOS tokens
icon: NEED TO ADD
---

The `rentnet` action allows an account to rent Network bandwidth for 30 days at a market-determined price.

As an authorized party I, {{ signer }}, wish to rent Network bandwidth for 30 days for the use of the account {{ receiver }} in exchange for the loan payment of {{ loan_payment }}, which shall be taken from the account {{ from }}. The loan fund amount {{ loan_fund }} is set for automatic renewal of the loan at the expiry of said loan.

The amount of Network bandwidth shall be determined by the market at time of loan execution and shall be recalculated at time of renewal, should I wish to automatically renew the loan at that time. I acknowledge that the amount of Network bandwidth received in exchange of {{ loan_payment }} for the benefit of {{ receiver }} at loan renewal may be different from the current amount of bandwidth received. 

---
spec_version: 0.1.1
title: Execute REX Maintenance
summary: Execute up to {{ max }} REX maintenance actions that may be pending
icon: NEED TO ADD
---

The `rexexec` action allows any account to perform REX maintenance by processing expired loans and unfilled sell orders.

I, {{ signer }}, wish to process up to {{ max }} of any CPU loans, Network loans, and sell orders that may currently be pending.

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
within `regproducer`, or any other governing documents which may make reference to `rmvproducer`.---
spec_version: 0.1.1
title: Sell RAM
summary: Sell {{ bytes }} bytes of RAM from account {{ account }}
icon: NEED TO ADD
---

The `sellram` action sells currently unused RAM for EOS tokens.

As an authorized party I, {{ signer }}, wish to sell {{ bytes }} of unused RAM from account {{ account }}. 

---
spec_version: 0.1.1
title: Sell REX
summary: Create an order to sell {{ rex }} tokens held by {{ from }}
icon: NEED TO ADD
---

The `sellrex` action allows an account to sell REX tokens held by the account.

As an authorized party I, {{ signer }}, wish to sell {{ rex }} REX tokens held on the account {{ from }} in exchange for core EOS tokens. If there is an insufficient amount of EOS tokens available at this time, I acknowledge that my order will be placed in a queue to be processed. 

If there is an open `sellrex` order for the account {{ from }}, then this amount of {{ rex }} REX shall be added to the existing order and the order shall move to the back of the queue. 

---
spec_version: 0.1.1
title: Set ABI
summary: Set an ABI file on the account {{ account }}
icon: NEED TO ADD
---

As an authorized party I, {{ signer }}, would like to set the ABI file corresponding to the sha256 hash {{ abi }} to the account {{ account }}.
The ABI data will be stored in the RAM of {{ account }}.

---
spec_version: 0.1.1
title: Set Code
summary: Set the contract code for account {{ account }}
icon: NEED TO ADD
---

As an authorized party I, {{ signer }}, would like to set the Smart Contract file corresponding to the sha256 hash {{ code }} to the account {{ account }}.
The ABI data will be stored in the RAM of {{ account }}.

When calling `setcode`, I shall produce suitable Ricaridan Contracts within the ABI file when calling `setabi` for the account {{ account }}.

---
spec_version: 0.1.1
title: Undelegate Bandwidth
summary: Undelegate {{ unstake_cpu_quantity }} CPU and {{ unstake_net_quantity }} Network bandwidth from {{ receiver }}
icon: NEED TO ADD
--- 

As an authorized party I, {{ signer }}, wish to unstake {{ unstake_cpu_quantity }} from CPU and {{ unstake_net_quantity }} from Network bandwidth from the tokens owned by {{ from }} previously delegated for the use of delegatee {{ receiver }}. 

I acknlowedge that I do not expect to have access to these tokens until at least 72 hours have passed since calling the `undelegatebw` action.

The CPU and Network bandwidth resources that have been unstaked will be immediately revoked from {{ receiver }}. Any voting weights based on staked resources will become immediately effected. 

If I, {{ signer }} am not the beneficial owner of these tokens I stipulate I have been authorized to take this action by their beneficial owner(s). 

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
title: Unregister Block Producer
summary: Unregister the Block Producer Canadidate {{ producer }}
icon: NEED TO ADD
---

The `unregprod` action unregisters a previously registered Block Producer Candidate.

As an authorized party I, {{ signer }}, wish to unregister the Block Producer Candidate {{ producer }}, rendering that candidate no longer able to receive votes.

---
spec_version: 0.1.1
title: Unstake to REX
summary: Purchase REX tokens using EOS tokens staked to CPU or Network Bandwidth
icon: NEED TO ADD
---

The `unstaketorex` action allows an account to buy REX using EOS tokens which are currently staked for either CPU or Network bandwidth.

As an authorized party I, {{ signer }}, wish to buy REX tokens by unstaking {{ from_cpu }} EOS from CPU bandwidth and {{ from_net }} EOS from Network bandwidth from account {{ owner }} that are staked to account {{ receiver }}.

I am aware of, and have fulfilled, all voting requirements needed to participate in the REX marketplace.

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

---
spec_version: 0.1.1
title: Update REX
summary: Update the REX voting weight of the account {{ owner }}
icon: NEED TO ADD
---

The `updaterex` action allows an account to update its vote weight.

As an authorized party I, {{ signer }}, wish to update the REX vote stake and vote weight of the account {{ owner }}.

---
spec_version: 0.1.1
title: Vote Producer
summary: {{ voter }} casts a vote for their preferred Block Producers
icon: NEED TO ADD
---

The `voteproducer` action casts a valid vote for up to 30 Block Producer Candidates. 

As an authorized party I, {{ signer }}, wish to vote on behalf of the account {{ voter }} in favor of the Block Producer Candidates {{ producers }} with a voting weight equal to all EOS tokens currently owned by {{ voter }} and staked for CPU or Network bandwidth, and the equivalent value of REX tokens that {{ voter }} holds. 

If I am not the beneficial owner of these shares I stipulate that I have been authorized to vote these shares by their beneficial owner(s). 

I stipulate I have not, and will not, accept anything of value in exchange for these votes, on penalty of confiscation of these tokens, and other penalties. 

I acknowledge that using any system of automatic voting, re-voting, or vote refreshing, or allowing such a system to be used on my behalf or on behalf of another, is forbidden and doing so violates this contract.

---
spec_version: 0.1.1
title: Withdraw
summary: Withdraw {{ amount }} EOS tokens from the REX fund of {{ owner }}
icon: NEED TO ADD
---

The `withdraw` action allows an account to withdraw EOS tokens from their REX fund into their liquid token balance.

As an authorized party I, {{ signer }}, wish to withdraw {{ amount }} of EOS tokens from the REX fund for the account {{ owner }} into its liquid token balance.
