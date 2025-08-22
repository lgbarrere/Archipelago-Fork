from dataclasses import dataclass
from Options import DefaultOnToggle, Range, Toggle, DeathLink, Choice, PerGameCommonOptions, Visibility


class RandomizeScraps(Choice):
    """
    Randomize the 636 scraps on the ground.

    **No:** Disabled (except mission rewards).

    **Region:** All scraps in a region must be collected to be considered as 1 location (49 regions = 49 locations).

    **Randomized:** All scraps are randomized.
    """
    display_name = "Randomize Scraps"
    option_no = 0
    option_region = 1
    option_all = 2
    default = 2
    visibility = Visibility.all


class ScrapsDetector(Choice):
    """
    Add a detector in the game, showing the closest scraps in a UI.

    **No:** Disabled.

    **Start:** The detector is enabled from the start of the game.

    **Randomized:** The detector is randomized.
    """
    display_name = "Scraps detector"
    option_no = 0
    option_start = 1
    option_randomized = 2
    default = 1
    visibility = Visibility.all


class ScrapsTracker(DefaultOnToggle):
    """
    The number of collected scraps in the region is shown on the map and the UI.
    """
    display_name = "Scraps tracker"
    visibility = Visibility.all


class BlueprintFragments(Choice):
    """
    Blueprint fragments must be received to access the 3 upgrades of the train.
    The 'Repair' option on the blueprint is not affected.
    These blueprints are randomized:

    Speed Upgrade ; Damage Upgrade ; Armor Upgrade

    **No:** Disabled.

    **Blueprints:** The 3 upgrades are locked until their blueprints (3 in total) are received.

    **Fragments:** When a fragment is received (30 in total), apply the upgrade directly without paying scraps.
    """
    display_name = "Blueprint fragments"
    option_no = 0
    option_blueprints = 1
    option_fragments = 2
    default = 1
    visibility = Visibility.all


class TrainAccess(Toggle):
    """
    The key to access the train is randomized.
    """
    display_name = "Train access"
    visibility = Visibility.all


class TrainRepairCost(Range):
    """
    Set the number of required scraps to repair the train.
    """
    display_name = "Repair cost"
    range_start = 0
    range_end = 5
    default = 1
    visibility = Visibility.all


class RandomStartingWeapon(DefaultOnToggle):
    """
    Randomize the starting weapon among the 4 possible guns.
    """
    display_name = "Random starting weapon"
    visibility = Visibility.all


class PaintCansRule(Choice):
    """
    Add a rule for the paint cans.

    **No:** Disabled.

    **Randomized:** The paint cans are randomized.

    **Hints:** The paint cans are randomized and give hints when received.

    **Potions:** The paint cans are randomized and confer passive effects when received.
    """
    display_name = "Paint Cans rule"
    option_no = 0
    option_randomized = 1
    option_hints = 2
    option_potions = 3
    default = 1
    visibility = Visibility.all


class SplitRemoteExplosives(Choice):
    """
    Split the explosives to make up to 8 packs to randomize.

    **1 pack:** 1 pack of 8 (vanilla).

    **2 packs:** 2 packs of 4.

    **4 packs:** 4 packs of 2.

    **8 packs:** 8 packs of 1.
    """
    display_name = "Split Remote Explosives"
    option_1_pack = 1
    option_2_packs = 2
    option_4_packs = 4
    option_8_packs = 8
    default = 1
    visibility = Visibility.all


class UnscrapTrap(Range):
    """
    What percent of traps removing 5 scraps from the inventory are randomized.
    """
    display_name = "Unscrap-trap %"
    range_start = 0
    range_end = 10
    default = 0
    visibility = Visibility.all


class DerailedTrap(Range):
    """
    What percent of traps reducing the train HP by 30 are randomized.
    """
    display_name = "Derailed-trap %"
    range_start = 0
    range_end = 10
    default = 0
    visibility = Visibility.all


class RailwaySwitch(Choice):
    """
    Randomize the railway switches.

    **No:** Disabled.

    **Once:** When a switch is received, enable all the railway switches.

    **All:** The 7 railway switches are randomized.
    """
    display_name = "Railway switch"
    option_no = 0
    option_once = 1
    option_all = 2
    default = 2
    visibility = Visibility.all


class SecretGear(Toggle):
    """
    Add the secret gear implementation that was canceled in the base game.
    The harrow in the North Mine cannot be opened without this gear.
    """
    display_name = "Secret gear"
    visibility = Visibility.all


class CharlesFrequency(Range):
    """
    Scale the encounter frequency against Charles.

    0 means Charles never attacks.

    1 is the default frequency.

    3 is the higher threat.
    """
    display_name = "Charles' frequency"
    range_start = 0
    range_end = 3
    default = 1
    visibility = Visibility.all


@dataclass
class CCCharlesOptions(PerGameCommonOptions):
    randomize_scraps: RandomizeScraps
    scraps_detector: ScrapsDetector
    scraps_tracker: ScrapsTracker
    blueprint_fragments: BlueprintFragments
    train_access: TrainAccess
    train_repair_cost: TrainRepairCost
    random_starting_weapon: RandomStartingWeapon
    paint_cans_rule: PaintCansRule
    split_remote_explosives: SplitRemoteExplosives
    unscrap_trap: UnscrapTrap
    derailed_trap: DerailedTrap
    railway_switch: RailwaySwitch
    secret_gear: SecretGear
    charles_frequency: CharlesFrequency
    death_link: DeathLink
