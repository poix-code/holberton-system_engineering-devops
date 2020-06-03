# 0-current_working_directory

Within the file in the first line we can check the Shebang (in this case #!/bin/bash), gives to the shell the indication of what program is used to interpret the script.

In the second line there is the command "PWD" that means "Print Working Directory", so in the file that exucte the script, this show the current wor directory.

# 1-listit

The first line is the Shebang mentioned above. The second line is "ls" command that list files or directories, to see more interactive options can use man ls and search one.

# 2-bring_me_home

The first line always have the Shebang, the second line is the command "cd", the command "cd" without options (cd [OPTIONS] directory) will take you to your home directory.

To execute the script the syntax is . ./[script], because "cd" runs in a subshell so weexecute that in a subshell. **bold text**
