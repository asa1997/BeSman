import os
def construct_raw_url(namespace, repo, branch):
    namespace = namespace
    repo = repo
    branch = branch
    platform = os.environ.get("BESMAN_CODE_COLLAB_PLATFORM")
    ca