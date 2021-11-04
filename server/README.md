# SPORTS TRENDS SERVER

_NOTE: Must have Docker Installed https://www.docker.com/_

### Installation

To build docker image:

```
docker build -t imagename .
```

To build packages:

```
docker compose up --build
```

### Launch Server After Build

The above will build the the packages required for the server and then will run it, but to run without having to build:

```
docker compose up
```
