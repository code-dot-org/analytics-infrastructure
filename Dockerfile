FROM python:3

WORKDIR /src

# Install Poetry
RUN pip install 'poetry==1'

# Copy only requirements to cache them in docker layer
COPY src/poetry.lock src/pyproject.toml /src/

# Project initialization:
RUN poetry install

# Creating folders, and files for the project
COPY src /src

# Run a script to test things
# TODO: make this a CMD or ENTRYPOINT so I can pass the script name as a param on docker run
# RUN poetry run python hello-world.py
ENTRYPOINT ["poetry", "run", "python"]
CMD ["hello-world.py"]
