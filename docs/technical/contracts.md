# Smart Contracts

Canonical reference table for deployed smart contracts, proxies, implementations, hooks, and multisig vaults governing the Web3 Outpost on Ethereum Mainnet.

---

## 🌐 Deployed Network: Ethereum Mainnet

> **Network:** Ethereum Mainnet  
> **Chain ID:** 1

| Contract Name | Type | Address | Etherscan Link |
| :--- | :--- | :--- | :--- |
| **SP DAO Safe** | Multisig | `0xdfdC9DBfDCd87F79636Ef8008B2Ccc5050F27579` | [View Address](https://etherscan.io/address/0xdfdC9DBfDCd87F79636Ef8008B2Ccc5050F27579) |
| **Security Council Safe** | Multisig | `0xCc4Fe7fD6a9a77574B0Ede442a5b63a5340498AC` | [View Address](https://etherscan.io/address/0xCc4Fe7fD6a9a77574B0Ede442a5b63a5340498AC) |
| **SPEC Token** | ERC-20 | `0x6AcD7735B3acF0DD677332a599FFfF71C18818BA` | [View Address](https://etherscan.io/address/0x6AcD7735B3acF0DD677332a599FFfF71C18818BA) |
| **SocietyProtocolBadges** | Proxy | `0x2313C0cDdc233c92d16c2cfE17DF5fDCcE556763` | [View Address](https://etherscan.io/address/0x2313C0cDdc233c92d16c2cfE17DF5fDCcE556763) |
| **SocietyProtocolBadges** | Implementation | `0x924F6Bc77089e1aa0333BCF4a9f698112734a3c2` | [View Address](https://etherscan.io/address/0x924F6Bc77089e1aa0333BCF4a9f698112734a3c2) |
| **CommunityWrapper** | Implementation | `0xc5934fF808e4D7b06d2f3D4fc722B7Cc543Be3E1` | [View Address](https://etherscan.io/address/0xc5934fF808e4D7b06d2f3D4fc722B7Cc543Be3E1) |
| **CommunityWrapperFactory** | Proxy | `0x84ffd2805af9d0946e02Fe19Cd1eE58228669B0e` | [View Address](https://etherscan.io/address/0x84ffd2805af9d0946e02Fe19Cd1eE58228669B0e) |
| **CommunityWrapperFactory** | Implementation | `0xF29a695E3002dCEd30DE82d1C53e5AE68195E939` | [View Address](https://etherscan.io/address/0xF29a695E3002dCEd30DE82d1C53e5AE68195E939) |
| **CommunityRegistry** | Proxy | `0xEa008f15E1454C79D6AA7B95Dd3E1d39Ba32EB76` | [View Address](https://etherscan.io/address/0xEa008f15E1454C79D6AA7B95Dd3E1d39Ba32EB76) |
| **CommunityRegistry** | Implementation | `0xBa7D6bD750f5D8Fe95c20738d8927BD999605fB4` | [View Address](https://etherscan.io/address/0xBa7D6bD750f5D8Fe95c20738d8927BD999605fB4) |
| **SingleMintHook** | Hook | `0xc5cA371c5F715E9d420941C1377e7682780bFC6D` | [View Address](https://etherscan.io/address/0xc5cA371c5F715E9d420941C1377e7682780bFC6D) |

---

## 🏗️ Architectural Overview

1. **ERC-1967 Proxies:** Core contracts (`SocietyProtocolBadges`, `CommunityWrapperFactory`, `CommunityRegistry`) use transparent proxies. Integrations interact exclusively with proxy addresses.

2. **Multisig Safes:** Treasury and contract upgrades are managed by the **SP DAO Safe** (`0xdfdC...7579`). Emergency circuit breakers are managed by the **Security Council Safe** (`0xCc4F...98AC`).

3. **Hooks:** `SingleMintHook` (`0xc5cA...FC6D`) enforces strict single-token limits per account for soulbound badges.
