  # Data type
  # Vatriable
  # collection
  # Loops and conditional statement


# Version control System
# Command: git status

# Output: fatal: not a git repository (or any of the parent directories): .git

# Explanation: This command is used to display the state of the working directory and the staging area in Git. It shows which changes have been staged, which haven't, and which files are not being tracked by Git. The error message you received indicates that the directory you were in (Bootcamp) was not a Git repository. This means that either Git had not been initialized in this directory (with git init), or you were not in the correct directory where a Git repository exists.

# Command: git clone https://github.com/Peppecoding/Python101.git

# Output: Various lines indicating the cloning process, ending with Cloning into 'Python101'...

# Explanation: This command is used to create a copy of an existing Git repository. In this case, you cloned the repository located at https://github.com/Peppecoding/Python101.git. The messages indicate the process of Git contacting the remote server (remote: Enumerating objects...), counting and receiving objects. This is a normal part of the cloning process, where Git is downloading all the files and history from the remote repository. After this command, you should have a new directory named Python101 in your Bootcamp directory, which contains the cloned Git repository.

# In summary:

# The git status command failed because it was run in a directory that was not a Git repository.
# The git clone command successfully cloned an external Git repository into a new directory within your current working directory.