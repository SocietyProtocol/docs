# Badge ID Registry

All official badges are minted as **ERC-1155** tokens under the `SocietyProtocolBadges` proxy (`0x2313C0cDdc233c92d16c2cfE17DF5fDCcE556763`).

---

## 📋 Official Badge ID Registry Table

| Preview | Badge Name | Badge ID | Mint Rule / Privilege | Transferability | Target Audience |
| :---: | :--- | :---: | :--- | :---: | :--- |
| ![SP DAO](../SP%20badges%20images/SP%20DAO.png) | **DAO Badge** | `11` | Represents the DAO Entity | Soulbound | `societyprotocol.eth` (DAO Account) |
| ![Security Council](../SP%20badges%20images/Security%20Council.png) | **Security Council Badge** | `12` | Identifies the Security Council Account | Soulbound | Security Council Multisig Account |
| ![Governor](../SP%20badges%20images/Governor.png) | **Governor Badge** | `13` | Meritocratic DAO Voting Seat | Soulbound | Appointed Governors |
| ![Bronze VIP](../SP%20badges%20images/Bronze%20VIP.png) | **Bronze VIP Badge** | `14` | Access to Bronze VIP Channels | Locked via SPEC | Outpost Members |
| ![Silver VIP](../SP%20badges%20images/Silver%20VIP.png) | **Silver VIP Badge** | `15` | Access to Silver VIP Channels | Locked via SPEC | Outpost Members |
| ![Gold VIP](../SP%20badges%20images/Gold%20VIP.png) | **Gold VIP Badge** | `16` | Access to Gold VIP Channels | Locked via SPEC | Outpost Members |
| ![Advisor](../SP%20badges%20images/Advisor.png) | **Advisor Badge** | `24` | Strategic Advisor Recognition | Soulbound | Protocol Advisors |
| ![Core Team](../SP%20badges%20images/Core%20Team.png) | **Core Team Badge** | `25` | Awarded after 6 months of service | Soulbound | Full-Time Core Team |
| ![Contributor](../SP%20badges%20images/Contributor.png) | **Contributor / Builder Badge** | `26` | Code / Research Contribution | Soulbound | Ecosystem Developers |
| ![ICO Participant](../SP%20badges%20images/ICO%20participant.png) | **ICO Participant Badge** | `27` | Fundraiser Contribution | Soulbound | Early Backers |
| ![Moderator](../SP%20badges%20images/moderator.png) | **Moderator Badge** | `28` | Outpost Forum / Channel Moderator | Soulbound | Community Ops |

> [!NOTE]
> **System Identity Badges (ID 11 and ID 12):** Unlike other role-based or community-locked badges that are minted to individual human participants, the **DAO Badge (ID: 11)** and **Security Council Badge (ID: 12)** are identity markers held exclusively by their respective contract/multisig accounts (`societyprotocol.eth` and the Security Council Safe) to represent the entities themselves.

---

## 🔍 Cast Query Example

```bash
cast call 0x2313C0cDdc233c92d16c2cfE17DF5fDCcE556763 \
  "balanceOf(address,uint256)(uint256)" \
  <USER_WALLET_ADDRESS> <BADGE_ID> \
  --rpc-url https://eth-mainnet.g.alchemy.com/v2/YOUR_API_KEY
```
