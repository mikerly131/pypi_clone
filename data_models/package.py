class Package:

    def __init__(self, package_name: str, summary: str, home_page: str, lic: str,
                 author_name: str, description: str, maintainers: list = None):
        if maintainers is None:
            maintainers = []

        self.package_name = package_name
        self.id = package_name
        self.summary = summary
        self.home_page = home_page
        self.license = lic
        self.author_name = author_name
        self.maintainers = maintainers
        self.description = description
