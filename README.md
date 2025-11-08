DICTIONARY APP (ENGLISH)

The following project aims to showcase my capabilities using Python for building a graphical user interfaces and API integration, allowing users to search for English word definitions in an intuitive graphical interface, utilizing:

- PyQt6;
- REST API (more specifically, Free Dictionary API, available here: https://freedictionaryapi.com/);

The project had the following requirements:
- create a program that takes as input, words in English and return the definitions of those words;
- the program must have a desktop GUI;
- you can use a JSON dataset or REST API to get the definitions of English words;

How it works:

**User Input**  
   - The user types a word into a `QLineEdit` input field.  
   - When the **Search** button is clicked (or later, when Enter is pressed), a function named `show_definitions()` is triggered.

**Fetching Definitions**  
   - The `show_definitions()` function calls an external helper function `word_result()` (from `functions.py`).  
   - This helper function looks up the entered word — it could use an API, a local dataset, or another source to find dictionary entries.

**Processing Results**  
   - The returned data (a list of word entries) is parsed to extract definitions.  
   - If no entries are found, a friendly error message is displayed instead.

**Displaying Output**  
   - The resulting definitions are displayed inside a `QLabel`.  
   - The window automatically resizes itself to fit the content using `adjustSize()`, keeping the UI responsive and clean.

**Clearing Results**  
   - When the **Clear** button is pressed, both the input field and the output label are cleared.  
   - The window resets to its original compact size.

Future improvements:
- Search by pressing the Enter key instead of only clicking the button
- Multi-language support — add translation or multilingual dictionary integration
- Package as a standalone .exe using PyInstaller for easy distribution
- Add word pronunciation, synonyms, and examples

Contributions, issues, and feature requests are always welcome!
Feel free to open a pull request or suggest improvements.


rafadev096@gmail.com 