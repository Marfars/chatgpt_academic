import os


def get_filepath_with_filename(filename):
    parent_dir = os.path.dirname(os.path.dirname(__file__))

    return os.path.join(parent_dir, 'origin_paper', filename)
