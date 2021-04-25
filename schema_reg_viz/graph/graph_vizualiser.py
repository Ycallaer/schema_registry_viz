import os
import requests
import uuid
import networkx as nx
from networkx.readwrite import json_graph
import json
import traceback
from schema_reg_viz.json_logging.json_logger import JsonLogging
from schema_reg_viz.schema_registry.schema_reg import SchemaRegistry

log_app = JsonLogging()
logger = log_app.get_logger()


class MissingSubjectNameException(Exception):
    """
    Exception class for missing subject
    """
    pass


class MissingCertFilePath(Exception):
    """
    Exception class for missing cert file
    """
    pass


def do_url_request(request_url, sr_protocol):
    """
    Helper function to handle requests for Schema registry. If https is used, a valid cerificate must be present
    :param request_url: str: URL endpoint you are trying to reach
    :param sr_protocol: str: Protocol (http or https)
    :return: requests.Response
    """
    if sr_protocol == "http":
        return requests.get(url=request_url, headers={'content-type': 'application/json'})
    else:
        if "CERT_FILE_PATH" in os.environ:
            return requests.get(url=request_url, headers={'content-type': 'application/json'},
                                verify=os.getenv("CERT_FILE_PATH"))
        else:
            raise MissingCertFilePath()


def viz_sr_topic(subject_name, sr_base_url):
    """
    This function will, for a given subject, query schema registry and generate a networkx graph from it.
    :param subject_name: str: Name of the subject as in SR
    :param sr_base_url: str: Full URL of SR
    :return: none
    """
    G = nx.Graph()
    versions = None
    subject = subject_name.subjectname
    persist_uuid = uuid.uuid4() if subject_name.persist else None

    try:
        if len(subject) == 0:
            raise MissingSubjectNameException()
        else:

            G.add_node(subject)
            sr = SchemaRegistry(base_url=sr_base_url)
            versions = do_url_request(request_url=sr.get_subject_versions_url(subject_name=subject),
                                      sr_protocol=sr.get_protocol())

            if versions.status_code != 200:
                logger.error("No versions found for the given subject {}".format(subject_name),
                             extra={"severity": "error"})
            else:
                for version in json.loads(versions.text):
                    version_response = do_url_request(
                        request_url=sr.get_references_url(subject_name=subject, version_id=version),
                        sr_protocol=sr.get_protocol())
                    if version_response.status_code == 200:
                        for refId in json.loads(version_response.text):
                            schema_response = do_url_request(request_url=sr.get_schema_by_id_url(schema_id=refId),
                                                             sr_protocol=sr.get_protocol())
                            if schema_response.status_code == 200:
                                result = json.loads(schema_response.text)
                                for ref in result["references"]:
                                    G.add_edge(subject, ref["name"])
                                    G.add_node(ref["name"])

        data = json_graph.node_link_data(G)
        if persist_uuid is None:
            return {"data": data, "uuid": ""}
        else:
            with open('static/' + str(persist_uuid) + '.json', 'w') as f:
                json.dump(data, f, indent=4)

            return {"data": data, "uuid": persist_uuid}

    except MissingSubjectNameException:
        logger.error("An empty subject name was supplied. Aborting the process.", extra={"severity": "error"})
    except MissingCertFilePath:
        logger.error("There was no valid certificate path supplied for HTTPS. Aborting the process",
                     extra={"severity": "error"})
    except Exception:
        logger.error("Uncaught error detected. Aborting the process.", extra={"severity": "error"})
        traceback.print_exc()
