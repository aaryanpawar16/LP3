// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    struct Student {
        uint256 id;
        string name;
        uint256 marks;
    }

    Student[] public students; // array of structures

    event FallbackCalled(address sender, uint256 value, bytes data);

    function addStudent(uint256 id, string memory name, uint256 marks) public {
        students.push(Student(id, name, marks));
    }

    function getStudent(uint256 index) public view returns (uint256, string memory, uint256) {
        Student memory s = students[index];
        return (s.id, s.name, s.marks);
    }

    function totalStudents() public view returns (uint256) {
        return students.length;
    }

    // Runs when an unknown function is called or ether is sent with no matching function
    fallback() external payable {
        emit FallbackCalled(msg.sender, msg.value, msg.data);
    }
}

// Deploy via Remix (Injected Provider - MetaMask, Sepolia). Gas and fees: check the Remix console
// (gas / transaction cost / execution cost) and the transaction on Sepolia Etherscan.
// Trigger fallback: send a low-level transaction with calldata (e.g. "0x1234") from Remix's Low level interactions.


// ======================= VIVA QUESTIONS =======================
// Q: What is a struct in Solidity?
// A: A user-defined type grouping related fields (id, name, marks) into one record.
// Q: What are dynamic and fixed-size arrays?
// A: Dynamic (Student[]) can grow with push(); fixed-size (Student[10]) has a set length.
// Q: What does a public array give you?
// A: The compiler auto-generates a getter students(index) that returns the struct fields.
// Q: What is a fallback function?
// A: A special function (fallback() external payable) executed when a call matches no function signature,
//    or when Ether is sent with data and no receive() exists.
// Q: fallback() vs receive()?
// A: receive() handles plain Ether transfers with empty calldata; fallback() handles everything else
//    (unknown functions, or Ether if receive is absent).
// Q: Why is the fallback marked payable?
// A: So it can accept Ether; otherwise Ether sent to it would revert.
// Q: What is msg.data?
// A: The complete calldata of the call; the fallback receives it for unmatched calls.
// Q: What are events?
// A: Logs written to the blockchain (cheaper than storage) that off-chain apps can listen to.
// Q: Why use memory for the string parameter?
// A: Strings are reference types, so you must declare their location; memory is temporary and cheaper than storage.
// Q: How do you read a student record?
// A: getStudent(index) returns (id, name, marks) from the array.
// Q: How is gas calculated?
// A: Gas used x gas price. Writing to storage (new slot ~20,000 gas) dominates the cost; strings and arrays cost more.
// Q: transaction cost vs execution cost in Remix?
// A: Transaction cost = total gas including the 21,000 base cost and calldata;
//    execution cost = gas consumed by running the code only.
// Q: Why is the deployment cost high?
// A: It stores the contract bytecode on-chain (about 200 gas per byte plus the base cost).
// Q: Why is addStudent costlier than getStudent?
// A: addStudent changes storage and is a transaction; getStudent is a view call (free off-chain).
// Q: Array vs mapping?
// A: Array: ordered and iterable but loops cost gas and removal is awkward; mapping: O(1) lookup by key but not iterable.
// Q: Risk of looping through a large array on-chain?
// A: Gas can exceed the block limit and the call fails (denial of service); avoid unbounded loops.
// Q: How do you delete an element?
// A: Swap with the last element and pop(), or use delete (which only resets the slot to default values).
// Q: What does students.length return?
// A: The number of elements in the array (used by totalStudents()).
// Q: How do you test the fallback in Remix?
// A: Use "Low level interactions" -> send calldata (e.g. 0x1234) to the contract; the FallbackCalled event appears in the logs.
// Q: How to deploy on a testnet?
// A: Compile in Remix -> Deploy & Run -> Environment: Injected Provider (MetaMask on Sepolia) -> Deploy -> confirm in MetaMask.
