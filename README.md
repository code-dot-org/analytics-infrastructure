# analytics-infrastructure

Welcome! You've found the source code for Code.org's analytics infrastructure.

## Getting Started
This document describes how to set up your workstation to contribute to `analytics-infrastructure`.

### Set Up

1. Install + Confirm OS-specific prerequisites

    ```
    python --version # --> python ^3.9.0
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

    3. Install [Poetry](https://python-poetry.org/docs/):

        ```
        curl -SSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
        ```

    </details>

    <details>
    <summary>Windows</summary>

    1. Install Python3: [Latest Python 3 Release](https://www.python.org/downloads/windows/)

    2. Install [Poetry](https://python-poetry.org/docs/)(bash):

    ```
    curl -SSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
    ```

    </details>

2. Clone the `code-dot-org/analytics-infrastructure` repo using SSH.

3. `cd analytics-infrastructure`

4. `cd src`

5. Install app dependencies:
    ```
    poetry install
    ```

6. Run the app:
    ```
    poetry run python hello-world.py
    ```

## Set up with Docker

If you have docker installed, you can run the following to run any of the python scripts.

The following **docker** command will **build** an image **t**agged as **etl-runner** using the Dockerfile in the current directory (aka '.').

```
docker build -t etl-runner .
```

Then you can **run** the image tagged **etl-runner**, optionally passing in the script name with the following command

```
docker run --rm etl-runner
# or
docker run --rm etl-runner hello-world.py
```
