# FAQ & zkTLS Verification

This page answers Frequently Asked Questions and provides a deep dive into **zkTLS & Off-Chain Verification**, explaining how Web2 credentials and private data are brought on-chain to claim badges without compromising privacy.

---

## 🔒 What is zkTLS & Off-Chain Verification?

**zkTLS (Zero-Knowledge Transport Layer Security)** is a cryptographic technology that allows users to generate zero-knowledge proofs of Web2 TLS web sessions (e.g. logging into Twitter, GitHub, bank portals, or government passport verification systems).

### Key Benefits

1. **Privacy-Preserving:** Proven credentials (e.g. "User is over 18" or "User holds verified GitHub account") are verified on-chain **without** revealing passwords, personal identifying information, or API tokens.

2. **Trustless Verification:** Proofs are verified directly by Society Protocol smart contract hooks (such as `SingleMintHook` at `0xc5cA...FC6D`).

3. **Sybil Resistance:** Prevents bot farming by linking unique physical or off-chain identity proofs to single Ethereum addresses.

---

## ⚙️ How zkTLS Badge Verification Works

```
+------------------+         Web2 TLS Session        +-------------------+
|  User's Browser  | <-----------------------------> |  Web2 Provider    |
| (zkTLS Prover)   |                                 | (Twitter/GitHub)  |
+------------------+                                 +-------------------+
         |
         | Generates Zero-Knowledge Proof (ZKP)
         v
+------------------+       Submit Proof              +-------------------+
| Society Protocol | ------------------------------> | Smart Contract    |
| Claim Interface  |                                 | Verification Hook |
+------------------+                                 +-------------------+
                                                               |
                                                               v
                                                     +-------------------+
                                                     | Mint ERC-1155     |
                                                     | Off-Chain Badge   |
                                                     +-------------------+
```

---

## ❓ Frequently Asked Questions (FAQ)

### General Questions

#### Q: Do I need to pay gas to claim badges?
**A:** Official badges minted on Ethereum Mainnet require standard gas. However, for select community badges, gasless meta-transactions (EIP-712) or Layer-2 wrapper deployments are supported.

#### Q: Are official badges transferable?
**A:** Most official governance and role badges (IDs `11`–`13`, `24`–`28`) are **Soulbound** (non-transferable) to protect credential integrity. VIP Badges (IDs `14`–`16`) are tied to SPEC lockup vaults and burn upon token withdrawal.

#### Q: What happens if I lose access to my wallet?
**A:** Because official badges are cryptographically tied to your wallet address, you must re-verify your identity or re-lock SPEC tokens from a new wallet address. Security Council revocation can clear lost address holdings upon request.

---

### Technical & Developer Questions

#### Q: Where is badge metadata stored?
**A:** All badge metadata JSON files and visual assets are permanently pinned to IPFS and indexed by `CommunityRegistry` (`0xEa008f15E1454C79D6AA7B95Dd3E1d39Ba32EB76`).

#### Q: Can I use Society Protocol badges in my Discord server?
**A:** Yes! Any Discord server can integrate Guild.xyz, Collab.Land, or Society Protocol's native OAuth bot pointing to `SocietyProtocolBadges` (`0x2313...6763`).
