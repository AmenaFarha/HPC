import subprocess

# Define repository path, file to commit, and commit message
repo_path = '/path/to/your/repo'
file_to_commit = 'file.txt'
commit_message = 'Add file.txt'

# Change directory to the repository
subprocess.run(['cd', repo_path], shell=True)

# Add the file to the staging area
subprocess.run(['git', 'add', file_to_commit], cwd=repo_path)

# Commit the file
subprocess.run(['git', 'commit', '-m', commit_message], cwd=repo_path)

# Push the changes to the remote repository
subprocess.run(['git', 'push'], cwd=repo_path)