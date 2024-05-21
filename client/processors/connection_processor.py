import logging

import esper
from components.drawable import Drawable
from components.server_id import ServerID
from resources.network_manager import NetworkManager

from common.components.name import Name
from common.components.position import Position
from common.engine.entity import Entity
from common.engine.processor import Processor
from common.engine.resource_manager import ResourceManager
from common.proto.server_packets import OMoveToPosition

logger = logging.getLogger(__name__)


class ConnectionProcessor(Processor):
    def __init__(self):
        super().__init__()

    def process(self, r: ResourceManager) -> None:
        network_manager = r.get_resource(NetworkManager)
        packets = network_manager.get_inbound_packets()
        for packet in packets:
            if packet.t == "ConfirmConnection":
                network_manager.connected = True
            if not network_manager.connected:
                continue
            if packet.t == "OMoveToPosition":
                pck: OMoveToPosition = packet.data
                for _, (serverId, pos) in esper.get_components(ServerID, Position):
                    if serverId.id == pck.id:
                        pos.x = pck.new_pos.x
                        pos.y = pck.new_pos.y
                else:
                    Entity().add_components(
                        Position(x=pck.new_pos.x, y=pck.new_pos.y),
                        Name("other player"),
                        Drawable("randomImage"),
                        ServerID(pck.id),
                    )

        if not network_manager.connected:
            network_manager.connect(name="JAAJ")
