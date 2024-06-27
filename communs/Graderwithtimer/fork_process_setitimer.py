import multiprocessing
import subprocess
import signal
import os
import time



signals = {
    2: "SIGINT",
    3: "SIGQUIT",
    4: "SIGILL",
    6: "SIGABRT",
    8: "SIGFPE",
    9: "SIGKILL",
    11: "SIGSEGV",
    13: "SIGPIPE",
    14: "SIGALRM",
    15: "SIGTERM"
};


def worker(command, thequeue):
    print(f"Worker process started with PID: {os.getpid()}")
        # Execute the command
    sp = subprocess.run(command, stdin=open("stdin_content", "r"), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, timeout=10)
    try: 
        spout = sp.stdout.decode() + sp.stderr.decode()
    except:
        spout = "Impossible de décoder la sortie standard"
    if -sp.returncode in signals:
        spout += "Processus terminé avec le signal UNIX ("+str(-sp.returncode)+") "+signals[-sp.returncode]
    elif sp.returncode < 0:
        spout += "Processus terminé avec le signal UNIX ("+str(-sp.returncode)+")"
    thequeue.put(spout)
    print(f"Worker process ended with PID: {os.getpid()}")

    
def handler(signum, frame):
    raise TimeoutError

def runStudentCode(timeout, command, stdin_content,theQueue):
    with open("stdin_content", "w") as f:
        f.write(stdin_content)
    # Fork the process
    process = multiprocessing.Process(target=worker, args=(command,theQueue,))
    process.start()

    # Set the timer
    signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, timeout)

    try:
        # attendre la fin du processus mais pas plus de timeout secondes (float)
        process.join(timeout)
        # Si il est encore vivant, on le tue et on attend la fin du processus
        if process.is_alive():
            print("Process taking too long, terminating...")
            process.terminate()
            process.join()
            theQueue.put("Processus trop long, terminé")
        else:
        # le processus est terminé, on désactive le timer et on affiche le message de fin
            pass
    except TimeoutError:
        print("Time limit reached, terminating the process...")
        process.terminate()
        process.join()
        theQueue.put("TimeputError : Processus trop long, terminé")
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)  # Disable the timer

if __name__ == "__main__":
    import sys
    timeout = float(sys.argv[1])  # Time limit in seconds
    sp =runStudentCode(timeout,"sleep 6;read a;write a", "Contenu du stdin")

