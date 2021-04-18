import requests
from schema_reg_viz.schema_registry.schema_reg import SchemaRegistry
import networkx as nx
import matplotlib.pyplot as plt
import json

class MissingTopicNameException(Exception):
    pass


def viz_sr_topic(subject_name, sr_base_url):
    G = nx.Graph()
    versions = None
    subject = subject_name.subjectname
    try:
        if len(subject) == 0:
            raise MissingTopicNameException()
        else:

            G.add_node(subject)
            sr = SchemaRegistry(base_url=sr_base_url)
            versions = requests.get(url=sr.get_subject_versions_url(subject_name=subject),headers = {'content-type': 'application/json'})

            if versions.status_code != 200 :
                print("No versions found")
            else:
                for version in json.loads(versions.text):
                    version_response = requests.get(url=sr.get_references_url(subject_name=subject,versionId=version),headers = {'content-type': 'application/json'})
                    if version_response.status_code == 200:
                        for refId in json.loads(version_response.text):
                            print("refid is "+str(refId))

                            schema_response = requests.get(url=sr.get_schema_by_id_url(schema_id=refId),headers = {'content-type': 'application/json'})
                            if schema_response.status_code == 200:
                                result = json.loads(schema_response.text)
                                for ref in result["references"]:
                                    G.add_edge(subject, ref["name"])
                                    G.add_node(ref["name"])
                                    print(ref["name"])
        plt.subplot(121)
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.show()
        plt.savefig('test.png')
    except MissingTopicNameException:
        print("Supply topic name")
