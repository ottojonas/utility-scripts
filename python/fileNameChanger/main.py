import os
import re


def to_camel_case(snake_str):
    """Convert a snake_case string to camelCase."""
    components = re.split(r"[^a-zA-Z0-9]", snake_str)
    return components[0].lower() + "".join(x.title() for x in components[1:])


def rename_files_to_camel_case(directory):
    """Rename all files in the given directory to camelCase."""
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            name, ext = os.path.splitext(filename)
            new_name = to_camel_case(name) + ext
            os.rename(
                os.path.join(directory, filename), os.path.join(directory, new_name)
            )


directory_path = "documents/"
rename_files_to_camel_case(directory_path)
