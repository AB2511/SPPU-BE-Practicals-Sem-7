// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BankAccount {
    mapping(address => uint256) public balances;

    // Deposit function
    function deposit() public payable {
        require(msg.value > 0, "Deposit must be > 0");
        balances[msg.sender] += msg.value;
    }

    // Withdraw function
    function withdraw(uint256 amount) public {
        require(amount <= balances[msg.sender], "Insufficient balance");
        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
    }

    // Show balance
    function getBalance() public view returns (uint256) {
        return balances[msg.sender];
    }
}
