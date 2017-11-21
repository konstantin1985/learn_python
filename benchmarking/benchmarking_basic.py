
 
# List comprehensions sometimes have a speed advantage over for loop
# statements, and that map calls can be faster or slower than both 
# depending on call patterns. 

# The generator functions and expressions tend to be slightly slower 
# than list comprehensions, though they minimize memory space 
# requirements and don't delay result generation

import time, sys


print('-' * 10 + "A.1. Basic timing function" + '-' * 10)

# time.clock() on Unix, return the current processor time as a floating
# point number expressed in seconds. The precision, and in fact the
# very definition of the meaning of "processor time", depends on that of
# the C function of the same name.

# time.clock() on Windows, returns wall-clock seconds elapsed since the
# first call to this function, as a floating point number, based on the
# Win32 function QueryPerformanceCounter(). The resolution is typically
# better than one microsecond.


def timer(func, *args):
    start = time.clock()
    for _ in range(100000):
        func(*args)
    return time.clock() - start

# Just 2 digits after the point here.
# For Linux it's better use time.time istead of time.clock

print(timer(pow, 2, 1000))        # 0.43
print(timer(str.upper, 'spam'))   # 0.03

print('-' * 10 + "A.2. More advanced timing function" + '-' * 10)

# Very important to use time.time for Linux 
timer = time.clock if sys.platform[:3] == 'win' else time.time

# The range call is hoisted out of the timing loop in
# the total function, so its construction cost is not 
# charged to the timed function in Python 2.X. In 3.X 
# range is an iterable, so this step is neither required
# nor harmful, but we still run the result through list
# so its traversal cost is the same in both 2.X and 3.X

def total(reps, func, *pargs, **kargs):
    """
    Total time to run func() reps times.
    Returns (total time, last result)
    """
    repslist = list(range(reps))               # Equalize 2.X and 3.X
    start = timer()
    for _ in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

# bestof() - more useful if you wish to filter out the 
# impacts of other activity on your computer, but less
# for tests that run too quickly to produce substantial 
# run times

def bestof(reps, func, *pargs, **kargs):
    """
    Quickest func() among reps runs.
    Returns (best time, last resull)
    """
    best = 2 ** 32                             # 136 years seems large enough
    for i in range(reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)

# Runs nested total tests within a best-of test, 
# to get the best-of-totals time.

def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    """
    Best of totals:
    (best of reps1 runs of (total of reps2 runs of func))
    """
    return bestof(reps1, total, reps2, func, *pargs, **kargs)

print(total(10000, pow, 2, 1000))                 # (0.046755075454711914, 1071508.....)
print(total(10000, str.upper, 'spam'))            # (0.0028319358825683594, 'SPAM')

print(bestof(10000, pow, 2, 1000))                # (3.814697265625e-06, 1071508.....)
print(bestof(10000, str.upper, 'spam'))           # (0.0, 'SPAM')

# Select bestof() from  10 times calculation of total()
print(bestoftotal(10, 10000, pow, 2, 1000))       # (0.0434269905090332, (0.043402910232543945, 1071508.....)
print(bestoftotal(10, 10000, str.upper, 'spam'))  # (0.002805948257446289, (0.0026569366455078125, 'SPAM'))

print('-' * 10 + "A.3. New timer calls in Python 3.X" + '-' * 10)

# time.perf_counter() returns the value in fractional
# seconds of a performance counter, defined as a clock
# with the highest available resolution to measure a
# short duration. It includes time elapsed during sleep
# states and is system-wide.

# time.process_time() returns the value in fractional
# seconds of the sum of the system and user CPU time
# of the current process. It does not include time elapsed
# during sleep, and is process-wide by definition.

# sys.version_info(major=2, minor=7, micro=3, releaselevel='final', serial=0)
if sys.version_info[0] >= 3 and sys.version_info[1] >= 3: # Python >= 3.3
    timer = time.perf_counter
else:
    timer = time.clock if sys.platform[:3] == 'win' else time.time

print('-' * 10 + "A.4. Comparison of list creation calls" + '-' * 10)

# forLoop : 1.33290 => [0...9999]
# listComp : 0.69658 => [0...9999]
# mapCall : 0.56483 => [0...9999]
# genExpr : 1.08457 => [0...9999]
# genFunc : 1.07623 => [0...9999]

# In comparison to these results, PyPy is roughly 10X 
# (an order of magnitude) quicker here

print('-' * 10 + "A.5. Even more advanced timing function" + '-' * 10)

timer = time.clock if sys.platform[:3] == 'win' else time.time

def total2(func, *pargs, **kargs):
    # If key is in the dictionary, remove it and return 
    # its value, else return default. If default is not
    # given and key is not in the dictionary, a KeyError is raised.
    _reps = kargs.pop('_reps', 10000)
    repslist = list(range(_reps))      # Hoist range out for 2.X lists
    start = timer()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof2(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 10000)
    best = 2 ** 32
    for _ in range(_reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)

def bestoftotal2(func, *pargs, **kargs):
    _reps1 = kargs.pop('_reps1', 5)
    # Because it must support two distinct repetition keywords with
    # defaults - total() and bestof() can't both use the same argument name
    return min(total2(func, *pargs, **kargs) for _ in range(_reps1))

print(total2(pow, 2, 1000))                   # (0.0458989143371582, 1071508.....)
print(total2(pow, 2, 1000, _reps = 100000))   # (0.44408607482910156, 1071508.....)
print(total2(str.upper, 'spam'))              # (0.0027551651000976562, 'SPAM')

print(bestof2(pow, 2, 1000))                  # (3.814697265625e-06, 1071508.....)
print(bestof2(pow, 2, 1000, _reps = 100000))  # (3.814697265625e-06, 1071508.....)
print(bestof2(str.upper, 'spam'))             # (0.0, 'SPAM')

print(bestoftotal2(pow, 2, 1000))             # (0.044569969177246094, 1071508.....)
print(bestoftotal2(str.upper, 'spam'))        # (0.0026810169219970703, 'SPAM')

print('-' * 10 + "A.6. Using keyword-only arguments (only Python 3.X)" + '-' * 10)

# They must be coded after a * and before a ** in the function header, 
# and in function call they must be passed by keyword and appear 
# before the ** if used.

# def total(func, *pargs, _reps=1000, **kargs):
#     ...
# 
# (elapsed, ret) = total(func, *pargs, _reps=1, **kargs)

