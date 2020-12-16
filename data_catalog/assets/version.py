from data_catalog.client.versioning import VersionResponse


class Version(VersionResponse):
    """
    A service level class to extend the VersionResponse class generated by OpenAPI.
    It provides methods to obtain data from different versions of an Asset
    """

    def __init__(self, id=None, name=None, asset_id=None, contents=None, created_at=None,
                 local_vars_configuration=None):
        """
        Constructor of Version class
        :param id:
        :param name:
        :param asset_id:
        :param contents:
        :param created_at:
        :param local_vars_configuration:
        """

        super().__init__(id=id, created_at=created_at, name=name, asset_id=asset_id,
                         contents=contents, local_vars_configuration=local_vars_configuration)

    @staticmethod
    def from_response(version_response: VersionResponse):
        """
        Converts a VersionResponse into a Version by generating a new Version
        :param version_response: VersionResponse class generated by OpenApi
        :return: version
        :rtype: Version
        """
        return Version(id=version_response.id, created_at=version_response.created_at, name=version_response.name,
                       asset_id=version_response.asset_id, contents=version_response.contents,
                       local_vars_configuration=version_response.local_vars_configuration)