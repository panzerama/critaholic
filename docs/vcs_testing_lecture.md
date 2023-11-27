1. Functional Test, aka End to End test
2. Unit test
3. Testing Process
    1. Arrange-Act-Assert
    2. Scope of each test
4. Testing Cycle
    1. Write a failing functional test
    2. Write a failing unit test
    3. Minimal code to make test succeed
    4. Write new unit test
    5. Repeat 2-4 until functional test passes
    6. Write new functional test
5. Software Development Lifecycle 
    2. Product Feature
    2. User Story
    3. Functional Test
    4. Hack on it
    5. Tests Pass
    6. Release

- what happens when we don't have a 'user' per se?
## User Story as a Functional Test


User Story
A description of how the application will work from the point of view of the user. Used to structure a functional test.

Expected failure
When a test fails in the way that we expected it to.

FTs	Unit Tests
One test per feature / user story

Many tests per feature

Test from the user’s point of view

Test the code, ie the programmer’s point of view

Can test that the UI "really" works

Tests the internals, individual functions or classes

Provides confidence that everything is wired together correctly, works end-to-end

Can exhaustively check permutations, details, edge cases

