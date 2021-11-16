# I am a slave process Database item.
class SlaveItem:
    # I am the ID of the master server for identification.
    master_id = None
    # I am the name of the master server for identification.
    master_name = None
    # I am the host name of the master server.
    master_host = None
    # I am the amount of seconds the master will wait before starting another slave.
    master_wait = None
    # I am the name of the slave process for identification.
    slave_name = None
    # I am the working directory of the slave process.
    slave_directory = None
    # I am the command that is being executed to start the slave.
    slave_command = None

    # I will construct the SlaveItem entry.
    def __init__(self, slaveItem):
        self.master_id       = slaveItem[0]
        self.master_name     = slaveItem[1]
        self.master_host     = slaveItem[2]
        self.master_wait     = slaveItem[3]
        self.slave_name      = slaveItem[4]
        self.slave_directory = slaveItem[5]
        self.slave_command   = slaveItem[6]
