import signal
import time
import resource 
import os
import resource
import sys
  
def limit_memory(maxsize): 
    soft, hard = resource.getrlimit(resource.RLIMIT_AS) 
    resource.setrlimit(resource.RLIMIT_AS, (maxsize, hard))

def time_exceeded(signo, frame): 
    print("Time's up !") 
    raise sys.exit(1) 
  
def signal_handler(signum, frame):
    raise Exception("Timed out!")

signal.signal(signal.SIGALRM, signal_handler)

if __name__ == "__main__":
    print("testing " + sys.argv[1] + ".py with USACO standards ...")
    problem = __import__(sys.argv[1])
    limit_memory(256)
    signal.alarm(4)
    try:
        problem.test()
    except Exception:
        print("Timed out")
        sys.exit(1)
    print("passed")
