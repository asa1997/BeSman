import os
def construct_raw_url(namespace, repo, branch):
    namespace = namespace
    repo = repo
    branch = branch
    platform = os.environ.get("BESMAN_CODE_COLLAB_PLATFORM")
    # https://raw.githubusercontent.com/{env_repo}/{branch}/environment-metadata.json
    # http://lab.o31e.com/{env_repo}/-/raw/{branch}/environment-metadata.json
    if platform == "github":
        url = f'https://raw.githubusercontent.com/{namespace}/{repo}/{branch}'
    elif platform == "gitlab":
        platform_url = os.environ.get("BESMAN_CODE_COLLAB_URL")
        url = f'{platform_url}/{namespace}/{repo}/-/raw/{branch}'
    else:
        print(f"Error: Unsupported platform: {platform}")
    return url