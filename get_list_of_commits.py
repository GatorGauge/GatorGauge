""" generate list of commit messages """

from dulwich import porcelain


def get_list_of_commits(file_path):
<<<<<<< HEAD
    """Write a list of commit messages.

    :param repo: Path to repository
    """

    commit_list = []

    with porcelain.open_repo_closing(file_path) as r:
        walker = r.get_walker(reverse=True)

    for entry in walker:
        item = str(entry.commit.message.decode())
        item = item.replace("\n", "")
        commit_list.append(item)

    return commit_list
=======
    """Write a list of commit messages."""
    return_list = []
    with porcelain.open_repo_closing(file_path) as repo:
        walker = repo.get_walker(reverse=True)
    for entry in walker:
        item = str(entry.commit.message.decode())
        item = item.replace("\n", "")
        return_list.append(item)
    return return_list
>>>>>>> origin
