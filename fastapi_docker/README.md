# FastAPI Docker App

This project demonstrates how to create and run a FastAPI application inside a Docker container.

### Getting Started

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

> Docker,
> Python 3.9 (optional, for local development)

### Installing

Clone the repository:

```sh
git clone https://github.com/yourusername/fastapi-docker-app.git
cd fastapi-docker-app
Create a main.py file:
```

### Build and run Docker

To Build the Docker Image run the following

```sh
docker build -t myfastapi .
```

Running the Docker Container
To run the Docker container, execute the following command:

```sh
docker run -d --name myfastapi -p 8000:8000 myfastapi
```
