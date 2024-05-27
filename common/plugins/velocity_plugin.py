from __future__ import annotations

from typing import TYPE_CHECKING

from common.engine.plugin import Plugin
from common.engine.schedule_label import ScheduleLabel
from common.processors.apply_velocity_processor import ApplyVelocityProcessor
from common.processors.reset_velocity_processor import ResetVelocityProcessor

if TYPE_CHECKING:
    from common.engine.engine import Engine


class VelocityPlugin(Plugin):
    def build(self, engine: Engine) -> None:
        engine.add_processors(
            ScheduleLabel.Update,
            ApplyVelocityProcessor(),
            ResetVelocityProcessor(),
        )
