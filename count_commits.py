from dulwich import porcelain


def get_number_of_commits(list_of_commits):
    """Return how many commits are in the repo
	
    :param file_path: Path to repository
    """
	
    count = 0
	
    with porcelain.open_repo_closing(file_path) as r:
        walker = r.get_walker(reverse=True)

    for entry in walker:
        count += 1
		
    return count