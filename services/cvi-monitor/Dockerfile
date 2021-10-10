FROM python:3.9.4-slim-buster

RUN pip install poetry==1.1.11

# A locale needs to be installed and set for later use by some python packages like click
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Store all of the packages under the /usr/src/app directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY poetry.lock pyproject.toml /usr/src/app/

# Turning off virtual env as not needed since its a container.
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --no-interaction --no-ansi --no-dev

# Copy the code into the image
COPY . /usr/src/app/

# Run the CLI
ENTRYPOINT [ "python", "-m", "cvi_monitor" ]