# Schema Registry Vizualiser
FastApi application to visualise Schema Registry subject references.

## Getting started
You will need the following tools to get started:
* Python 3
* Installation of requirements.txt in a virtualenv
* A running schema registry in http or https mode
* Access to HTTPS certificate if running in http mode

## Local development
You can run the program locally by starting the following script
```python
python /home/yves/PersonalProjects/schema_registry_viz/schema_reg_viz/main.py
```
The environment will by default go to `local`. You can override the environment by setting the environemnt variable
`SR_VIZ_ENV`

#### Local development: Endpoint call
If the application is running you can do a curl request as follows:
```bash
curl -d'{"subjectname": "google%2fprotobuf%2fdescriptor.proto"}' -X POST http://localhost:8888/viz_topic
```

## Contributing
If you want to contribute, please abide by the following rules:
* Create a feature branch and add your changes
* Create a pull request to merge into master
* Have a reviewer and merge