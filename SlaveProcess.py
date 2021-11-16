import threading
import time
import subprocess
from SlaveItem import SlaveItem

# I am a slave process that will be executed inside its own thread.
class SlaveProcess:
    # I am the slave process Item from the database.
    slaveItem = None
    # I am the slave process' execution thread.
    slaveThread = None
    # I am the subprocess itself
    subProcess = None

    # I will construct the slave process object utilizing the given SlaveItem.
    def __init__(self, slaveItem: SlaveItem):
        self.slaveItem = slaveItem

    # I will solely start the thread that executes the subprocess.
    def start(self):
        self.slaveThread = threading.Thread(target=self.runThread)
        self.slaveThread.start()

    # I will wait for the specified amount of seconds before anything will happen.
    def wait(self):
        time.sleep(self.slaveItem.master_wait)

    # I will solely stop the slave process.
    def stop(self):
        self.slaveThread.raise_exception()
        self.slaveThread.join()

    # I will set the subProcess to run if not already done.
    def isRunning(self):
        if self.subProcess is None:
            self.subProcess = True
            subprocess.run(["python3.7", self.slaveItem.slave_directory + self.slaveItem.slave_command])
            return True

    # I am the threads function that will run the process.
    def runThread(self):
        while True:
            if self.isRunning():
                print(self.slaveItem.slave_name + " GOOD")
            else:
                print(self.slaveItem.slave_name + " BAD...")
            time.sleep(5)
