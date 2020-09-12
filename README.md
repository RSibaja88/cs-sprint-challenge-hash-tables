# Sprint Challenge: Hash Tables

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This challenge allows you to practice the concepts and techniques learned over the past sprint and apply them in a concrete project. This sprint explored hash tables. During this sprint, you studied hash functions, collision resolution, complexity analysis of hash tables, load factor, resizing, and various use cases for hash tables. In your challenge this week, you will demonstrate mastery of these skills by solving five problems related to hash tables.

The sprint challenge is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the sprint challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your TL if you need direction.

_You have **three hours** to complete this challenge. Plan your time accordingly._

## Introduction

This challenge requires you to solve algorithm problems that are amenable to being solved efficiently with a hash table.

### Commits

Commit your code regularly and meaningfully. This practice helps both you (in case you ever need to return to old code for any number of reasons) and your Team Lead as they evaluate your solution.

## Interview Questions

Be prepared to demonstrate your understanding of this week's concepts by answering questions on the following topics. You might prepare by writing down your answers beforehand.

1. Hashing functions
   A hash table is a data structure that has ability to map keys to values. It uses a hash function to compute an index into an array in which an element will be inserted or searched. A hash table is of a defined size, and because its a defined size, collisions can occur. A good hash function would minimize collisions while hopefully keeping constant runtime.

2. Collision resolution
   When two items hash to the same slot, we must have a systematic method for placing the second item in the hash table. This process is called collision resolution. This can be approached by Separate Chaining, or Open Addressing.

   Separate Chaining- In order to handle the collision, we must create a linked list to the slot for which collision occurs. A new key is then inserted in the linked list.These linked lists to the slots appear like chains. That is why, this technique is called as separate chaining.

   Open Addressing- With this method a hash collision is resolved by probing, or searching through alternate locations in the array (the probe sequence) until either the target record is found, or an unused array slot is found, which indicates that there is no such key in the table

3. Performance of basic hash table operations
   Search, add, edit, delete should be O(1) (constant time), but with many collisions, could be a worst case of 0(n) - linear time.

4. Load factor
   The load factor is the number of keys stored in the hash table divided by the capacity. The size should be chosen so that the load factor is less than 1

5. Automatic resizing
   Hash tables perform well if the number of elements in the table remain proportional to the size of the table. If we know exactly how many inserts/deletes are going to be performed on a table, we would be able to set the table size appropriately at initialization. When a hash table calculates the load factor after we add or delete and then resizes accordingly, it is automatically resizing

6. Various use cases for hash tables
   Storing anything where you need access based on a non integer.
   Storage where insertion and access both need to be fast.
   Storage where uniqueness is useful.
   Storing anything where order does not matter but access speed does.

We expect you to be able to answer questions in these areas. Your responses contribute to your Sprint Challenge grade.

## Instructions

### Task 1: Project Set-Up

- [ ] Create a forked copy of this project
- [ ] Add your team lead as a collaborator on Github
- [ ] Clone your OWN version of the repository (Not Lambda's by mistake!)
- [ ] Create a new branch: git checkout -b `<firstName-lastName>`.
- [ ] Implement the project on your newly created `<firstName-lastName>` branch, committing changes regularly
- [ ] Push commits: git push origin `<firstName-lastName>`

### Task 2: Project Requirements

Your finished project must include all of the following requirements:

- [ ] Solve any three of the five problems

For each problem that you choose to solve, complete the following:

- [ ] Navigate into each exercise's directory
- [ ] Read the instructions for the exercise in the README
- [ ] Implement your solution in the `.py` skeleton file
- [ ] Make sure your code passes the tests running the test script with make tests

_Note: For these exercises, we expect you to use Python's built-in `dict` as a hashtable. That said, if you wish, you can attempt to solve using your own hashtable implementation, as well. All solutions should utilize a `dict` or hashtable. You should not use Sets. (Though you can make a `dict` behave like a set if you wish.)_

### Task 3: Stretch Goals

After finishing your required elements, you can push your work further. These goals may or may not be things you have learned in this module, but they build on the material you just studied. Time allowing, stretch your limits, and see if you can deliver on the following optional goals:

- [ ] Solve any four of the five problems
- [ ] Solve all five problems

## Submission format

Follow these steps to complete your project.

- [ ] Submit a Pull-Request to merge <firstName-lastName> Branch into master (student's Repo). **Please don't merge your own pull request**
- [ ] Add your team lead as a reviewer on the pull-request
- [ ] Your team lead will count the project as complete after receiving your pull-request
