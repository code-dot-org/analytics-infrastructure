# analytics-infrastructure

Welcome! You've found the source code for Code.org's analytics infrastructure.

## Getting Started
This document describes how to set up your workstation to contribute to `analytics-infrastructure`.

### Set Up

1. Install + Confirm OS-specific prerequisites

    ```
    python --version # --> python ^3.10.0
    python -m pip --verison # --> pip ^22.0.4
    poetry --version # --> Poetry ^1.1.13
    ```

    <details>
    <summary>MacOS X</summary>

    1. Install Homebrew:

        ```
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
        ```

    2. Install Python 3.10.0:

        ```
        brew install python
        ```

    3. Install/Upgrade pip:

        ```
        python -m ensurepip --upgrade
        ```

    4. Install poetry:

        ```
        curl -SSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
        ```

    </details>

    <details>
    <summary>Windows</summary>

    1. Install Python3: [Latest Python 3 Release](https://www.python.org/downloads/windows/)

    2. Install/Upgrade pip:

        ```
        python -m ensurepip --upgrade
        ```

    3. Install poetry (bash):

    ```
    curl -SSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
    ```

    </details>

2. Clone the `code-dot-org/analytics-infrastructure` repo using SSH.

3. `cd analytics-infrastructure`

4. Install app dependencies:
    ```
    pip install -r requirements.txt
    ```
