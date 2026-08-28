import subprocess
from sys import stdout
import os


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_directory_path = os.path.abspath(working_directory)
        full_path = os.path.join(working_directory_path, file_path)
        norm_path = os.path.normpath(full_path)
        joined_path = [norm_path, working_directory_path]
        common_path = os.path.commonpath(joined_path)

        if common_path != working_directory_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        is_file = os.path.isfile(norm_path)
        if is_file is False:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not norm_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", norm_path]
        if args is not None:
            command.extend(args)
        result = subprocess.run(command, cwd=working_directory_path, capture_output=True, text=True, timeout=30)
        output = ""
        if result.returncode != 0:
            output = f"Process exited with code {result.returncode} "
        if not result.stdout and not result.stderr:
            output += "No output produced"
        if result.stdout:
            output += f" STDOUT:{result.stdout}"
        if result.stderr:
            output += f" STDERR:{result.stderr}"
        return output
    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "executes the file and returns its output",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "path to the file that you should run",
                },
                "args": {
                    "type": "array",
                    "description": "optional command-line arguments to pass to the script",
                    "items": {
                        "type": "string"
                    },
                },
            },
            "required": ["file_path"],
        },
    },
}
