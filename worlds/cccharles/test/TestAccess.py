from .. import Options
from BaseClasses import CollectionState
from .bases import CCCharlesTestBase


class TestAccess(CCCharlesTestBase):
    def test_claire_breakers(self) -> None:
        """Test locations that require 4 Breakers"""
        options = {
            "cursed_fogs": Options.CursedFogs.option_all # Lock Lighthouse
        }

        lighthouse_claire_mission_end = self.world.get_location("Lighthouse Claire Mission End")

        state = CollectionState(self.multiworld)
        # Do not collect Fogbane Relics: keep Lighthouse locked
        self.collect_all_but(["Breaker", "Fogbane Relic Pack", "Fogbane Relic - Lighthouse"])

        breakers_in_pool = self.get_items_by_name("Breaker")
        self.assertGreaterEqual(len(breakers_in_pool), 4) # Check at least 4 Breakers are in the item pool

        for breaker in breakers_in_pool[:3]:
            state.collect(breaker) # Collect 3 Breakers into state

        # Check without access to Lighthouse (not enough breakers)
        self.assertFalse(
            lighthouse_claire_mission_end.can_reach(state),
            "Lighthouse Claire Mission End should not be reachable with only three Breakers"
        )

        # Check with Lighthouse unlocked (still not enough breakers)
        state.collect(self.get_item_by_name("Fogbane Relic - Lighthouse"))
        self.assertFalse(
            lighthouse_claire_mission_end.can_reach(state),
            "Lighthouse Claire Mission End should not be reachable with only three Breakers"
        )

        # Check nominal case
        state.collect(breakers_in_pool[3]) # Collect 4th breaker into state
        self.assertTrue(
            lighthouse_claire_mission_end.can_reach(state),
            "Lighthouse Claire Mission End should have been reachable with four Breakers"
        )
