


# MAIN SOURCE:
# Lutz, "Programming Python" Chapter 5

# USEFUL LINKS:
#
# 1) What is difference between sys.exit(0) and os._exit(0)
#    https://stackoverflow.com/questions/9591350/what-is-difference-between-sys-exit0-and-os-exit0
#
# 2) Python:How os.fork() works? - very good explanation
#    https://stackoverflow.com/questions/33560802/pythonhow-os-fork-works


# GENERAL INFORMATION:

# There are two fundamental ways to get tasks running at the same 
# time in Python-process forks and spawned threads. Functionally,
# both rely on underlying operating system services to run bits of
# Python code in parallel. Procedurally, they are very different in
# terms of interface, portability, and communication.

# Although the process, thread, and IPC mechanisms we will explore
# in this chapter are the primary parallel processing tools in Python
# scripts, the third party domain offers additional options which may
# serve more advanced or specialized roles. The MPI for Python system
# allows Python scripts to also employ the Message Passing Interface
# (MPI) standard, allowing Python programs to exploit multiple
# processors in various ways.

print("-" * 20 + "# 1 Forking Processes" + "-" * 20)

# Forking is a straightforward way to start an independent program,
# whether it is different from the calling program or not. Forking 
# based on the notion of copying programs: when a program calls the
# fork routine, the operating system makes a new copy of that program
# and its process in memory and starts running that copy in parallel
# with the original.

# After a fork operation, the original copy of the program is called
# the parent process, and the copy created by os.fork is called the
# child process. In general, parents can make any number of children,
# and children can create child processes of their own; all forked
# processes run independently and in parallel under the operating
# system's control, and children may continue to run after their 
# parent exits.

# os._exit calls the C function _exit() which does an immediate
# program termination. Note the statement "can never return".
# sys.exit() is identical to raise SystemExit(). It raises a Python
# exception which may be caught by the caller.

# Python's process forking tools, available in the os module, are simply
# thin wrappers over standard forking calls in the system library also
# used by C language programs. To start a new, parallel process, call
# the os.fork built-in function. Because this function generates a copy
# of the calling program, it returns a different value in each copy: zero
# in the child process and the process ID of the new child in the parent.

# Programs generally test this result to begin different processing in
# the child only; this script, for instance, runs the child function in
# child processes only.

# Because forking is ingrained in the Unix programming model, this script
# works well on Unix, Linux, and modern Macs. Unfortunately, this script
# won't work on the standard version of Python for Windows today, because
# fork is too much at odds with the Windows model. Python scripts can
# always spawn threads on Windows, and the multiprocessing module described
# later in this chapter provides an alternative for running processes 
# portably, which can obviate the need for process forks on Windows in 
# contexts that conform to its constraints.

# You can fork with Python on Windows under Cygwin, even though its
# behavior is not exactly the same as true Unix forks.

"forks child processes until you type 'q'"

import os
import sys

def child():
    print('Hello from child', os.getpid())
    os._exit(0)                                                  # else goes back to parent loop

def parent():
    
    while True:
        
        
        # Create exact copy of the process
        
        newpid = os.fork()
        
        # So, if they are exact copies, how does one difference 
        # between parent and child? Simple. If the result of os.fork()
        # is zero, then you're working in the child. Otherwise, you're
        # working in the parent, and the return value is the PID 
        # (Process IDentifier) of the child. Anyway, the child can get
        # its own PID from os.getpid().
        
        if newpid == 0:
            child()
        else:
            print('Hello from parent', os.getpid(), newpid)
        
        if sys.version_info >= (3, 0):
            if input() == 'q': break
        else:
            if raw_input() == 'q': break


parent()

# OUTPUT:

# ('Hello from parent', 8268, 8274)
# ('Hello from child', 8274)                                     # Press Enter

# ('Hello from parent', 8268, 8275)
# ('Hello from child', 8275)                                     # Press Enter

# ('Hello from parent', 8268, 8276)
# ('Hello from child', 8276)q

# A subtle point: the child process function is also careful to exit
# explicitly with an os._exit call. We'll discuss this call in more
# detail later in this chapter, but if it's not made, the child process
# would live on after the child function returns (remember, it's just a
# copy of the original process). The net effect is that the child would
# go back to the loop in parent and start forking children of its own 
# (i.e., the parent would have grandchildren). If you delete the exit
# call and rerun, you'll likely have to type more than one q to stop,
# because multiple processes are running in the parent function.

