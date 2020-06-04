# 0-current_working_directory

Within the file in the first line we can check the Shebang (in this case #!/bin/bash), gives to the shell the indication of what program is used to interpret the script.

In the second line there is the command "PWD" that means "Print Working Directory", so in the file that exucte the script, this show the current wor directory.

# 1-listit

The first line is the Shebang mentioned above. The second line is "ls" command tha list files or directories, to see more interactive options can use man ls and search one.

# 2-bring_me_home

The first line always have the Shebang, the second line is the command "cd", the command "cd" without options **(cd [OPTIONS] directory)** will take you to your home directory.

**To execute the script the syntax is . ./[script], because "cd" runs in a subshell so weexecute that in a subshell.**

# 3-listfiles

The command line ls -l list in long format, and shows a directory or a file like this:

**drwxr-xr-xr root root 1093 Oct 7 09:26 file**, the first letter (d) is the corresponds to a directory, the "rwx" groups correspond respectively to file owner user permissions, gruop permissions and others. 

# 4-listmorefiles

After the line of Shebang, the command "ls -la" print a list in long format and  don't ignore entries starting with "."

# 5-listfilesdigitonly

The command line ls -na, uses the option -n to do long lists like "-l" option but listing numeric user and group IDs and the option "-a" to show hidden files and directories.

# 6-firstdirectory

The command line "mkdir" is used to create folders, if the user is not located in the specific directory the route must be specified.

# 7-movethatfile

It's used to move a file to a directory with an absolute route, since the user is not in the directory, in this case /tmp.

# 8-firstdelete

Removed a file in a specific route directory with the command "rm".

# 9-firstdirdeletion

Removed a directory with the command and the option "rm -r", to finally removed the directory even if it has files within the directory.

# 10-back

The command "cd -" is the other way to go back to home directory, the other way is "cd ..".

# 11-lists

the command "ls -la" shows the long list of the current directory ".", the father directory ".." and the "/boot" directory in the required order.

# 12-file_type

Display information about command type.

# 13-symbolic_link

Creates a symbolic link using the option -s, that means make symbolic links instead of hard links.

# 14-copy_html

The command "cp" is used to copy only the newest files with the option "-u" and only the ones that end in .html because the wildcard "*" like this "*.html" is used.

# 15-lets_move

The script moves all files beginning with an uppercase to the directory /tmp/u.

# 16-clean_emacs

The script removes all files that end in "~", using the wildcard "*".

# 17-tree

The script makes directories with the option -p, creating parent directories as you wish.

# 18-commas

The script lists all the files and directories of the current directory, using the options required in the task, all of the options have been reviewed from the "man ls".

# holberton.mgc

Define what the string contains inside, the second line use "file" with the option "--mime" since you use the 'magic' file. 