# C2 — Create a personal wallet with MetaMask and perform transactions

1. Install the MetaMask extension from https://metamask.io.
2. Create a new wallet: set a password, then write down the 12-word Secret Recovery Phrase and confirm it.
   (Never share it. Anyone with it controls the wallet.)
3. Switch to the **Sepolia** test network (Settings → Advanced → Show test networks).
4. Copy your account address and request test ETH from a Sepolia faucet.
5. Create a second account: account menu → Add account.
6. Send ETH: Send → select/paste recipient address → enter amount → Next → Confirm.
7. Check the transaction: Activity tab → status (Pending → Confirmed), then open it on Sepolia Etherscan.
8. Verify the balances of both accounts changed (sender's decreases by amount + gas fee).


## Viva Questions

- **What is a cryptocurrency?** A digital currency secured by cryptography and managed by a decentralized network instead of a bank.
- **Coin vs token?** A coin runs on its own blockchain (ETH, BTC); a token is built on another blockchain via smart contracts (ERC-20 tokens).
- **What is a crypto wallet?** Software/hardware that stores your keys and lets you sign transactions. It does not literally hold coins; the balance lives on the blockchain.
- **What is MetaMask?** A non-custodial browser wallet for Ethereum and EVM networks that also connects to dApps.
- **Hot vs cold wallet?** Hot: connected to the internet (MetaMask). Cold: offline storage (hardware wallet), more secure.
- **What is the Secret Recovery Phrase and why keep it safe?** 12 words (BIP-39) that regenerate all accounts; if lost you lose access, if leaked you lose funds.
- **What is an HD wallet?** A hierarchical deterministic wallet derives many accounts from a single seed phrase.
- **Public key cryptography - how is a transaction authorized?** The sender signs the transaction with the private key; the network verifies the signature with the public key.
- **Why are accounts identified by addresses?** The address is a hash of the public key (0x + 40 hex characters).
- **Steps of a transaction?** Create -> sign -> broadcast -> pending in the mempool -> validator includes it in a block -> confirmed.
- **How do balances change after a send?** Sender loses amount + gas fee; receiver gains the amount.
- **What if a transaction is stuck pending?** Speed it up (higher gas) or cancel by sending a 0-ETH transaction with the same nonce.
- **What is a nonce?** Counter of an account's transactions; keeps ordering and prevents replay.
- **What is gas and who receives it?** Fee for computation; the priority fee goes to the validator and the base fee is burned.
- **Is a failed transaction charged?** Yes, gas for work done is still spent.
- **Why use a testnet?** To practise with valueless ETH (from a faucet) without risking real money.
- **How to add or switch networks in MetaMask?** Network dropdown -> add network (RPC URL, chain ID, symbol) or enable test networks in Settings.
- **How to add a second account?** Account menu -> Add account (derived from the same seed) or Import account (via private key).
- **What does decentralization / immutability mean?** No single authority controls the network; confirmed blocks cannot be altered.
- **What is double spending?** Spending the same coin twice; blockchain consensus prevents it.
- **Bitcoin vs Ethereum?** Bitcoin is mainly digital money (UTXO model); Ethereum is programmable (account model, smart contracts).
- **What is a consensus mechanism?** The rule by which nodes agree on the ledger (PoW, PoS).
