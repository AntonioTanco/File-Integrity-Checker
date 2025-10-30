from Utils.hashing.hashops import run_hash_computation

# import threading module
import threading

# Defining class to start a thread to handle hashing operation
def start_hash_thread():

    hashing_thread = threading.Thread(target=run_hash_computation)

    hashing_thread.start()

    hashing_thread.join()

    status = hashing_thread.is_alive

    if status == True:

        return True