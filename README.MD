# PRESIDIO ASSESMENT - Programming Assignment By ISHWOR UPRETI

## Author: Ishowr Upreti

## Getting Started

### Using this app

1. Clone this repo and navigate directory
2. Run `chmod +x start.sh`
3. Then `run ./sart.sh`

### Running project using docker

1. Directly run `docker run -it -d --name flask_app -p8080:8080 iupreti01/presidio-assessment`  

### hitting endpoints directly which is hosted on AWS ec2 instance

1. Hitting endpoint `
curl --location 'http://ec2-3-84-157-176.compute-1.amazonaws.com:80/search' \
--header 'Content-Type: application/json' \
--data '{
    "query": "your query"
}'
`

## Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.3.x/)
* [Docker](https://www.docker.com/)
