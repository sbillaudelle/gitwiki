from django.conf import settings
import git

def get_repository():
    return git.Repo(settings.REPOSITORY_PATH)

def get_file_from_tree(tree, path):
    for part in path.split('/'):
        tree = tree[part]
        if tree is None:
            # File not found :(
            break
        if not isinstance(tree, git.Tree):
            # Found and not a tree: we have the file, return it.
            return tree
    raise git.NoSuchPathError(path)
