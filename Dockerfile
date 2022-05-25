FROM python:3

WORKDIR /src

# Install Poetry
RUN pip install --no-cache-dir  'poetry==1'

# Copy only requirements to cache them in docker layer
COPY src/poetry.lock src/pyproject.toml /src/

# Project initialization:
RUN poetry install

# Creating folders, and files for the project
COPY src /src

# Run a python script
ENTRYPOINT ["poetry", "run", "python"]
CMD ["hello-world.py"]
