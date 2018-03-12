

# MAIN SOURCE:
# Lutz, "Programming Python" Chapter 5

# USEFUL LINKS:


# GENERAL INFORMATION:

# Here we have a more complicated example than in fork_basic.py

print("-" * 20 + "# 1 Forking Processes" + "-" * 20)

# Illustrate multiple forked processes running in parallel.
# We start up 5 copies of itself, each copy counting up to 5 with
# a one-second delay between iterations.

# The output of all of these processes shows up on the same screen,
# because all of them share the standard output stream (and a system
# prompt may show up along the way, too). Technically, a forked 
# process gets a copy of the original process's global memory,
# including open file descriptors. Because of that, global objects
# like files start out with the same values in a child process, so
# all the processes here are tied to the same single stream. But it's
# important to remember that global memory is copied, not shared; 
# if child process changes a global object, it changes only its own
# copy. (As we'll see, this works differently in threads, the topic
# of the next section.)


"""
fork basics: start 5 copies of this program running in parallel with
the original; each copy counts up to 5 on the same stdout stream--forks
copy process memory, including file descriptors; fork doesn't currently
work on Windows without Cygwin: use os.spawnv or multiprocessing on
Windows instead; spawnv is roughly like a fork+exec combination;
"""

import os, time

def counter(count):                                  # run in new process
    for i in range(count):
        time.sleep(1)
        print('[%s] => %s' % (os.getpid(), i))
        
for i in range(5):
    pid = os.fork()
    if pid != 0:
        print('Process %d spawned' % pid)            # in parent: continue
    else:
        counter(5)                                   # else in child/new process
        os._exit(0)                                  # run function and exit

print('Main process exiting')                        # parent need not wait

# There is an error when I start it in Eclipse: 
# IOError: [Errno 32] Broken pipe
#
# Reason of the error may be: Doing something outside of Python
# to redirect the standard output of the Python interpreter to
# somewhere else. 

# OUTPUT:

# konstantin@linux-ks:~/Sphinx/learn_python/parallel/fork> python fork_count.py                                                    
# --------------------# 1 Forking Processes--------------------                                                                        
# Process 10154 spawned                                                                                                                
# Process 10155 spawned                                                                                                                
# Process 10156 spawned                                                                                                                
# Process 10157 spawned                                                                                                                
# Process 10158 spawned                                                                                                                
# Main process exiting                                                                                                                 
# konstantin@linux-ks:~/Sphinx/learn_python/parallel/fork> [10155] => 0                                                                
# [10157] => 0                                                                                                                         
# [10154] => 0                                                                                                                         
# [10156] => 0                                                                                                                         
# [10158] => 0                                                                                                                         
# [10155] => 1                                                                                                                         
# [10156] => 1                                                                                                                         
# [10157] => 1                                                                                                                         
# [10154] => 1                                                                                                                         
# [10158] => 1                                                                                                                         
# [10156] => 2                                                                                                                         
# [10158] => 2                                                                                                                         
# [10154] => 2
# [10157] => 2
# [10155] => 2
# [10158] => 3
# [10156] => 3
# [10154] => 3
# [10157] => 3
# [10155] => 3
# [10156] => 4
# [10158] => 4
# [10155] => 4
# [10154] => 4
# [10157] => 4
