import threading
import time
import subprocess
from SlaveItem import SlaveItem
from noxLogger import noxLogger

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
        noxLogger.info("opc.master SlaveProcess start for " + self.slaveItem.slave_name + " begins")
        self.slaveThread = threading.Thread(target=self.runThread)
        self.slaveThread.start()
        noxLogger.info("opc.master SlaveProcess start for " + self.slaveItem.slave_name + " ends")

    # I will wait for the specified amount of seconds before anything will happen.
    def wait(self):
        time.sleep(self.slaveItem.master_wait)

    # I will solely stop the slave process.
    def stop(self):
        noxLogger.info("opc.master SlaveProcess stop for " + self.slaveItem.slave_name + " begins")
        self.slaveThread.raise_exception()
        self.slaveThread.join()
        noxLogger.info("opc.master SlaveProcess stop for " + self.slaveItem.slave_name + " ends")

    # I will set the subProcess to run if not already done.
    def isRunning(self):
        if self.subProcess is None:
            noxLogger.info("opc.master isRunning for " + self.slaveItem.slave_name + " will run the command now")
            self.subProcess = True
            noxLogger.error("opc.master executing python3.7 " + self.slaveItem.slave_directory + self.slaveItem.slave_command)
            subprocess.run(["python3.7", self.slaveItem.slave_directory + self.slaveItem.slave_command], cwd=self.slaveItem.slave_directory)
            noxLogger.error("opc.master isRunning for " + self.slaveItem.slave_name + " process stopped")
            return False

    # I am the threads function that will run the process.
    def runThread(self):
        while True:
            if self.isRunning():
                noxLogger.info(self.slaveItem.slave_name + " GOOD")
            else:
                noxLogger.warning(self.slaveItem.slave_name + " BAD...")
                self.subProcess = None
            time.sleep(5)
