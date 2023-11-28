# Version Control and Testing
or 
## How _Not_ to Suck at Coding

1. What do tests really get us?
    1. Direction
        - Relying on user stories to drive functional tests and using unit tests to define code requirements can give you a focused path to completing a project.
        - When you follow the pattern of failing test -> code, you're always going to know where to pick back up
    2. Reliability
        - Having good code coverage reduces the risk of breaking code with future changes
        - Being able to run your tests quickly makes fixing bugs under pressure way easier
    3. Documentation
        - Well written tests are documentation. Don't know what a piece of code does? Look for the tests that exercise it.
2. Writing a test
    1. Functional tests
        - Branch `01-first-functional-test`
        - Functional or end-to-end tests tell us something about the behavior of an application, whether its a website, a mobile app, or an API
        - Functional test frameworks can help you maintain state, mimic user behavior, and even record animations to verify. Some examples are Selenium and Cypress
        - Functional tests often focus on the 'happy path', or the successful behavior of an app
        - sidebar: integration test as a term
    2. Unit tests
        - Branch `02-a-unit-test`
        - Unit tests are much smaller in scope, and are useful for fine-grained testing, error cases, and permutations
        - Unit test frameworks include Python's unittest, Java's Junit, and JavaScript's Jest
        - It's worth noting that Jest is a not-uncommon example of a test framework that isn't just limited to one or the other
    3. Other kinds of testing
        - Load testing: testing the ability of systems to handle a large number of events
        - Manual testing: good ol' eyeballs
        - Regression testing: running your test suites on a cycle to ensure no bugs are introduced (keep this in mind for later)
    4. Arrange, Act, Assert
        - Tests need to set up some state. Maybe that's starting up a server, initializing and creating a record in a database, or queueing up some messages to be consumed
        - The test then needs to make the code do the thing. This could be opening a browser to a page, starting a message consumer, or just calling a simple function
        - Finally, we need to check that the test did what we expect of it with assertions. Does that web page have the title we want? When the consumer read a message of the queue, did it store the data correctly? Did calling `add_me(1,2)` return 3!?
3. TDD and the SDLC
    1. Look up Extreme Programming. I'm not going to get into it, but that's where we get TDD
    2. TDD Cycle
        1. Write a failing test
        2. Make the minimum change to make the test pass _or fail a different way_
        3. Once the test succeeds, write a new test or expand the current
    3. If we have features we're working on, we can get more specific
        1. Branch `03-tests-and-sdlc`
            - Point out the common patterns in test case inheriting classes
        2. We've expanded our functional test to a proper user story
        3. That's our goal, and now we can test our way to success
        4. We write a _failing_ unit test to fulfill the smallest reasonable chunk of that feature
        5. Git commit as much as you need!
        6. Once it succeeds, rinse and repeat until the feature is done
    4. Now that we have a test, we can prevent regressions!
        1. What happens if I change some content? 
        2. Rename a function?
4. Useful git tools
    1. Git internals, at speed, with log
        - Also, read the docs. You need to get used to reading docs _today_
    1. status
        - What does each color/state mean
        - What does 'restore' or 'reset' do
    2. diff
        - How to read a diff
        - Compact summary
        - add -i
    3. stash
        - stash, stash push, stash pop
        - stash list
        - look, more meta refs
    4. checkout
        - checkout to move to another commit (detached head state thingy)
        - checkout to emulate cherry-pick
    5. commit --amend
        - oops...
    6. reflog
        - Git reference logs, hashes that point to references in code
        - HEAD@{2}
        - really useful if you aren't sure what branch you were working on last
    7. merge vs. rebase
        - tl;dr; unless you have a reason, merge
        - rebase is *destructive*, merge is not
        - one *really* good reason: cleaning up messy commit history
5. The 'Real World' if you can call it that
    1. Product teams, OKRs and roadmaps
    2. Jira and other project management tools
    3. Release cadences
    4. CI/CD and regression testing