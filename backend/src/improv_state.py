"""
Improv Battle Game State Management

Manages the state of the improv game including rounds, scenarios, and player progress.
"""

import json
import random
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass, field, asdict
import logging

logger = logging.getLogger("improv_state")

# Global state storage keyed by room name
_game_states: Dict[str, "ImprovState"] = {}


@dataclass
class RoundData:
    """Data for a single improv round"""
    round_number: int
    scenario: str
    scenario_id: int
    player_performance: str = ""
    host_reaction: str = ""
    completed: bool = False


@dataclass
class ImprovState:
    """Game state for an improv battle session"""
    room_name: str
    player_name: Optional[str] = None
    current_round: int = 0
    max_rounds: int = 3
    rounds: List[RoundData] = field(default_factory=list)
    phase: str = "intro"  # "intro" | "awaiting_improv" | "reacting" | "done"
    scenarios_used: List[int] = field(default_factory=list)
    
    def to_dict(self) -> dict:
        """Convert state to dictionary"""
        return asdict(self)


def load_scenarios() -> List[dict]:
    """Load improv scenarios from JSON file"""
    scenarios_path = Path(__file__).parent.parent / "data" / "scenarios.json"
    
    try:
        with open(scenarios_path, "r", encoding="utf-8") as f:
            scenarios = json.load(f)
        logger.info(f"Loaded {len(scenarios)} scenarios")
        return scenarios
    except Exception as e:
        logger.error(f"Error loading scenarios: {e}")
        # Return fallback scenarios
        return [
            {
                "id": 1,
                "scenario": "You are a barista who has to tell a customer that their latte is actually a portal to another dimension.",
                "difficulty": "medium"
            }
        ]


def get_state(room_name: str) -> ImprovState:
    """Get or create game state for a room"""
    if room_name not in _game_states:
        _game_states[room_name] = ImprovState(room_name=room_name)
        logger.info(f"Created new game state for room: {room_name}")
    return _game_states[room_name]


def reset_state(room_name: str) -> ImprovState:
    """Reset game state for a room"""
    _game_states[room_name] = ImprovState(room_name=room_name)
    logger.info(f"Reset game state for room: {room_name}")
    return _game_states[room_name]


def get_random_scenario(state: ImprovState, all_scenarios: List[dict]) -> dict:
    """Get a scenario - fixed for first 3 rounds, random after that"""
    
    # Fixed scenarios for first 3 rounds (for consistent demo videos)
    FIXED_SCENARIO_IDS = [1, 2, 3]  # IDs: 1=barista, 2=time-travel, 3=waiter
    
    # Use fixed scenarios for first 3 rounds
    if state.current_round <= len(FIXED_SCENARIO_IDS):
        scenario_id = FIXED_SCENARIO_IDS[state.current_round - 1]
        scenario = next((s for s in all_scenarios if s["id"] == scenario_id), None)
        
        if scenario:
            state.scenarios_used.append(scenario["id"])
            logger.info(f"Using fixed scenario {scenario_id} for round {state.current_round}")
            return scenario
    
    # After first 3 rounds, use random scenarios
    # Filter out already used scenarios
    available = [s for s in all_scenarios if s["id"] not in state.scenarios_used]
    
    # If all scenarios used, reset and use all
    if not available:
        logger.info("All scenarios used, resetting available pool")
        available = all_scenarios
        state.scenarios_used = []
    
    # Pick random scenario
    scenario = random.choice(available)
    state.scenarios_used.append(scenario["id"])
    logger.info(f"Using random scenario {scenario['id']} for round {state.current_round}")
    
    return scenario


def start_game(room_name: str, player_name: str, max_rounds: int = 3) -> ImprovState:
    """Initialize a new game"""
    state = get_state(room_name)
    state.player_name = player_name
    state.max_rounds = max_rounds
    state.current_round = 0
    state.rounds = []
    state.phase = "intro"
    state.scenarios_used = []
    
    logger.info(f"Started game for {player_name} in room {room_name} with {max_rounds} rounds")
    return state


def start_new_round(room_name: str, all_scenarios: List[dict]) -> tuple[ImprovState, dict]:
    """Start a new improv round"""
    state = get_state(room_name)
    
    # Check if game is over
    if state.current_round >= state.max_rounds:
        state.phase = "done"
        logger.info(f"Game over for room {room_name}")
        return state, None
    
    # Mark previous round as completed if it exists
    if state.rounds:
        state.rounds[-1].completed = True
    
    # Increment round
    state.current_round += 1
    
    # Get random scenario
    scenario = get_random_scenario(state, all_scenarios)
    
    # Create round data
    round_data = RoundData(
        round_number=state.current_round,
        scenario=scenario["scenario"],
        scenario_id=scenario["id"]
    )
    state.rounds.append(round_data)
    state.phase = "awaiting_improv"
    
    logger.info(f"Started round {state.current_round} for room {room_name}: {scenario['scenario'][:50]}...")
    return state, scenario


def record_reaction(room_name: str, reaction: str) -> ImprovState:
    """Record host's reaction to the current round"""
    state = get_state(room_name)
    
    if state.rounds:
        current_round = state.rounds[-1]
        current_round.host_reaction = reaction
        current_round.completed = True
        state.phase = "reacting"
        logger.info(f"Recorded reaction for round {current_round.round_number} in room {room_name}")
    
    return state


def end_game(room_name: str) -> ImprovState:
    """End the game"""
    state = get_state(room_name)
    state.phase = "done"
    logger.info(f"Ended game for room {room_name}")
    return state


def get_game_summary(room_name: str) -> dict:
    """Get a summary of the game"""
    state = get_state(room_name)
    
    return {
        "player_name": state.player_name,
        "total_rounds": len(state.rounds),
        "max_rounds": state.max_rounds,
        "completed": state.phase == "done",
        "rounds": [
            {
                "round": r.round_number,
                "scenario": r.scenario,
                "reaction": r.host_reaction,
                "completed": r.completed
            }
            for r in state.rounds
        ]
    }


def is_game_over(room_name: str) -> bool:
    """Check if the game is over"""
    state = get_state(room_name)
    return state.current_round >= state.max_rounds or state.phase == "done"
