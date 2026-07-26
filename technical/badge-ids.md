# Badge ID Registry

All official badges are minted as **ERC-1155** tokens under the `SocietyProtocolBadges` proxy (`0x2313C0cDdc233c92d16c2cfE17DF5fDCcE556763`).

---

## 📋 Official Badge ID Registry Table

| Badge Name | Badge ID | Mint Rule / Privilege | Transferability | Target Audience |
| :--- | :---: | :--- | :---: | :--- |
| **DAO Badge** | `11` | Protocol Governance Access | Soulbound | DAO Members |
| **Security Council Badge** | `12` | Security Council Multisig Keyholder | Soulbound | Security Council Keys |
| **Governor Badge** | `13` | Meritocratic DAO Voting Seat | Soulbound | Appointed Governors |
| **Bronze VIP Badge** | `14` | Access to Bronze VIP Channels | Locked via SPEC | Outpost Members |
| **Silver VIP Badge** | `15` | Access to Silver VIP Channels | Locked via SPEC | Outpost Members |
| **Gold VIP Badge** | `16` | Access to Gold VIP Channels | Locked via SPEC | Outpost Members |
| **Advisor Badge** | `24` | Strategic Advisor Recognition | Soulbound | Protocol Advisors |
| **Core Team Badge** | `25` | Awarded after 6 months of service | Soulbound | Full-Time Core Team |
| **Contributor / Builder Badge** | `26` | Code / Research Contribution | Soulbound | Ecosystem Developers |
| **ICO Participant Badge** | `27` | Fundraiser Contribution | Soulbound | Early Backers |
| **Moderator Badge** | `28` | Outpost Forum / Channel Moderator | Soulbound | Community Ops |

---

## 🔍 Cast Query Example

```bash
cast call 0x2313C0cDdc233c92d16c2cfE17DF5fDCcE556763 \
  "balanceOf(address,uint256)(uint256)" \
  <USER_WALLET_ADDRESS> <BADGE_ID> \
  --rpc-url https://eth-mainnet.g.alchemy.com/v2/YOUR_API_KEY
```
