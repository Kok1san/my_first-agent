import os




def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        # Will be True or False
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if valid_target_dir is False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        is_dir = os.path.isdir(target_dir)
        if is_dir is False:
            return f'Error: "{directory}" is not a directory'

    except:
        return f"Error: Oops, something wrong!"
    try:
        list_dir = os.listdir(target_dir)
        list_files = []
        for item in list_dir:
            full_path = os.path.join(target_dir, item)
            file_name = item
            file_size = os.path.getsize(full_path)
            is_item_dir = os.path.isdir(full_path)
            list_files.append(f"- {file_name}: file_size={file_size} bytes, is_dir={is_item_dir}")
        list_files_result = "\n".join(list_files)
        return list_files_result
    except:
        return f"Error: list_dir block is not working"


schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
