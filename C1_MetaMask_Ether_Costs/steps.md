# C1 — Install MetaMask and examine Ether transaction costs

1. Install the MetaMask extension from https://metamask.io (Chrome/Firefox/Edge).
2. Create a wallet, set a password, and save the 12-word Secret Recovery Phrase offline.
3. Enable test networks: Settings → Advanced → Show test networks. Switch to **Sepolia**.
4. Get free test ETH from a Sepolia faucet.
5. Send a small amount of ETH to a second account (Send → paste address → amount).
6. On the confirm screen, examine the fee: **Gas fee = Gas used × Gas price (Gwei)**.
   - A plain ETH transfer uses 21,000 gas.
   - Compare Low / Market / Aggressive fee options.
7. After confirmation, open the tx in MetaMask Activity → View on block explorer (Sepolia Etherscan) and
   note: Transaction Hash, Gas Used, Gas Price, Transaction Fee, Block number.
8. Repeat with a different amount and a different fee level, and compare the fees of each transaction.


## Viva Questions

- **What is a blockchain?** A distributed, tamper-resistant ledger of transactions grouped into blocks, each linked to the previous one by a hash.
- **What is Ethereum / Ether?** Ethereum is a blockchain platform that runs smart contracts; Ether (ETH) is its native cryptocurrency, used to pay for transactions and computation.
- **What is MetaMask?** A non-custodial browser-extension wallet that stores your keys and connects you to Ethereum and dApps (acts as a Web3 provider).
- **Custodial vs non-custodial wallet?** Non-custodial: you hold the private keys (MetaMask). Custodial: a third party (e.g. an exchange) holds them.
- **Public key vs private key vs address?** Private key signs transactions (keep secret); the public key is derived from it; the address is derived from the public key and is what others send funds to.
- **What is the Secret Recovery Phrase?** A 12-word mnemonic (BIP-39) from which all your keys are generated. Anyone with it controls your funds.
- **What is gas?** The unit measuring computational work on Ethereum. Every operation costs gas; it prevents spam and pays validators.
- **Formula for the transaction fee?** Fee = Gas used x Gas price (in Gwei). With EIP-1559: Gas price = Base fee + Priority fee (tip).
- **What is EIP-1559?** The base fee is set by the network and burned; the priority fee (tip) goes to the validator; a max fee caps the total.
- **Gas limit vs gas used?** Gas limit = the maximum you allow; gas used = what the transaction actually consumed (unused gas is refunded). A plain ETH transfer uses 21,000 gas.
- **Why do fees differ between transactions?** Network congestion (base fee), your priority tip, and the complexity of the transaction (contract calls use more gas).
- **Units of Ether?** 1 ETH = 10^9 Gwei = 10^18 Wei.
- **What is a testnet? Why Sepolia?** A network with valueless ETH for testing without spending real money. Test ETH comes from a faucet.
- **Mainnet vs testnet?** Mainnet is the real network with real-value ETH; testnet is for development.
- **What is a nonce?** A per-account counter of sent transactions; it orders transactions and prevents replays.
- **What is a transaction hash?** A unique ID of a transaction, used to look it up on a block explorer like Etherscan.
- **Transaction states?** Pending -> Confirmed (included in a block) or Failed (fee is still charged for work done).
- **What is a block explorer?** A website (Etherscan) to view transactions, blocks, addresses and gas details.
- **Proof of Work vs Proof of Stake?** PoW: miners solve puzzles. PoS (Ethereum since 2022): validators stake ETH to propose/attest blocks; far less energy.
- **What is a smart contract?** Code stored on the blockchain that runs automatically when triggered by transactions.
- **EOA vs contract account?** An externally owned account is controlled by a private key; a contract account is controlled by its code.
- **What are Layer 2s?** Networks built on top of Ethereum (Arbitrum, Optimism) that give cheaper, faster transactions.
