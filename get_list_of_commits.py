from dulwich import porcelain


def get_list_of_commits(file_path):
    """Write a list of commit messages.

    :param file_path: Path to repository
    """

    list = []

    with porcelain.open_repo_closing(file_path) as r:
        walker = r.get_walker(reverse=True)

    for entry in walker:
        item = str(entry.commit.message.decode())
        item = item.replace("\n", "")
        list.append(item)

    return list
	
