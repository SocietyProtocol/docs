# Badges & Account Histories

Badges form the core identity primitive of the Web3 Outpost. Attached to sybil-resistant accounts, badges differentiate users over time by recording verifiable history, roles, characteristics, and contributions.

---

## 💡 Accounts & Badges Overview

### Accounts
All participants in the Society Protocol movement create an Ethereum-based account within the Web3 Outpost. 
* **Long-Term Continuity:** Users are encouraged to maintain a single main account that accumulates a rich, multi-year history.
* **Referral Chains:** Accounts support permanent referral chains, recording relationships between participants that can later inform Genesis parameters in Web4 SP instances.

### Badges (ERC-1155)
Badges are non-fungible or semi-fungible tokens minted to accounts under the `SocietyProtocolBadges` proxy (`0x2313...6763`). They serve two primary roles:
1. **Functional Credentials:** Unlock token-gated communication channels, DAO governance rights, or administrative moderation roles.
2. **Permanent Attributions:** Create verifiable proof of event attendance, core contributions, or verified off-chain attributes (via zkTLS).

---

## 🛠️ Technical Reference: Badge Standards & Attributes

Badges leverage **ERC-1155** on Ethereum Mainnet for gas efficiency and modularity.

```
+-------------------+      zkTLS / SPEC Lock      +--------------------+
|                   |  ------------------------>  |                    |
|   User Account    |                             | SingleMintHook     |
|   (Web3 Outpost)  |  <------------------------  | Verification       |
+-------------------+       Mint Token ID         +--------------------+
                                                            |
                                                            v
                                                  +--------------------+
                                                  |  ERC-1155 Badge    |
                                                  |  `0x2313...6763`   |
                                                  +--------------------+
```

### Core Token Properties

| Property | Value / Description |
| :--- | :--- |
| **Token Standard** | ERC-1155 Multi-Token |
| **Proxy Contract** | `0x2313C0cDdc233c92d16c2cfE17DF5fDCcE556763` |
| **Implementation** | `0x924F6Bc77089e1aa0333BCF4a9f698112734a3c2` |
| **Mint Enforcer** | `SingleMintHook` (`0xc5cA...FC6D`) |
| **URI Scheme** | `ipfs://` metadata resolved via protocol registry |
