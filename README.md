# Rep Tracker
Simple application for tracking workout stats overtime.

## Installation

Install [Docker Desktop](https://docs.docker.com/get-docker/)

Run Docker Build:
```
docker build .
```

## Local Setup
Run Migrations:
```
make migrations
```

Create a Superuser:
```
make create_superuser
```

Start Local Server:
1. Run `make dev_server`
2. In a browser open http://localhost:8000/

## Running Tests
Run Tests:
```
make runtests
```
