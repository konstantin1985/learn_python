


# MAIN SOURCE:
# Lutz, "Programming Python" Chapter 5

# USEFUL LINKS:


# GENERAL INFORMATION:

# In fork_basic.py and fork_count.py child processes simply ran
# a function within the Python program and then exited. On Unix-like
# platforms, forks are often the basis of starting independently
# running programs that are completely different from the program that
# performed the fork call. For instance, the next example forks new 
# processes until we type q again, but child processes run a brand-new
# program instead of calling a function in the same file.

# The main thing to notice is the os.execlp call in this code. In a
# nutshell, this call replaces (overlays) the program running in the
# current process with a brand new program. Because of that, the
# combination of os.fork and os.execlp means start a new process and
# run a new program in that process-in other words, launch a new 
# program in parallel with the original program.

# The arguments to os.execlp specify the program to be run by giving
# command-line arguments used to start the program. If successful, 
# the new program begins running and the call to os.execlp itself 
# never returns (since the original program has been replaced, 
# there's really nothing to return to).the call does return, an error
# has occurred.

# Here is this code in action on Linux. It doesn't look much different
# from the original fork1.py, but it's really running a new program in
# each forked process.


