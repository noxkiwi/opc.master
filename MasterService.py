import threading
import time
from DatabaseManager import DatabaseManager
from SlaveProcess import SlaveProcess
from SlaveItem import SlaveItem
from ConfigManager import ConfigManager

# I am the master service class.U
class MasterService:
    # I am the configuration manager
    configManger = None
    # I am the ID of the Master Server I will start.
    MasterId = None
    # I am the master thread.
    masterThread = None
    # I trigger the execution of the master thread.
    scanEnable = False
    # I am the list of SlaveProcess objects.
    slaveProcesses = []

    # I will construct the master process.
    def __init__(self):
        self.configManger = ConfigManager()
        self.MasterId = self.configManger.get("master>MasterId")
        self.prepareSlaves()
        self.startMaster()

    # I will start the slaves as internal part of the master thread.
    def runThread(self):
        self.startSlaves()

    # I will start every slave while waiting ten seconds in between each slave.
    def startSlaves(self):
        for slaveProcess in self.slaveProcesses:
            slaveProcess.start()
            time.sleep(8)

    # I will query for active slaves of the currently active Master server.
    def prepareSlaves(self):
        query = '''SELECT
    `master`.`master_id`,
    `master`.`master_name`,
    `master`.`master_host`,
    `master`.`master_wait`,
    `slave`.`slave_name`,
    `slave`.`slave_directory`,
    `slave`.`slave_command`
FROM
    `master`
JOIN `slave` USING(`master_id`)
WHERE TRUE
    AND `master`.`master_id` = 1
    AND `master`.`master_flags` & 1
    AND `slave`.`slave_flags` & 1
ORDER BY
    `slave`.`slave_order`
'''
        dm = DatabaseManager()
        groupCursor = dm.read(query, ())
        for groupRow in groupCursor:
            slaveitem = SlaveItem(groupRow)
            self.slaveProcesses.append(SlaveProcess(slaveitem))

    # I will start the master thread.
    def startMaster(self):
        self.scanEnable = True
        if self.masterThread is None:
            print("Starting Master")
            self.masterThread = threading.Thread(target=self.runThread)
            self.masterThread.start()
            print(self.masterThread)
        return True

    # I will stop the master thread.
    def stop(self):
        self.masterThread.raise_exception()
        self.masterThread.join()

    # I will trigger the master thread on.
    def scan_on(self):
        # self.scan_thread.setDaemon(True)
        self.ScanEnable = True

    # I will trigger the master thread off.
    def scan_off(self):
        # self.scan_thread.setDaemon(False)
        self.ScanEnable = False
