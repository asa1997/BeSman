import os

class ConstructURL:
    def __init__(self, namespace, repo, branch):
        self.namespace = namespace
        self.repo = repo
        self.branch = branch
    
    def construct_raw_url(self, namespace, repo, branch):
        platform = os.environ.get("BESMAN_CODE_COLLAB_PLATFORM")
        # https://raw.githubusercontent.com/{env_repo}/{branch}/environment-metadata.json
        # http://lab.o31e.com/{env_repo}/-/raw/{branch}/environment-metadata.json
        url = ""  # Initialize url with a default value
        if platform == "github":
            url = f'https://raw.githubusercontent.com/{namespace}/{repo}/{branch}'
            print("github")
        elif platform == "gitlab":
            platform_url = os.environ.get("BESMAN_CODE_COLLAB_URL")
            url = f'{platform_url}/{namespace}/{repo}/-/raw/{branch}'
        else:
            print(f"Error: Unsupported platform: {platform}")
        return url