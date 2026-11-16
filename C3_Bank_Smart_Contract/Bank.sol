// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Bank {
    mapping(address => uint256) private balances;

    function deposit() public payable {
        require(msg.value > 0, "Send some ether");
        balances[msg.sender] += msg.value;
    }

    function withdraw(uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount; // update state before sending ether
        (bool ok, ) = payable(msg.sender).call{value: amount}("");
        require(ok, "Transfer failed");
    }

    function showBalance() public view returns (uint256) {
        return balances[msg.sender];
    }
}

// Deploy: Remix IDE -> compile (0.8.x) -> Deploy & Run -> Environment: Injected Provider (MetaMask, Sepolia).
// Deposit: enter value in the Value field, click deposit. Then call withdraw(amount) and showBalance().


// ======================= VIVA QUESTIONS =======================
// Q: What is a smart contract and what is Solidity?
// A: A smart contract is self-executing code on the blockchain; Solidity is the language for writing contracts for the EVM.
// Q: What does pragma solidity ^0.8.0 mean?
// A: The code compiles with compiler versions 0.8.0 up to (not including) 0.9.0.
// Q: What is SPDX-License-Identifier?
// A: A comment declaring the license of the code; the compiler warns if it is missing.
// Q: What is mapping(address => uint256)?
// A: A key-value store (hash table) mapping each user address to their balance; unset keys return 0.
// Q: What are msg.sender and msg.value?
// A: msg.sender = address calling the function; msg.value = amount of wei sent with the call.
// Q: What does the payable keyword do?
// A: Lets a function receive Ether. Without it, sending Ether to the function is rejected.
// Q: What is require()?
// A: Checks a condition; if false, the transaction reverts (state changes undone) with the message and unused gas is refunded.
// Q: require vs assert vs revert?
// A: require validates inputs/conditions; assert checks internal invariants (should never fail); revert aborts explicitly.
// Q: What does the view keyword mean?
// A: The function only reads state and does not modify it; calling it off-chain costs no gas.
// Q: Why is the balance updated before sending Ether in withdraw?
// A: To prevent reentrancy attacks (checks-effects-interactions pattern).
// Q: What is a reentrancy attack?
// A: A malicious contract calls withdraw again from its fallback before the balance is reduced and drains the funds.
// Q: transfer vs send vs call?
// A: transfer: 2300 gas, reverts on failure. send: 2300 gas, returns false. call: forwards all gas, returns bool
//    (recommended now, always check the result).
// Q: Visibility specifiers?
// A: public (anywhere), external (outside only), internal (this contract + derived), private (this contract only).
// Q: memory vs storage vs calldata?
// A: storage = permanent on-chain state; memory = temporary during execution; calldata = read-only function arguments.
// Q: Does private mean the data is secret?
// A: No - it only blocks other contracts; all on-chain data is publicly readable.
// Q: Does Solidity 0.8 have overflow protection?
// A: Yes, arithmetic is checked and reverts on overflow/underflow.
// Q: What is the EVM, ABI and bytecode?
// A: EVM = virtual machine that executes contracts; bytecode = compiled code deployed on-chain;
//    ABI = interface description used to call the contract's functions.
// Q: What is Remix IDE and "Injected Provider"?
// A: Remix = browser IDE to write, compile and deploy contracts. Injected Provider connects Remix to MetaMask
//    (JavaScript VM is a local simulated blockchain).
// Q: Which functions cost gas?
// A: Anything that changes state (deposit, withdraw) costs gas; view calls are free off-chain.
// Q: What happens when a user withdraws more than their balance?
// A: require fails -> transaction reverts with "Insufficient balance".
// Q: How do you find your deposit in the contract?
// A: Call showBalance() from the same account, since it reads balances[msg.sender].
// Q: What are events and constructors (possible follow-ups)?
// A: Events log data to the blockchain for off-chain apps; a constructor runs once at deployment.
