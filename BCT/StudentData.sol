// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract StudentData {

    struct Student {
        uint256 id;
        string name;
        uint8 age;
        string course;
    }

    Student[] public students;
    event StudentAdded(uint256 id, string name);

    function addStudent(uint256 _id, string memory _name, uint8 _age, string memory _course) public {
        Student memory newStudent = Student({
            id: _id,
            name: _name,
            age: _age,
            course: _course
        });
        students.push(newStudent);
        emit StudentAdded(_id, _name);
    }

    function getStudentCount() public view returns (uint256) {
        return students.length;
    }

    function getStudent(uint256 index) public view returns (uint256, string memory, uint8, string memory) {
        require(index < students.length, "Invalid index");
        Student storage s = students[index];
        return (s.id, s.name, s.age, s.course);
    }

    // Accept plain ETH transfers
    receive() external payable {}
    fallback() external payable {}

    function getContractBalance() public view returns (uint256) {
        return address(this).balance;
    }
}
