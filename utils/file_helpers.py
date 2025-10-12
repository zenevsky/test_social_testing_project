import os


def get_test_file_path(filename: str) -> str:
    utils_root = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(utils_root)
    resources_dir = os.path.join(project_root, "tests", "resources")
    file_path = os.path.join(resources_dir, filename)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Test file not found: {file_path}")

    return os.path.normpath(file_path)
