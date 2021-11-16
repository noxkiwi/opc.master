import sys

sys.path.insert(0, "..")

from opcua import Server
from MasterService import MasterService
from ConfigManager import ConfigManager

configManager = ConfigManager()

if __name__ == "__main__":
    # setup our server
    HostName = configManager.get("server>HostName")
    Port     = configManager.get("server>Port")
    Endpoint = configManager.get("server>EndPoint")
    server   = Server()
    server.set_endpoint("opc.tcp://" + HostName + ":" + str(Port) + "/" + Endpoint)

    # setup our own namespace, not really necessary but should as spec
    uri = "http://master.opc.nox.kiwi"
    namespace = server.register_namespace(uri)

    service = MasterService()
    server.start()
    service.scan_on()
