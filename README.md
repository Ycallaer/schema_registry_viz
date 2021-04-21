# Schema Registry Visualiser
FastApi application to visualise Schema Registry subject references.
For demo purposes an endpoint is foreseen to visualise your schema using d3 js.

## Getting started
You will need the following tools to get started:
* Python 3
* Installation of requirements.txt in a virtualenv
* A running schema registry in http or https mode
* Access to HTTPS certificate if running in https mode
* docker and docker-compose if you want to build the docker solution

## Local development
You can run the program locally by starting the file `main.py` from python. Before doing this you will need to uncomment
the last 2 lines in the `main.py`.
The environment will by default go to `local`. You can override the environment by setting the environment variable
`SR_VIZ_ENV`. If you need additional environments, add configuration files in the package `schema_reg_viz.config`

#### Local development: Endpoint call
If the application is running you can do a curl request as follows:
```bash
curl -d'{"subjectname": "google%2fprotobuf%2fdescriptor.proto"}' -X POST http://localhost:8888/viz_topic
```
This will return a JSON object containing the graph in a JSON structure, this can later 
be used to visualise it in a tool like D3.JS.

However, an endpoint has been foreseen to visualise your structure within this app. You will need to call the same
endpoint but you will need to supply the parameter `persist`. An example call would be:
```bash
curl -d'{"subjectname": "google%2fprotobuf%2fdescriptor.proto","persist":true}' -X POST http://localhost:8888/viz_topic
```
Part of the returning result will be a UUID eg: `"uuid":"00a7b2fb-c421-4bf2-8f49-97fa47b7957a"`

#### Local development: Visualising
With the UUID generated in the previous step you can call the following endpoint from your browser
```
http://localhost/show/00a7b2fb-c421-4bf2-8f49-97fa47b7957a
```
This will load the persisted JSON and visualise it in your browser.

## Docker environment
A docker solution has also been foreseen. 
First you will need to build the base image which can be done with the following command in the root of the project
```bash
docker build -t schema_registry_visualizer -f Docker/Dockerfile .
```

Once the base image is created you can run docker-compose to have a playground. Within this playground the following
services will be active:
* zookeeper
* kafka broker
* schema registry
* our schema registry visualiser app

Note: If you build the docker image with a different name, you need to change the docker-compose accordingly.

## Unit test
Pytests have been foreseen in the root directory `tests` and will be executed during pipeline execution.

## Contributing
If you want to contribute, please abide by the following rules:
* Create a feature branch and add your changes
* Create a pull request to merge into master
* Have a reviewer and merge