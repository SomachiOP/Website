# Phase 1 Major Goals:
- Single page w/ `HTML` & `CSS`.
- Slick design 😎.
- Text displayed from a `markdown` file, which can be changed as needed to alter the text on the website.
- A compiler that can ideally handle multiple languages.
- A "Run" button that triggers an unchanging `test_cases/public.py` script. The script will:
> Take a list of test-case-inputs from a `test_cases/public.txt` file, <br>
> Pass them through to the code written on the compiler, <br>
> Display any compiler/run-time errors to the user as is, <br>
> Gather outputs and matches them with expected outputs also in `test_cases/public.txt` <br>
> In the event of unsuccessful matches, display all outputs paired with expected outputs, <br>
> In the event of no unsuccessful matches, display an appropriate message.
- Accordingly, develop a standard format for the `public.txt` test case file.
- A "Submit" button that will save the code to a local folder, trigger an unchanging `test_cases/private.py` script. The script will:
> Take a list of test-case-inputs from a `test_cases/private.txt` file, <br>
> Pass them through to the code saved on file, <br>
> Gather outputs and matches them with expected outputs also in `test_cases/private.txt` <br>
> Display the number of successful/unsuccessful cases.
## Phase 1 Extra Goals:
- Create an ID system, that requires users to enter an ID before being able to access the rest of the website.
- Submitted files will be filed under a folder titled `submissions/<ID>/`.
- Every such folder will have a `log.txt` folder that will be logged with various data:
> [Current time]: ID was logged <br>
> [Current time]: # of successful public tests upon hitting "Run" <br>
> [Current time]: # of successful private tests upon hitting "Submit" <br>
- Encrypt data stored and/or implement https protocol

This system, alongside the provided info will be used for the admin endpoint in future phases