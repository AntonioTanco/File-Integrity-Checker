import Utils.hashing.hashops as hash
import Config.configops as config
import Utils.logs as syslog
from Utils.system import get_nodes_name
import Utils.system.check_if_file_exist as system

# use getServicesLogPaths() from config to store a list of paths to files from CONFIG.YAML
TARGETED_LOG_FILE = config.getServicesLogPaths()

# use getServicesName() from config to store a list of paths to files from CONFIG.YAML
TARGETED_SERVICE_NAMES = config.getServicesName()

# run check on TARGETED_LOG_FILE to see if files exist within the system
file_path_exist = system.check_if_file_exist(TARGETED_LOG_FILE)

# Creating function to run hash computation on program execution
def run_hash_computation():

    # Checking if files listed in YAML Config exist within the system
    if file_path_exist == True:

        # calculate and return hash of all the files present in YAML Config
        hash.getFilesHash(TARGETED_LOG_FILE)

        # print to console - hashes were successfully calculated for the targeted services after hashes were calculated
        syslog.logging.info(f"Calculated hashes successfully for: {TARGETED_SERVICE_NAMES}")

if __name__ == "__main__":
    run_hash_computation()