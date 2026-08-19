# How to Create Community Badges

This guide explains how third-party DAOs, NFT projects, and Web3 protocols can deploy custom ERC-1155 badge contracts using Society Protocol's **CommunityWrapperFactory** (`0x84ffd2805af9d0946e02Fe19Cd1eE58228669B0e`).

---

## 💡 Overview

Deploying custom badges through the factory provides your project with instant compatibility across Society Protocol's ecosystem:

* **No Smart Contract Coding:** Initialize permissioned ERC-1155 badges via single factory calls.
* **Automatic Registry Indexing:** Deployed wrappers register immediately in `CommunityRegistry` (`0xEa00...EB76`).
* **Custom Minting & Transfer Rules:** Define whether your badges are soulbound, burnable, or transferable.

---

## 🛠️ Deployment Methods

### Method 1: Web Interface (Recommended)

1. Navigate to the **[Community Developer Console](https://app.societyprotocol.io/badges)** (accessible once logged in).

2. Connect your community admin wallet (or Safe multisig).

3. Fill out your community metadata:
   * **Community Name:** (e.g. *Acme DAO*)
   * **Badge Symbol:** (e.g. *ACME*)
   * **Base URI:** `ipfs://.../` (Metadata directory URI)

4. Select permission flags (Mintable by admin, Transferable, Burnable).

5. Click **Deploy Community Wrapper** and execute the transaction.

---

### Method 2: Smart Contract Interaction (CLI / Foundry / Hardhat)

Developers can interact directly with `CommunityWrapperFactory` at `0x84ffd2805af9d0946e02Fe19Cd1eE58228669B0e`.

```solidity
// Interface Excerpt
interface ICommunityWrapperFactory {
    function createCommunityWrapper(
        string memory name,
        string memory symbol,
        string memory baseURI,
        address admin,
        bool isSoulbound
    ) external returns (address wrapperAddress);
}
```

#### Example Deployment via Foundry Cast:

```bash
cast send 0x84ffd2805af9d0946e02Fe19Cd1eE58228669B0e \
  "createCommunityWrapper(string,string,string,address,bool)" \
  "Acme Community" "ACME" "ipfs://QmYourHash/" 0xYourAdminAddress true \
  --rpc-url https://eth-mainnet.g.alchemy.com/v2/YOUR_API_KEY \
  --private-key $PRIVATE_KEY
```

---

## ⚙️ Post-Deployment Management

Once deployed:

1. **Minting Badges:** The assigned admin address can call `mintBadge(address to, uint256 id, uint256 amount)` on the returned `CommunityWrapper` instance.

2. **Hook Integration:** Attach optional hooks (e.g. `SingleMintHook` or custom gating logic) to restrict issuance parameters.
