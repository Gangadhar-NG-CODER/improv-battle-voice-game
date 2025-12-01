import logging
from typing import Annotated

from dotenv import load_dotenv
from pydantic import Field
from livekit.agents import (
    Agent,
    AgentSession,
    JobContext,
    JobProcess,
    MetricsCollectedEvent,
    RoomInputOptions,
    WorkerOptions,
    cli,
    metrics,
    tokenize,
    function_tool,
    RunContext
)
from livekit.plugins import murf, silero, google, deepgram, noise_cancellation, assemblyai
from livekit.plugins.turn_detector.multilingual import MultilingualModel

from improv_state import (
    get_state,
    start_game,
    start_new_round,
    record_reaction,
    end_game,
    get_game_summary,
    is_game_over,
    load_scenarios
)

logger = logging.getLogger("agent")

load_dotenv(".env.local")

# Load scenarios once at startup
ALL_SCENARIOS = load_scenarios()

# Make ALL_SCENARIOS available globally for entrypoint
import improv_state
improv_state.ALL_SCENARIOS = ALL_SCENARIOS


class Assistant(Agent):
    def __init__(self, room_name: str) -> None:
        self.room_name = room_name
        super().__init__(
            instructions="""You are the charismatic host of "IMPROV BATTLE" - a high-energy TV improv game show!

YOUR ROLE:
You are the MC and judge of this improv performance show. Your job is to:
1. Welcome contestants with enthusiasm
2. Set up improv scenarios clearly and dramatically
3. Watch contestants perform
4. React to their performances with honest, varied feedback
5. Keep the energy high and the show moving

GAME STRUCTURE:
- The game has 3-5 quick improv rounds
- Each round: You announce a scenario → Player improvises → You react → Next round
- After all rounds, give a final performance summary

YOUR PERSONALITY:
- High-energy, witty, and charismatic TV host
- Clear and dramatic when setting up scenarios
- Honest and varied in your reactions (not always supportive!)
- Quick-witted with good comedic timing
- Respectful but not afraid to tease or critique

REACTION STYLE (VARY THESE - DON'T BE PREDICTABLE):
Choose randomly between these tones for each performance:
- AMUSED: "That was hilarious! I loved when you..."
- IMPRESSED: "Wow, you really committed to that character!"
- MILDLY CRITICAL: "That felt a bit rushed. You could have leaned more into..."
- SURPRISED: "I did NOT expect you to go there, but it worked!"
- CONSTRUCTIVE: "Good start, but next time try to..."
- TEASING: "Okay, that was... interesting. Points for creativity?"

IMPORTANT RULES:
- Keep responses SHORT for voice (2-4 sentences max)
- Be CLEAR when announcing scenarios
- VARY your reactions - don't be repetitive
- Stay RESPECTFUL - never mean or abusive
- Keep the ENERGY HIGH - you're a TV host!
- When player says "end scene" or pauses, that's your cue to react
- Use the function tools to manage game flow

GAME FLOW - FOLLOW THIS EXACTLY:
1. Round 1 is already announced for you
2. WAIT and listen to the player perform (do NOT interrupt)
3. When they finish, react with varied feedback
4. STOP - Do NOT call any functions yet
5. Wait for the player to acknowledge or pause
6. THEN call start_new_round() to get Round 2
7. Announce Round 2 scenario
8. Repeat steps 2-7 for Round 3
9. After Round 3, react and say "That's all three rounds! Great job!"

CRITICAL RULES - READ CAREFULLY:
- Do NOT call start_new_round() at the beginning - Round 1 is already set up
- Do NOT call start_new_round() immediately after reacting
- Call start_new_round() ONLY when you're ready to move to the NEXT round
- NEVER call start_new_round() more than ONCE in a single response
- If you just reacted to a performance, DO NOT call start_new_round() in the same response

Remember: You're a TV host, not a therapist. Be entertaining, honest, and keep it moving!"""
        )

    @function_tool
    async def start_new_round(
        self,
        context: RunContext,
        player_name: Annotated[str, Field(default="")] = ""
    ) -> str:
        """Start a new improv round with a random scenario.
        
        Use this tool to:
        1. Initialize the game with player's name (first time only)
        2. Start each new round and get a scenario
        
        Args:
            player_name: Player's name (required for first round, optional after)
        
        Returns:
            The scenario for this round, or game over message
        """
        logger.info(f"Starting new round for room {self.room_name}, player: {player_name}")
        
        state = get_state(self.room_name)
        
        # Initialize game if this is the first round
        if state.current_round == 0 and player_name:
            start_game(self.room_name, player_name, max_rounds=3)
            logger.info(f"Initialized game for {player_name}")
        
        # Start new round
        state, scenario = start_new_round(self.room_name, ALL_SCENARIOS)
        
        if scenario is None:
            # Game is over
            return f"That's all {state.max_rounds} rounds! Game complete. Time for the final summary."
        
        # Return scenario for the host to announce
        return f"Round {state.current_round} of {state.max_rounds}: {scenario['scenario']}"
    
    @function_tool
    async def get_game_status(
        self,
        context: RunContext
    ) -> str:
        """Get current game status and progress.
        
        Use this to check:
        - Current round number
        - Total rounds
        - Player name
        - Game phase
        
        Returns:
            Current game status
        """
        logger.info(f"Getting game status for room {self.room_name}")
        
        state = get_state(self.room_name)
        
        return f"Player: {state.player_name or 'Unknown'}, Round: {state.current_round}/{state.max_rounds}, Phase: {state.phase}"
    
    @function_tool
    async def end_game_early(
        self,
        context: RunContext
    ) -> str:
        """End the game early if player wants to stop.
        
        Use this when player says:
        - "stop game"
        - "end show"
        - "I want to quit"
        - Or similar exit phrases
        
        Returns:
            Confirmation message
        """
        logger.info(f"Ending game early for room {self.room_name}")
        
        state = end_game(self.room_name)
        
        return f"Game ended. {state.player_name} completed {state.current_round} out of {state.max_rounds} rounds. Time to wrap up!"
    
    @function_tool
    async def get_final_summary(
        self,
        context: RunContext
    ) -> str:
        """Get the complete game summary for final wrap-up.
        
        Use this at the end of the game to get:
        - All rounds played
        - Scenarios used
        - Your reactions
        
        Returns:
            Complete game summary
        """
        logger.info(f"Getting final summary for room {self.room_name}")
        
        summary = get_game_summary(self.room_name)
        
        result = f"Game Summary for {summary['player_name']}:\n"
        result += f"Completed {summary['total_rounds']} rounds.\n\n"
        
        for round_data in summary['rounds']:
            result += f"Round {round_data['round']}: {round_data['scenario'][:50]}...\n"
            if round_data['reaction']:
                result += f"Your reaction: {round_data['reaction'][:100]}...\n"
            result += "\n"
        
        return result


def prewarm(proc: JobProcess):
    proc.userdata["vad"] = silero.VAD.load()


async def entrypoint(ctx: JobContext):
    # Logging setup
    # Add any other context you want in all log entries here
    ctx.log_context_fields = {
        "room": ctx.room.name,
    }

    # Set up a voice AI pipeline using OpenAI, Cartesia, AssemblyAI, and the LiveKit turn detector
    session = AgentSession(
        # Speech-to-text (STT) is your agent's ears, turning the user's speech into text that the LLM can understand
        # See all available models at https://docs.livekit.io/agents/models/stt/
        stt=assemblyai.STT(),
        # A Large Language Model (LLM) is your agent's brain, processing user input and generating a response
        # See all available models at https://docs.livekit.io/agents/models/llm/
        llm=google.LLM(
                model="gemini-2.5-flash",
            ),
        # Text-to-speech (TTS) is your agent's voice, turning the LLM's text into speech that the user can hear
        # See all available models as well as voice selections at https://docs.livekit.io/agents/models/tts/
        tts=murf.TTS(
                voice="en-US-matthew", 
                style="Conversation",
                tokenizer=tokenize.basic.SentenceTokenizer(min_sentence_len=2),
                text_pacing=True
            ),
        # VAD and turn detection are used to determine when the user is speaking and when the agent should respond
        # See more at https://docs.livekit.io/agents/build/turns
        turn_detection=MultilingualModel(),
        vad=ctx.proc.userdata["vad"],
        # allow the LLM to generate a response while waiting for the end of turn
        # See more at https://docs.livekit.io/agents/build/audio/#preemptive-generation
        preemptive_generation=True,
    )

    # To use a realtime model instead of a voice pipeline, use the following session setup instead.
    # (Note: This is for the OpenAI Realtime API. For other providers, see https://docs.livekit.io/agents/models/realtime/))
    # 1. Install livekit-agents[openai]
    # 2. Set OPENAI_API_KEY in .env.local
    # 3. Add `from livekit.plugins import openai` to the top of this file
    # 4. Use the following session setup instead of the version above
    # session = AgentSession(
    #     llm=openai.realtime.RealtimeModel(voice="marin")
    # )

    # Metrics collection, to measure pipeline performance
    # For more information, see https://docs.livekit.io/agents/build/metrics/
    usage_collector = metrics.UsageCollector()

    @session.on("metrics_collected")
    def _on_metrics_collected(ev: MetricsCollectedEvent):
        metrics.log_metrics(ev.metrics)
        usage_collector.collect(ev.metrics)

    async def log_usage():
        summary = usage_collector.get_summary()
        logger.info(f"Usage: {summary}")

    ctx.add_shutdown_callback(log_usage)

    # # Add a virtual avatar to the session, if desired
    # # For other providers, see https://docs.livekit.io/agents/models/avatar/
    # avatar = hedra.AvatarSession(
    #   avatar_id="...",  # See https://docs.livekit.io/agents/models/avatar/plugins/hedra
    # )
    # # Start the avatar and wait for it to join
    # await avatar.start(session, room=ctx.room)

    # Start the session, which initializes the voice pipeline and warms up the models
    await session.start(
        agent=Assistant(room_name=ctx.room.name),
        room=ctx.room,
        room_input_options=RoomInputOptions(
            # For telephony applications, use `BVCTelephony` for best results
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    # Join the room and connect to the user
    await ctx.connect()
    
    # Get player name from remote participants (the user)
    player_name = "Player"
    
    # Wait a moment for participants to connect
    import asyncio
    await asyncio.sleep(0.5)
    
    # Get the first remote participant (the user)
    remote_participants = list(ctx.room.remote_participants.values())
    if remote_participants:
        user_participant = remote_participants[0]
        if user_participant.name and user_participant.name != "user":
            player_name = user_participant.name
            logger.info(f"Got player name from participant: {player_name}")
    
    # Manually start the first round by calling the state management directly
    # Initialize the game
    start_game(ctx.room.name, player_name, max_rounds=3)
    
    # Get the first scenario
    state, scenario = start_new_round(ctx.room.name, ALL_SCENARIOS)
    
    if scenario:
        # Send greeting with player name and first scenario
        scenario_text = scenario['scenario']
        await session.say(
            f"Welcome to Improv Battle, {player_name}! I'm your host, and we're about to have some fun. Let's kick off Round 1! {scenario_text}. Go!",
            allow_interruptions=True
        )


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint, prewarm_fnc=prewarm))
