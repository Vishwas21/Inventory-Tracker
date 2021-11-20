# Testing and running the application using the latest version of Python

FROM python:latest

# Creating a directory in the container to store the application code
RUN mkdir -p /usr/src/inventoryTracker

# Setting the working directory to the created folder
WORKDIR /usr/src/inventoryTracker

# Copy the requirements.txt file
COPY ./requirements.txt .

# Installing the required packages
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:5982" ]