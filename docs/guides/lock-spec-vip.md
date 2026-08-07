# How to Lock SPEC to Get VIP Badges

This step-by-step tutorial guides community members on how to lock **SPEC tokens** (`0x6AcD...18BA`) to claim **Bronze**, **Silver**, or **Gold** VIP Badges and unlock access to token-gated communication rooms.

---

## 📱 Prerequisites

Before starting, ensure you have:

1. An Ethereum Web3 Wallet (e.g. MetaMask, WalletConnect, Rabby).

2. Sufficient ETH for Mainnet gas fees.

3. Sufficient **SPEC tokens** in your wallet for your desired VIP Tier:
   * **Bronze VIP (ID: 14):** 1,000 SPEC (30 days minimum lockup)
   * **Silver VIP (ID: 15):** 10,000 SPEC (90 days minimum lockup)
   * **Gold VIP (ID: 16):** 100,000 SPEC (180 days minimum lockup)

---

## 🛠️ Step-by-Step Tutorial

### Step 1: Access the Society Protocol Portal
Navigate to the official dApp interface:
👉 **[Society Protocol Portal (https://app.societyprotocol.io/vip)](https://app.societyprotocol.io/vip)**

> [!CAUTION]
> Always verify the URL and ensure your browser is connected to Ethereum Mainnet before signing transactions.

### Step 2: Connect Your Wallet

1. Click **Connect Wallet** in the top right corner.

2. Select your Web3 provider (MetaMask, Coinbase Wallet, etc.).

3. Authenticate the session signature request.

### Step 3: Approve SPEC Token Lockup
Smart contracts require your explicit approval before transferring SPEC tokens into the lockup vault:

1. Select your target VIP Tier (Bronze, Silver, or Gold).

2. Click **Approve SPEC**.

3. Confirm the ERC-20 token approval transaction in your wallet UI.

### Step 4: Lock SPEC & Mint VIP Badge

1. Once the approval transaction is confirmed, click **Lock SPEC & Claim Badge**.

2. Review the transaction parameters:
   * **Lock Duration:** Selected duration (e.g. 90 days for Silver).
   * **Badge ID:** Target ERC-1155 token ID (e.g. `15`).

3. Confirm the transaction in your wallet.

### Step 5: Verify Badge Receipt & Join VIP Channels
After transaction confirmation on Ethereum Mainnet:

* Your wallet will instantly receive the corresponding ERC-1155 VIP Badge (`SocietyProtocolBadges` proxy: `0x2313...6763`).
* Connect your wallet to Discord or Telegram via our verification bot to automatically claim your VIP roles.

---

## 🔓 How Unlocking Works

* When your lockup period expires, you can visit the **My Vaults** section on the portal to withdraw your SPEC tokens.
* **Important:** Withdrawing your locked SPEC tokens automatically **burns** your VIP Badge, forfeiting channel access until tokens are re-locked.
