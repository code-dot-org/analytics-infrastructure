# Uncomment the following lines to also build the image each time you execute this script

if [[ "$(docker images -q etl-runner 2> /dev/null)" == "" ]]; then
  echo Image 'etl-loader' not found, building Docker image...
  docker build -t etl-runner .
fi

# This version of the run command will volume mount the src folder, so you can run scripts modified or added since you last ran `docker build`
echo Running Docker image...
echo -------------------------------------------
docker run --rm -v "$(pwd)"/src:/src etl-runner $1

