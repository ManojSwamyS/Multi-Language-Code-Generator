# Multi-Language Code Generator

A Streamlit web application that leverages Google's Gemini AI to generate code snippets in multiple programming languages, including C, C++, C#, Java, and Python. This tool allows users to input natural language prompts and receive tailored code outputs, with options to refine the generated code based on additional specifications.

## Features

- **Multi-Language Support**: Generate code in C, C++, C#, Java, or Python.
- **Natural Language Prompts**: Describe your code requirements in plain English.
- **Code Refinement**: Improve generated code by adding specifications or modifications.
- **User-Friendly Interface**: Built with Streamlit for an intuitive web-based experience.
- **AI-Powered**: Utilizes Google's Gemini 2.5 Pro model for high-quality code generation.

## Deployed Link

Access the live application here: [https://multi-language-code-generator-ot3xs7eacnnevb76nb2hso.streamlit.app/](https://multi-language-code-generator-ot3xs7eacnnevb76nb2hso.streamlit.app/)

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd codegen
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Google Gemini API key:
   - Obtain an API key from [Google AI Studio](https://makersuite.google.com/app/apikey).
   - Replace the placeholder in `code_gen_multi.py` with your actual API key.

4. Run the application:
   ```
   streamlit run code_gen_multi.py
   ```

## Usage

1. Open the application in your browser (or use the deployed link).
2. Enter a natural language description of the code you want to generate (e.g., "Write a function to reverse a string").
3. Select the desired programming language from the dropdown.
4. Click "Generate Code" to produce the code snippet.
5. (Optional) Use the refinement section to add specifications and generate an improved version.

## Requirements

- Python 3.7+
- Streamlit
- google-generativeai

See `requirements.txt` for full dependencies.
