from urllib.parse import urlparse


class SchemaRegistry():
    def __init__(self, base_url):
        self.base_url = base_url
        self.protocol = urlparse(self.base_url).scheme

    def get_protocol(self):
        """
        Returns the protocol of a given URL
        :return: str: Protocol
        """
        return self.protocol

    def get_subject_versions_url(self, subject_name):
        """
        Creates the URL to retrieve the subject versions
        :param subject_name: str: Name of the subject
        :return: str
        """
        return self.base_url + "/subjects/{}/versions/".format(subject_name)

    def get_references_url(self, subject_name, version_id):
        """
        Creates the URL for the references for a specific subject and version
        :param subject_name: str: Name of the subject
        :param version_id: str: Id of the versions
        :return: str
        """
        return self.base_url + "/subjects/{}/versions/{}/referencedby".format(subject_name, version_id)

    def get_schema_by_id_url(self, schema_id):
        """
        Creates the URL for the schema of a specific ID
        :param schema_id: str: Id of the schema
        :return: str
        """
        return self.base_url + "/schemas/ids/{}/".format(schema_id)
