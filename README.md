# Python Code Analyzer with Gemini AI

This project is a Python-based tool designed to analyze Python code for potential issues, style inconsistencies, and areas for improvement. It leverages the power of Google's Gemini AI to provide insightful feedback and suggestions.  The application uses a simple command-line interface for ease of use.

## Features

* **AI-Powered Code Analysis:** Employs Google Gemini AI to examine Python code.
* **Style and Best Practices Check:** Identifies deviations from PEP 8 style guidelines and suggests best practices.
* **Potential Bug Detection:**  Flags potential bugs and logic errors.
* **Code Clarity Suggestions:** Offers advice on improving code readability and maintainability.
* **Command-Line Interface:**  Easy-to-use command-line interface for submitting code and viewing results.
* **Detailed Reporting:** Provides a structured report of identified issues with explanations and suggestions.

## Tech Stack

* Python 🐍
* Google Generative AI (Gemini AI)
* `ast` module (for abstract syntax tree parsing)
* `click` (for command-line interface creation)
* `os` module (for environment variable handling and file I/O)

## How it Works

The tool takes a Python file as input.  It first parses the code into an Abstract Syntax Tree (AST) using Python's built-in `ast` module. This allows for structural analysis of the code. Then, it interacts with the Gemini AI API, providing the code and the AST representation. Gemini AI analyzes the code and returns a report containing findings. The tool processes this report and presents it to the user in a clear and organized format on the command line.

## Planned Features (Roadmap)

* Support for other programming languages.
* Integration with popular IDEs.
* Customizable rules and checks.
* Interactive mode for real-time feedback.
* Enhanced reporting with code snippets and visualisations.

## Getting Started

(Instructions on how to install and run the tool will be added here once the project is developed. This section will include details about dependencies, API keys, and usage examples.)
