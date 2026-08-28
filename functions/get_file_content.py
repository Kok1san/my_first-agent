import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_directory_path = os.path.abspath(working_directory)
        full_path = os.path.join(working_directory_path, file_path)
        norm_path = os.path.normpath(full_path)
        joined_path = [norm_path, working_directory_path]
        common_path = os.path.commonpath(joined_path)

        if common_path != working_directory_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        is_file = os.path.isfile(norm_path)
        if is_file is False:
            return f'Error: File not found or is not a regular file: "{file_path}"'


        with open(norm_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            # After reading the first MAX_CHARS...
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string
    except:
        return f"Error: Something is wrong in get_file_content first block"

schema_get_file_content = {
    "type": "function",
    "function": {
        "name": "get_file_content",
        "description": "reads file content",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "this is the path to the file whose contents should be read",
                },
            },
            "required": ["file_path"],
        },
    },
}
