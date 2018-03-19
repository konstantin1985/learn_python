

# 1) find
#    https://www.lifewire.com/uses-of-linux-command-find-2201100 

# 2) xargs
#    https://shapeshed.com/unix-xargs/

# 3) Calculate number of code lines
#    find . -name '*.php' | xargs wc -l
#    https://stackoverflow.com/questions/1358540/how-to-count-all-the-lines-of-code-in-a-directory-recursively

# Dot and Dot Dot – . and ..
# http://teaching.idallen.com/cst8207/12f/notes/160_pathnames.html#dot-and-dot-dot-.-and-..


# SEE: https://www.tecmint.com/20-advanced-commands-for-middle-level-linux-users/
# pwd - current working directory
# cd {path} - go to path
# cp {old} {new}
# * wc
# * cat
# * ls
# mv {from} {to}
# echo
# jar
# grep
# find
# xargs
# sort
# >
# <
# >>
# ps
# whereis
# service
# alias
# df
# du
# rm
# read
# cmp
# * wget
# mount




# [|] "pipe" - use output from one command as input into another



# [wc] "Word Count" https://www.computerhope.com/unix/uwc.htm
# 1) wc {file}
#    OUTPUT: number of lines, number of words, number of characters.
# 2) wc -l --- print the newline counts.
# 3) ls -l | wc -l --- print the number of objects in the current directory

# [cp]
# 1) cp {old} {new} --- copy {file} to {new} including all the content



# [cat] https://www.tecmint.com/13-basic-cat-command-examples-in-linux/
# 1) cat {file} --- view content of {file}
# 2) cat >{file} --- create a file {file} and you immediately type IN the file, then Ctrl+D, then you can read it.
# 3) cat {file} | more or cat {file} | less --- not show all content, but scroll
# 4) cat -n {file} --- display line numbers in a file
# 5) cat {file1}; cat {file2} --- display multiple files at once
# 6) cat {file1} > {file2} --- create (or overwrite) content of {file2} with content of {file1}
# 7) cat {file1} >> {file2} --- append content of {file1} to {file2}, create {file2} if it doesn't exist
# 8) cat < {file} --- view content of {file} in terminal
# 9) cat {file1} {file2} {file3} > {file4} --- create {file4} and all output to {file4}
# 10) cat {file1} {file2} {file3} | sort > {file4} --- create {test4} and output of cat command is piped to sort and result will be redirected in {file4}

# [ls] https://www.tecmint.com/15-basic-ls-command-examples-in-linux/
# 1) ls *.py --- print only python file names
# 2) ls -l --- shows file or directory, size, modified date and time, file or folder name and owner of file and it's permission.
# 3) ls -a --- shows hidden files
# 4) ls -r --- lists in reverse order
# 5) ls -R --- recursively list sub-directories (with files in them)
# 6) ls -lS --- big in size first
# 7) ls -lS -r --- small in size first
# 8) ls -l /tmp --- list files under directory "/tmp"
# 9) ls -ld /tmp --- displays information of /tmp directory
# 10) ls -i --- file/directory with its inode number
# 11) ls -n --- display UID and GID of files
#     OUTPUT: -rw-r--r-- 1 1000 100  6965 Mar 19 11:16 command.py
#     1000 - standard first non root user

# [echo] https://www.tecmint.com/echo-command-in-linux/
# 1) echo Some text --- input a line of text and display on standard output
#    OUTPUT: Some text
# 2) echo "Test Page" > testpage --- with redirect operator to output to a file and not standard output
# 3) echo ~ --- show current home directory (~ is for home directory in Linux)

# [wget] "WWW get" https://en.wikipedia.org/wiki/Wget
# 1) wget http://www.example.com/ ---  Download the title page of example.com to a file # named "index.html".
# 2) wget ftp://ftp.gnu.org/pub/gnu/wget/wget-latest.tar.gz - download wget source code