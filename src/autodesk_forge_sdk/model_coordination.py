"""
Clients for working with the Forge Model Coordination service.
"""

from .auth import BaseOAuthClient, Scope, TokenProviderInterface


class ModelSetClient(BaseOAuthClient):
    def __init__(
        self,
        token_provider: TokenProviderInterface(),
        base_url: str = "https://developer.api.autodesk.com/bim360/modelset/v3",
    ):
        BaseOAuthClient.__init__(self, token_provider, base_url)

    def get_modelsets(self, container_id):
        return self._get(
            f"/containers/{container_id}/modelsets",
            scopes=[Scope.DATA_READ],
        ).json()


class ClashTestClient(BaseOAuthClient):
    def __init__(
        self,
        token_provider: TokenProviderInterface(),
        base_url: str = "https://developer.api.autodesk.com/bim360/clash/v3",
    ):
        BaseOAuthClient.__init__(self, token_provider, base_url)

    def get_tests(self, container_id, modelset_id):
        return self._get(
            f"/containers/{container_id}/modelsets/{modelset_id}/tests?continuationToken=0",
            scopes=[Scope.DATA_READ],
        ).json()

    def get_tests_2(self, container_id, modelset_id, version_id):
        return self._get(
            f"/containers/{container_id}/modelsets/{modelset_id}/versions/{version_id}/tests",
            scopes=[Scope.DATA_READ],
        ).json()

    def get_test(self, container_id, test_id):
        return self._get(
            f"/containers/{container_id}/tests/{test_id}",
            scopes=[Scope.DATA_READ],
        ).json()

    def get_test_resources(self, container_id, test_id):
        resources = self._get(
            f"/containers/{container_id}/tests/{test_id}/resources",
            scopes=[Scope.DATA_READ],
        ).json()

        # clashes = self._get(resources["resources"][0]["url"])
        instances = self._get(resources["resources"][1]["url"])
        documents = self._get(resources["resources"][2]["url"])

        return instances.content, documents.content
