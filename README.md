# analytics-infrastructure

Welcome! You've found the source code for Code.org's analytics infrastructure.

## Getting Started
This document describes how to set up your workstation to contribute to `analytics-infrastructure`.

### Set Up

1. Install + Confirm OS-specific prerequisites

    ```
    python --version # --> python ^3.10.0
    pip -m pip --verison # --> pip ^22.0.4
    ```

    > TODO: python virtual environments?

    <details>
    <summary>MacOS X</summary>

    1. Install Homebrew:

        ```
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
        ```

    2. Install and set up [pyenv]('https://github.com/pyenv/pyenv') to manage different versions of Python.

        ```
        brew install pyenv
        ```

    3. Install Python 3.10.0:

        ```
        pyenv install 3.10.0
        ```

    4. Add the following to your `.bash_profile`. (more details in [their documentation](https://github.com/pyenv/pyenv#basic-github-checkout)):

        ```
        eval "$(pyenv init --path)"
        ```

    5. Set your global Python version:

        ```
        pyenv global 3.10.0
        ```

    5. Install pip:

        ```
        python -m ensurepip --upgrade
        ```

    </details>

    <details>
    <summary>Windows</summary>

    1. Install Python3: [Latest Python 3 Release](https://www.python.org/downloads/windows/)
    2. Install and set up [pyenv]('https://github.com/pyenv-win/pyenv-win#installation') to manage different versions of Python. In Powershell or Git Bash:
        ```
        pip install pyenv-win --target $HOME\\.pyenv
        ```

    3. Set your global Python version (and install if necessary):

        ```
        pyenv global 3.10.0
        ```

    </details>


2. Clone the `code-dot-org/analytics-infrastructure` repo using SSH.
3. `cd analytics-infrastructure`
4. Install app dependencies:
    ```
    pip install -r requirements.txt
    ```
