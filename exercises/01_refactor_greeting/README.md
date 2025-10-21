# 01 – Refactor a function (keep tests passing)

**(Situation)**  
We have a working function that builds a greeting string, but the code is long, repetitive, and hard to read.

**(Task)**  
Refactor the function to be short, clear, and Pythonic **without changing behavior**. Do **not** edit the tests—your changes must keep them green.

**(Action)**  
Use an AI assistant to:  
- Identify smells (duplicated logic, unnecessary branches, odd naming).  
- Propose a cleaner design (small helpers, early returns, f-strings).  
- Generate a diff for a safe refactor.  
- Explain *why* the refactor is equivalent.

**(Result)**  
`pytest` still passes. The function is ~3–8 lines, easy to read, and has a clear docstring.
