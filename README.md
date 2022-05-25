# analytics-infrastructure

Welcome! You've found the source code for Code.org's analytics infrastructure.

- [analytics-infrastructure](#analytics-infrastructure)
  - [Deployed Resources](#deployed-resources)
  - [Application Logs](#application-logs)
  - [Getting Started](#getting-started)
    - [Set Up](#set-up)
    - [Set up with Docker](#set-up-with-docker)
  - [Deployment](#deployment)
    - [Security Prerequisites](#security-prerequisites)
  - [Verification](#verification)
    - [Application Deployment](#application-deployment)

## Deployed Resources

Cloudformation Stacks in production AWS:

- `analytics` stack: The AWS resources for this project, primarily an ECS Task Definition.
- `analytics-cicd` stack: Dependencies of the main application cicd process. Namely an Amazon Elastic Container Registry Repository, for storing built docker images.
- `analytics-security` stack: Security and authentication esources, manually deployed by privileged code.org admins.

## Application Logs

The ECS Tasks that execute the Python script in this project ship logs to AWS CloudWatch.

- [ECSLogGroup-analytics](https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#logsV2:log-groups/log-group/ECSLogGroup-analytics)

Deployment logs can be found in the Actions tab in GitHub or within the relevant Cloudformation stack.

## Getting Started

This document describes how to set up your workstation to contribute to `analytics-infrastructure`.

### Set Up

1. Install + Confirm OS-specific prerequisites

    ```bash
    python --version # --> python ^3.9.0
    poetry --version # --> Poetry ^1.1.13
    ```

    <details>
    <summary>MacOS X</summary>

    1. Install Homebrew:

        ```bash
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
        ```

    2. Install Python 3.10.0:

        ```bash
        brew install python
        ```

    3. Install [Poetry](https://python-poetry.org/docs/):

        ```bash
        curl -SSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
        ```

    </details>

    <details>
    <summary>Windows</summary>

    1. Install Python3: [Latest Python 3 Release](https://www.python.org/downloads/windows/)

    2. Install [Poetry](https://python-poetry.org/docs/)(bash):

    ```bash
    curl -SSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
    ```

    </details>

2. Clone the `code-dot-org/analytics-infrastructure` repo using SSH.

3. `cd analytics-infrastructure`

4. `cd src`

5. Install app dependencies:

    ```bash
    poetry install
    ```

6. Run the app:

    ```bash
    poetry run python hello-world.py
    ```

### Set up with Docker

If you have docker installed, you can run the following to run any of the python scripts.

The following **docker** command will **build** an image **t**agged as **etl-runner** using the Dockerfile in the current directory (aka '.').

```bash
docker build -t etl-runner .
```

Then you can **run** the image tagged **etl-runner**, optionally passing in the script name with the following command

```bash
docker run --rm etl-runner
# or
docker run --rm etl-runner test.py
```

## Deployment

There are layers to the infrastructure for this project. The following describes a setup-from-scratch process.

### Security Prerequisites

To create the initial security resources, or update them with changes, have the Infrastructure Team execute the "[deploy-security.sh](deploy-security.sh)" script which will deploy the "[security.cloudformation.yml](security.cloudformation.yml)" Cloudformation Template.

Once deployed, manually create an access token for the created user and paste the values into the following [GitHub Actions Secrets](https://github.com/code-dot-org/analytics-infrastructure/settings/secrets/actions) for this repository.

- `DEPLOY_AWS_ACCESS_KEY_ID`
- `DEPLOY_AWS_SECRET_ACCESS_KEY`

These will ensure that the deployment actions can authenticate with AWS to execute Cloudformation deployments.

## Verification

Upon creation of a Pull Request, and upon any subsequent commit to that Pull Request Branche, several verification steps will be performed. These are executed as GitHub Actions defined in the "[.github/workflows](.github/workflows)" directory. The following verifications occur:

- The dockerfile is linted
- All Python scripts are linted
- All cloudformation templates are linted

### Application Deployment

The application is deployed automatically upon merge to the `main` branch. This is defined within the "[ci-deploy.yml](.github/workflows/ci-deploy.yml)" GitHub Actions Workflow. First the "[cicd.cloudformation.yml](cicd.cloudformation.yml)" Cloudformation stack will be deployed, and then the Docker image will be built and pushed to an ECR Repository. Finally, the "[app.cloudformation.yml](app.cloudformation.yml)" stack will be deployed.
