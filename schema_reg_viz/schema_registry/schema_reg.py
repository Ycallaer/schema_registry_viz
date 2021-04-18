class SchemaRegistry():
    def __init__(self,base_url):
        self.base_url = base_url

    def get_subject_versions_url(self,subject_name):
        return self.base_url+"/subjects/{}/versions/".format(subject_name)

    def get_references_url(self,subject_name,versionId):
        return self.base_url+"/subjects/{}/versions/{}/referencedby".format(subject_name,versionId)

    def get_schema_by_id_url(self,schema_id):
        return self.base_url+"/schemas/ids/{}/".format(schema_id)