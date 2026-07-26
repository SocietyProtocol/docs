# Badges Overview & Permissions

Society Protocol badges are categorized into **Official Badges** (issued by the SP DAO) and **Community Badges** (issued by partner protocols via Community Wrappers).

---

## 🎖️ Meritocratic DAO vs. SPEC Holders

A critical design principle of Society Protocol is the separation between **meritocratic governance** and **economic contribution**:

* **DAO Governors (Governor Badges):** The SP DAO is a meritocracy governed by accountable core team members, strategic advisors, and partner communities holding **Governor Badges**. It explicitly avoids pseudonymous token-based voting to prevent sybil attacks and treasury capture.
* **SPEC Token Holders:** SPEC holders participate in economic alignment, VIP channels, and community feedback polls, while qualifying for Genesis Energy distributions in Web4 instances.

---

## 🔐 The 4 ERC-1155 Permissions Explained

Permissions control who can issue, destroy, move, or configure badges within the system:

### 1. 🪙 Mint Permission
* **Definition:** The authority to create new instances of a specific Badge ID and assign them to recipient addresses.
* **Official Badges:** Held by the **SP DAO Safe** (`0xdfdC...7579`) or automated hooks (e.g. zkTLS verification or SPEC locking vaults).
* **Community Badges:** Held by the community's admin address or custom wrapper contract.

### 2. 🔥 Burn Permission
* **Definition:** The authority to destroy existing badges from an account.
* **Official Badges:** Restricted to self-burn by the holder or revocation by the **Security Council Safe** (`0xCc4F...98AC`) during operational offboarding.
* **Community Badges:** Configured by the community wrapper owner.

### 3. 🔄 Transfer Permission
* **Definition:** The ability to transfer a badge between accounts.
* **Official Badges:** Most official badges are **Soulbound** (Transfer disabled) to preserve credential integrity. VIP Badges follow SPEC lockup rules.
* **Community Badges:** Configurable upon wrapper initialization.

### 4. 🛠️ Manage Permission
* **Definition:** Admin control over badge metadata URIs, royalties, and hook attachments.
* **Official Badges:** Governed by the SP DAO Safe.
* **Community Badges:** Managed by the community admin via `CommunityRegistry` (`0xEa00...EB76`).

---

## 📊 Permission Matrix Comparison

| Permission | Official Badges (System Default) | Community Badges (Wrapper Default) |
| :--- | :--- | :--- |
| **Mint** | SP DAO / Verification Hooks | Community Admin / Custom Hook |
| **Burn** | Holder (Self) / Security Council | Holder / Community Admin |
| **Transfer** | Disabled (Soulbound) | Configurable (Default: Allowed) |
| **Manage** | SP DAO Multisig | Community Deployer / Multisig |
