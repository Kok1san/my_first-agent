import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_directory_path = os.path.abspath(working_directory)
        full_path = os.path.join(working_directory_path, file_path)
        norm_path = os.path.normpath(full_path)
        joined_path = [norm_path, working_directory_path]
        common_path = os.path.commonpath(joined_path)
        is_dir = os.path.isdir(norm_path)
        if common_path != working_directory_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if is_dir == True:
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        os.makedirs(os.path.dirname(norm_path), exist_ok=True)
        with open(norm_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"

schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "writes or overwrites a file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "this is the path to the file whose contents should be writen",
                },
                "content": {
                    "type": "string",
                    "description": "this is the actual text/data that will be written into the file",
                },
            },
            "required": ["file_path", "content"],
        },
    },
}
