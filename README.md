# Fixed Width File Project

## Overview

This project includes a library to read and write fixed-width format files, along with a command-line interface (CLI) to interact with these files.

## Project Structure

fixed_width_file_project/
├── fixed_width_file/
│ ├── init.py
│ ├── fixed_width_file.py
│ └── logger.py
├── tests/
│ ├── init.py
│ └── test_fixed_width_file.py
├── cli.py
├── requirements.txt
├── README.md
└── setup.py


## Getting Started

### Prerequisites

- Python 3.6 or higher

### Setup

1. **Clone the repository**:
    ```
    git clone https://github.com/yourusername/fixed_width_file_project.git
   
    cd fixed_width_file_project
    ```

2. **Create a virtual environment and activate it**:
    ```
    python3 -m venv venv
   
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   
    ```

3. **Install the required packages**:
    ```
    pip install -r requirements.txt
   
    ```

### Running the CLI

To use the CLI to interact with fixed-width files:

1. **Get a field value**:
    ```
    python cli.py path_to_file get header name
   
    ```

2. **Set a field value**:
    ```
    python cli.py path_to_file set header name "New Name"
   
    ```

3. **Add a transaction**:
    ```
    python cli.py path_to_file add 1000 USD
   
    ```

### Running the Tests

To run the tests, follow these steps:

1. **Create a sample fixed-width file**:

    Create a file named `sample_fixed_width_file.txt` with the following content:
    ```
    01John                          Doe                           Johnsson                     123 Main St                
    02000001000000000100USD                                                                                    
    02000002000000000200USD                                                                                    
    03000002000000000300     
                                                                                  
    ```

2. **Run the tests using `unittest`**:
    ```
    python -m unittest tests/test_fixed_width_file.py C:/path/to/sample_fixed_width_file.txt
   
    ```

### Example Fixed-Width File

Create a sample fixed-width file named `sample_fixed_width_file.txt` with the following content:

01John Doe Johnsson 123 Main St
02000001000000000100USD
02000002000000000200USD
03000002000000000300

