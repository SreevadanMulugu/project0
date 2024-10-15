
import re
import ollama


# Function to interact with Ollama and extract response
def get_ollama_response(query):
    response = ollama.chat(model='qwen2.5-coder:7b-instruct', messages=[
        {
            'role': 'user',
            'content': query,
        },
    ])
    return response['message']['content']


# Function to extract bash command from Ollama response
def extract_bash_command(response):
    # Use regex to find the bash command
    pattern = r"```bash(.*?)```"
    match = re.search(pattern, response, re.DOTALL)
    if match:
        bash_command = match.group(1).strip()
        return bash_command
    else:
        return None


# Function to extract Python program from Ollama response
def extract_python_program(response):
    # Use regex to find the Python program
    pattern = r"```python(.*?)```"
    match = re.search(pattern, response, re.DOTALL)
    if match:
        python_program = match.group(1).strip()
        return python_program
    else:
        return None


# Function to create .bat or .py file
def create_file(content, file_name, extension):
    file_name = f"{file_name}.{extension}"
    with open(file_name, 'w', encoding='utf-8') as file:  # Set encoding to 'utf-8'
        file.write(content)

    return file_name


# Example usage
def main():
    # Example query to Ollama
    query = 'Create a python program to play devara chutamalle video song (telugu) in youtube'
    response = get_ollama_response(query)

    # Step 2: Extract and save bash command
    bash_command = extract_bash_command(response)
    if bash_command:
        bat_file_name = create_file(bash_command, "install_package", "bat")
        print(f"Created {bat_file_name} with command:\n{bash_command}")
    else:
        print("No bash command found in the Ollama response.")

    # Step 3: Extract and save Python program
    python_program = extract_python_program(response)
    if python_program:
        py_file_name = create_file(python_program, "example_program", "py")
        print(f"Created {py_file_name} with content:\n{python_program}")
    else:
        print("No Python program found in the Ollama response.")


if __name__ == "__main__":
    main()
