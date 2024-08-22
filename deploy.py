# pip install paramiko
import paramiko
import time

# SSH configuration
ssh_host = 'your_server_ip'
ssh_port = 22
ssh_user = 'your_ssh_username'
ssh_password = 'your_ssh_password'  # If using password authentication
ssh_key_file = '/path/to/your/private/key'  # If using SSH key authentication

# GitHub and Project configuration
github_repo_url = 'https://github.com/yourusername/yourrepository.git'
project_directory = '/path/to/your/project/directory'

# Commands to run on the server
commands = [
    f'cd {project_directory} && git clone {github_repo_url}',
    f'cd {project_directory} && composer install',
    f'cd {project_directory} && npm install',
    f'cd {project_directory} && npm run build',
]

def run_ssh_commands(commands):
    # Create an SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the server
    try:
        # If using password authentication
        ssh.connect(ssh_host, port=ssh_port, username=ssh_user, password=ssh_password)

        # If using SSH key authentication
        # ssh.connect(ssh_host, port=ssh_port, username=ssh_user, key_filename=ssh_key_file)

        # Execute commands
        for command in commands:
            print(f"Executing: {command}")
            stdin, stdout, stderr = ssh.exec_command(command)
            stdout.channel.recv_exit_status()  # Block until command finishes
            output = stdout.read().decode()
            error = stderr.read().decode()

            if output:
                print(f"OUTPUT:\n{output}")
            if error:
                print(f"ERROR:\n{error}")

    except Exception as e:
        print(f"Failed to connect or execute commands: {e}")

    finally:
        ssh.close()

if __name__ == "__main__":
    run_ssh_commands(commands)
