# VIP Rooms & Token-Gated Access

VIP Room Badges grant accounts entry into 3 exclusive, spam-free communication channels thanks to the Web3 Outpost.

--- 

## Overview & Access Mechanics

Acquire VIP Badges by locking SPEC tokens (`0x6AcD...18BA`) in protocol vaults. By requiring a time-bound token lockup, the protocol makes sybil manipulation economically unviable, keeping VIP channels highly aligned.

### Access Tiers & Badges

#### Bronze VIP Badge (Badge ID: 14)
![Bronze VIP Badge](../SP%20badges%20images/Bronze%20VIP.png)

- **Access Level:** Entry-tier access. General VIP rooms for serious community discussion, free of spam and with active core team presence.

#### Silver VIP Badge (Badge ID: 15)
![Silver VIP Badge](../SP%20badges%20images/Silver%20VIP.png)

- **Access Level:** Mid-tier access. A gathering space primarily for our network of partner communities, and those who want to connect with them.

#### Gold VIP Badge (Badge ID: 16)
![Gold VIP Badge](../SP%20badges%20images/Gold%20VIP.png)

- **Access Level:** Elite tier access. Channels designed for advisors, gold community partners, and the SP leadership (founder + CEO).

---

## Technical Reference: SPEC Lock Tiers

| Badge Name | Badge ID | SPEC Lock Threshold | Minimum Lock Duration |
| :--- | :---: | :---: | :---: |
| **Bronze VIP Badge** | `14` | 400,000 SPEC | 30 days |
| **Silver VIP Badge** | `15` | 2,000,000 SPEC | 30 days |
| **Gold VIP Badge** | `16` | 10,000,000 SPEC | 30 days |

> **Source of truth:** Thresholds and the minimum lock duration are set on-chain in the `SocietyVipManager` contract (`0x8840...7117`, see [Smart Contracts](../technical/contracts.md)). The values above reflect Ethereum Mainnet; the contract owner (currently an externally owned account, not the SP DAO Safe) can update the tier thresholds.

