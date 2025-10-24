1. Which issues were the easiest to fix, and which were the hardest? Why?
The easiest issues were stylistic ones like blank lines, naming, and unused imports, as they only required minor edits. The hardest were logic and security issues such as bare except blocks, global variables, and eval(), which needed careful handling to avoid breaking functionality.

2. Did the static analysis tools report any false positives? If so, describe one example.
Yes, there were false positives; for example, Pylint suggested converting lazy % logging to f-strings, but lazy formatting is actually preferred for performance.

3. How would you integrate static analysis tools into your actual software development
workflow? Consider continuous integration (CI) or local development practices.
Static analysis can be integrated by running tools locally before commits and including them in CI pipelines to automatically check for style, security, and logic issues.

4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
After fixes, the code is more readable, maintainable, and robust, with safer error handling, consistent formatting, proper input validation, and secure data handling.
