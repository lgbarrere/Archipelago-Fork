from dataclasses import dataclass
from Options import (
    StartInventoryPool, PerGameCommonOptions, DefaultOnToggle, Range, Toggle, DeathLink, Choice, Visibility
)


class TrackSwitches(Choice):
    """
    Randomize the track switches.

    **No:** Disabled.

    **Once:** When a switch is received, enable all the track switches.

    **All:** The 7 track switches are randomized.
    """
    display_name = "Track switches"
    option_no = 0
    option_once = 1
    option_all = 2
    default = 2
    visibility = Visibility.all


@dataclass
class CCCharlesOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    track_switches: TrackSwitches
    death_link: DeathLink
