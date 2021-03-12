## Software Engineering Assignment

### How to run?

- You will need docker and docker-compose build
- run `docker-compose build` to build docker containers
- run `docker-compose up` to spin up the containers
- go to `localhost:5000` to access the web-app

### Pulling the docker image from docker hub

- Login to your docker hub account
- use the command `docker pull sachdev1/stackoverflow-tagfinder:latest`
- You will see the docker image with the same name on your local machine if the command succeeds.
- To run the image use `docker run -p [PORT]:5000 sachdev1/stackoverflow-tagfinder:latest`
- Replace `[PORT]` with an available port on your device. Example : `docker run -p 5000:5000 sachdev1/stackoverflow-tagfinder:latest`
- Navigate to `http://localhost:[PORT]` to access the site.
