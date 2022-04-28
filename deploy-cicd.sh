#!/bin/bash -e

# Deploys AWS IAM-permissions CloudFormation stack.
# Requires admin access to create/modify IAM roles.
# This is manually created/updated, whereas the
# rest of the cicd for this project is deployed
# via GitHub Actions.

STACK=${STACK-'analytics-cicd'}
TEMPLATE=cicd.cloudformation.yml


echo Validating cloudformation template...
aws cloudformation validate-template \
  --template-body file://${TEMPLATE} \
  | cat

ACCOUNT=$(aws sts get-caller-identity --query "Account" --output text)

read -r -p "Would you like to deploy this template to AWS account $ACCOUNT? [y/N] " response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]
then
  echo Deploying...
  aws cloudformation deploy \
    --template-file ${TEMPLATE} \
    --capabilities CAPABILITY_IAM \
    --stack-name ${STACK} \
    --tags \
      environment=dev \
      owner=redteam
else
  echo Exiting...
fi