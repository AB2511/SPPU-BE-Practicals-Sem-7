# 🧠 Blockchain Technology – Smart Contract Assignments

Savitribai Phule Pune University (SPPU)
**Course:** Laboratory Practice III (410246)
**Assignments Covered:**

* Assignment 3 – Bank Account Smart Contract
* Assignment 4 – Student Data Smart Contract

---

## 📘 Overview

This repository contains smart contracts developed as part of the **Blockchain Technology** module in the final year of Computer Engineering under the 2019 course structure.
The objective of these assignments is to gain hands-on experience in writing, deploying, and testing smart contracts using **Solidity**, **Remix IDE**, and **Ethereum test networks**.

Both assignments explore key blockchain principles — **immutability, transparency, and decentralization** — while emphasizing **secure and efficient smart contract design**.

---

## 🧩 Assignment 3 – Bank Account Smart Contract

### 🎯 **Objective**

To design and deploy a smart contract that acts as a simple decentralized bank, allowing users to:

* Deposit Ether
* Withdraw Ether
* Check their account balance

### ⚙️ **Concept**

This assignment focuses on understanding how **value transactions** occur on Ethereum.
Each user’s balance is tracked through their unique blockchain address, ensuring full transparency and control. The exercise reinforces:

* Use of `payable` functions for handling Ether.
* Proper state management using mappings.
* Validation mechanisms to prevent unauthorized or invalid transactions.

### 🧠 **Learning Outcomes**

* Hands-on experience in **handling Ether in Solidity**.
* Understanding **gas fees** and blockchain transaction flow.
* Application of **secure coding practices** to prevent vulnerabilities like reentrancy.
* Deployment and testing using **Remix IDE** and **MetaMask** connected to a test network.

---

## 🧩 Assignment 4 – Student Data Smart Contract

### 🎯 **Objective**

To develop and deploy a smart contract that manages student information using:

* **Structures (structs)**
* **Arrays**
* **Fallback and receive functions**

### ⚙️ **Concept**

This contract demonstrates how data can be stored and accessed on the blockchain using Solidity’s data structures.
It introduces the concept of **structured data storage**, and how contracts can also **receive Ether** through fallback and receive functions.

Students learn to:

* Define and use **custom data types** (structs).
* Maintain collections using **dynamic arrays**.
* Implement **fallback mechanisms** for handling unexpected transactions.

### 🧠 **Learning Outcomes**

* Understanding **data organization and persistence** in smart contracts.
* Differentiating between **storage** and **memory** in Solidity.
* Observing the **behavior of fallback and receive functions** during deployment.
* Building confidence in reading, interpreting, and interacting with on-chain data.

---

## ⚡ How to Run These Smart Contracts (Using Remix + MetaMask)

Follow these steps carefully 👇

---

### 🧩 **1️⃣ Open Remix IDE**

Go to:
👉 [https://remix.ethereum.org](https://remix.ethereum.org)

Remix is a browser-based IDE for Solidity — no installation needed.

---

### 🧩 **2️⃣ Create a New Workspace**

* On the left sidebar, click **File Explorer** → **Create New File**.
* Save inside the **contracts/** folder (Remix automatically creates one).

  * File 1: `BankAccount.sol`
  * File 2: `StudentData.sol`
* Paste the corresponding code into each file (one contract per file).
* Save changes (Ctrl + S).

---

### 🧩 **3️⃣ Compile the Code**

* In Remix sidebar, click the **Solidity Compiler** tab (S icon).
* Make sure the compiler version is **0.8.0 or higher** (for example: `0.8.20`).
* Click **Compile BankAccount.sol** and **Compile StudentData.sol** one by one.
  ✅ You should see “Compilation successful” without any errors.

---

### 🧩 **4️⃣ Connect MetaMask Wallet**

* Open **MetaMask** in your browser.
* Make sure you’re logged in and connected to a test network:

  * **Sepolia Test Network** (recommended) or
  * **Ganache** (local testing, optional).
* Get test ETH if using Sepolia: [https://sepolia-faucet.pk910.de/](https://sepolia-faucet.pk910.de/)

---

### 🧩 **5️⃣ Deploy the Contract**

#### In Remix:

* Go to the **Deploy & Run Transactions** tab (Ethereum icon).
* Under **Environment**, select:

  * `Injected Provider - MetaMask` ✅
  * (This connects Remix to your MetaMask wallet).
* Check the connected account address (it will appear in Remix).
* Make sure:

  * **Gas Limit:** ~3000000 (auto-filled)
  * **Value:** 0 (for deployment)
* Select the contract (either `BankAccount` or `StudentData`) from the dropdown.
* Click **Deploy** 🚀
* MetaMask will pop up → click **Confirm**.
* Wait until “Transaction mined” appears.

You’ll now see your deployed contract under **Deployed Contracts** at the bottom of Remix.

---

### 🧩 **6️⃣ Interact with the Contract**

#### For **Assignment 3: BankAccount.sol**

In the deployed contract:

* **Deposit ETH**

  * In the **Value** box → enter:
    `1000000000000000` (equals 0.001 ETH).
  * Click `deposit()`.
  * Confirm in MetaMask.
* **Check Balance**

  * Click `getBalance()` → output shows your balance (in Wei).
* **Withdraw**

  * Set Value = 0 (important).
  * Enter the same number in `withdraw(uint256 amount)`:
    `1000000000000000`
  * Click `withdraw()` → Confirm in MetaMask.

You can check all transactions in MetaMask → Activity tab.

---

#### For **Assignment 4: StudentData.sol**

In the deployed contract:

* **Add Student**

  * Enter sample values in `addStudent()` fields:

    * `_id`: `1`
    * `_name`: `Anjali`
    * `_age`: `21`
    * `_course`: `Computer Engineering`
  * Click **transact** → Confirm in MetaMask.
* **Get Student Count**

  * Click `getStudentCount()` → should show `1`.
* **View Student Details**

  * In `getStudent(index)` → enter `0` (for first student).
  * Click call → will return:

    ```
    0: uint256: 1
    1: string: Anjali
    2: uint8: 21
    3: string: Computer Engineering
    ```
* **Send Ether (optional)**

  * In the **Value** box → enter any amount (e.g., `1000000000000000`)
  * Click **Transact** (without selecting any function) → triggers fallback/receive.
  * Use `getContractBalance()` to confirm that ETH was received.

---

### 🧩 **7️⃣ Understanding the Environments (Choose One)**

| Environment Option                 | When to Use      | Description                                                                        |
| ---------------------------------- | ---------------- | ---------------------------------------------------------------------------------- |
| **JavaScript VM (London)**         | For testing only | Local simulated blockchain inside Remix (no MetaMask needed). Resets after reload. |
| **Injected Provider - MetaMask** ✅ | Recommended      | Connects Remix to your MetaMask account (e.g., Sepolia or Ganache network).        |
| **Web3 Provider**                  | Advanced users   | Connects Remix to a remote blockchain node (HTTP RPC URL).                         |

✅ **Use “Injected Provider - MetaMask”** for official submission or demo — it shows real transaction confirmations and gas usage.

---

### 🧩 **8️⃣ Observing Transactions**

You can see:

* Contract Address
* Gas used
* Transaction hash
  on **Etherscan** (for Sepolia network).

Each function call updates blockchain state permanently.

---

### 🧩 **9️⃣ Optional – View on Ganache (Local)**

If you prefer running locally:

* Start Ganache → copy the RPC URL (usually `HTTP://127.0.0.1:7545`).
* Add a new network in MetaMask (Custom RPC).
* Select **Web3 Provider** in Remix → enter the same RPC URL.
* Deploy and test in your private blockchain environment.

---

### 🏁 **That’s It!**

You’ve now:
✅ Written the contract
✅ Compiled it
✅ Deployed it to blockchain
✅ Interacted with it using real transactions

---

## ⚙️ **Tools & Technologies Used**

| Tool                          | Purpose                                              |
| ----------------------------- | ---------------------------------------------------- |
| **Remix IDE**                 | Writing, compiling, and deploying smart contracts    |
| **MetaMask**                  | Ethereum wallet integration for signing transactions |
| **Ganache / Sepolia Testnet** | Local or public blockchain testing                   |
| **Solidity (v0.8.x)**         | Smart contract development language                  |

---

## 🔍 **General Observations**

* Every blockchain interaction consumes **gas**, proportional to computational complexity.
* Functions marked as `view` or `pure` do **not** consume gas when called locally.
* Proper state validation (`require` statements) ensures security and prevents unwanted behavior.
* Smart contracts deployed on a test network remain **permanently recorded** and verifiable.

---

## 🏁 **Conclusion**

Both assignments provide foundational skills in **blockchain programming** using Solidity.
They demonstrate how smart contracts can manage:

* **Value (BankAccount)** and
* **Data (StudentData)**
  on a decentralized network securely and transparently.

These experiments serve as a stepping stone for building more complex decentralized applications (DApps) such as supply chain tracking, identity verification, and e-voting systems.

---

## 📂 **Repository Structure**

```
📦 BCT
 ┣ 📜 BankAccount.sol
 ┣ 📜 StudentData.sol
 ┗ 📄 README.md
```
