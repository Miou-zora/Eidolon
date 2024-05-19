from resources.network_manager import NetworkManager
from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager


class ConnectionProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        network_manager: NetworkManager = r.get_resource(NetworkManager)
        packets = network_manager.get_inbound_packets()
        for packet in packets:
            if packet.t == "ConfirmConnection":
                network_manager.connected = True
                network_manager.client_id = packet.data.id

        if not network_manager.connected:
            network_manager.connect(name="JAAJ")
