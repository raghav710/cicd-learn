### Let's understand why CI/CD is important! (and useful)

1. Pick up the monolith_calculator HTML from 1.1.2, but in Python (attached)
2. Change it so that it supports string concatenation i.e. "a" + "b" should be "ab"
3. Now to test this you have to test add with numbers, add with strings, and then the other operations with numbers
4. Now let's say I introduce a new requirement of multiplication where a * 2 is "aa". Now you need to test multiplication as well with numbers and strings
5. The list goes on increasing! if it takes you 5 minutes to test this and there are 50 developers making changes, you are going to take 5 * 50 = 250 mins to test all their changes
6. With CI, you can write tests (to start with, unit tests) that will ensure your code is not breaking the project and the work is not breaking you!
7. Refer to the attached calc.py and test.py to see how tests help you stay sane with your codebase!
8. The process of running the tests on every change is "integration"
9. Once you've tested, "deploying" the code to the user is "deployment"
10. How to make this continuous? stay tuned for the next chapters...