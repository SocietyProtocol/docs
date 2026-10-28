# Accounts & Badges

In Web3, a wallet is just a cryptographic key. It has no history, no reputation, and no identity. Anyone can create a thousand wallets in a minute. 

The Web3 Outpost solves this by introducing **Accounts** and **Badges**. This is the core identity primitive of the Outpost, it transforms an anonymous wallet into a recognizable participant with a verifiable history.

---

## Accounts

All participants in the Society Protocol movement create an Ethereum-based account within the Web3 Outpost.

- **Long-Term Continuity:** Users are encouraged to maintain a single main account. While anyone can create a new wallet, the Outpost rewards those who maintain a single account that accumulates a rich, multi-year history of contributions and relationships.

## What is a Badge?

Badges are verifiable digital credentials minted directly to your account. They serve two primary roles:

1. **Functional Credentials:** They act as keys. A specific badge might unlock a private Discord channel, grant voting rights in the DAO, or give you admin moderation powers.
2. **Permanent Attributions:** They act as a resume. They create verifiable proof of event attendance, core code contributions, or verified off-chain attributes (like proving you hold a specific passport without revealing your identity).

---

## Why ERC-1155? 

You will often see badges referred to as **ERC-1155** tokens. Here is why that matters.

In crypto, there are different "standards" for tokens:

- **ERC-20** is like a standard dollar bill. Every dollar is identical and interchangeable.
- **ERC-721** is like a unique painting. There is only one, and it cannot be replaced.
- **ERC-1155** is like a **digital ticket wallet**. It allows a single smart contract to manage both unique items (a one-of-a-kind VIP pass) and multi-copy items (10,000 general admission tickets) at the same time. 

For the Outpost, ERC-1155 is perfect. It allows us to issue thousands of "Builder" badges (multi-copy) and a single "Security Council" badge (unique) using the same system, which saves massive amounts of gas fees and keeps the architecture clean.

---

## How Badges are Issued (The Verification Mechanism)

Issuing a badge is not a manual process. The Outpost uses automated smart contracts (known as **Hooks**) to ensure badges cannot be forged or duplicated.

1. **The Verification:** When you claim a badge, the Outpost verifies your eligibility. This can happen in two ways:
    - **zkTLS:** You cryptographically prove an off-chain fact (e.g., "I own this GitHub account" or "I am a verified Argentine citizen") without revealing your passwords or personal data.
    - **SPEC Lockup:** You lock SPEC tokens in a vault to prove economic commitment.

2. **The Hook:** Once verified, a smart contract (the Hook) automatically approves the transaction. It ensures you haven't already claimed the badge (preventing duplicates).
3. **The Mint:** The badge is minted to your account. Most governance and role badges are **Soulbound**, meaning they are permanently locked to your account and cannot be transferred or sold to someone else. 

Note that, the Web3 Outpost provide the freedom to the communities to determine the way they want to configure their own badges.

