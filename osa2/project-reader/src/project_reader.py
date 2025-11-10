from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        toml_data = tomli.loads(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        tool_data = toml_data.get("tool", {}).get("poetry", {})

        name = tool_data.get("name")
        description = tool_data.get("description")
        license = tool_data.get("license")
        authors = tool_data.get("authors", [])
        dependencies = list(tool_data.get("dependencies", {}).keys())
        dev_dependencies = list(
            tool_data.get("group", {}).get("dev", {}).get("dependencies", {}).keys()
        )

        return Project(name, description, license, authors, dependencies, dev_dependencies)

