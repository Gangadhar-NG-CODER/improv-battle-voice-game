# Improv Battle - Backend (Python)

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![LiveKit Agents](https://img.shields.io/badge/LiveKit-Agents-green)](https://livekit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](../LICENSE)

> 🎭 **DAY 10 of the Murf AI Voice Agents Challenge**
>
> This backend powers the Improv Battle game show - an AI-powered improv host that runs contestants through hilarious scenarios and reacts with honest, varied feedback.
> Built with **Murf Falcon TTS** (fastest TTS API), **Google Gemini 2.5 Flash**, and **AssemblyAI STT**.

[Main Project](../README.md) | [Frontend](../frontend/README.md)

## 🎭 What This Does

This backend implements an **Improv Game Show Host AI** that:

- **Welcomes** contestants and explains the game
- **Announces** random improv scenarios dramatically
- **Listens** to player performances
- **Reacts** with varied, honest feedback (amused, critical, surprised)
- **Manages** game state across 3-5 rounds
- **Summarizes** player's improv style at the end

## 🏗️ Tech Stack

- **LLM**: Google Gemini 2.5 Flash (conversation & reactions)
- **TTS**: Murf Falcon (fastest TTS API - 20 seconds of audio in <1 second)
- **STT**: AssemblyAI (speech-to-text)
- **Framework**: LiveKit Agents Python SDK
- **Turn Detection**: Multilingual Model (contextual speaker detection)
- **Data Storage**: JSON files (scenarios.json)

## ✨ Key Features

- **4 Function Tools** - Complete game management
- **20 Scenarios** - Wild, creative improv situations
- **Varied Reactions** - Host doesn't repeat feedback style
- **Game State** - Tracks rounds, scenarios, reactions
- **Voice-Optimized** - Concise responses perfect for voice
- **Auto-Greeting** - Welcomes contestants and asks for name

## 📁 Project Structure

```
backend/
├── src/
│   ├── agent.py          # Main improv host agent
│   └── improv_state.py   # Game state management
├── data/
│   └── scenarios.json    # 20 improv scenarios
├── .env.local            # API keys (not in git)
├── .env.example          # Example environment variables
├── pyproject.toml        # Python dependencies
└── README.md
```

## 🛠️ Function Tools

### 1. `start_new_round`
Start a new improv round with a random scenario.

```python
start_new_round(player_name="John")  # First round only
start_new_round()  # Subsequent rounds
```

### 2. `get_game_status`
Get current game status and progress.

```python
get_game_status()
# Returns: "Player: John, Round: 2/3, Phase: awaiting_improv"
```

### 3. `end_game_early`
End the game early if player wants to stop.

```python
end_game_early()
```

### 4. `get_final_summary`
Get complete game summary for final wrap-up.

```python
get_final_summary()
```

## 🎭 Improv Scenarios

20 creative scenarios including:
- Barista explaining latte is a portal to another dimension
- Time-travelling tour guide with someone from 1800s
- Waiter explaining order escaped the kitchen
- Customer returning cursed object
- Tech support for sentient computer
- Flight attendant on plane to nowhere
- Museum guide for invisible art
- Chef with self-aware soup
- Librarian with books reading themselves
- Taxi driver who only drives backwards
- ...and 10 more!

## 🚀 Dev Setup

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager

### Installation

```bash
cd backend

# Install dependencies
uv sync
```

### Environment Variables

Copy `.env.example` to `.env.local` and fill in your API keys:

```env
# LiveKit
LIVEKIT_URL=wss://your-livekit-server-url
LIVEKIT_API_KEY=your_api_key
LIVEKIT_API_SECRET=your_api_secret

# Murf AI (TTS)
MURF_API_KEY=your_murf_api_key

# AssemblyAI (STT)
ASSEMBLYAI_API_KEY=your_assemblyai_api_key

# Google Gemini (LLM)
GOOGLE_API_KEY=your_google_api_key
```

### Download Required Models

Before first run, download VAD and turn detection models:

```bash
uv run python src/agent.py download-files
```

## 🎮 Run the Agent

### Development Mode

For use with frontend:

```bash
uv run python src/agent.py dev
```

### Production Mode

```bash
uv run python src/agent.py start
```

### Console Mode (Testing)

Speak to the agent directly in your terminal:

```bash
uv run python src/agent.py console
```

## 📊 Game State Model

### ImprovState Schema

```python
{
  "room_name": "room-123",
  "player_name": "John",
  "current_round": 2,
  "max_rounds": 3,
  "phase": "awaiting_improv",  # intro | awaiting_improv | reacting | done
  "scenarios_used": [1, 5, 12],
  "rounds": [
    {
      "round_number": 1,
      "scenario": "You are a barista...",
      "scenario_id": 1,
      "player_performance": "",
      "host_reaction": "That was hilarious!",
      "completed": true
    }
  ]
}
```

## 🎯 Agent Instructions

The agent is configured as a high-energy TV improv show host with:
- Charismatic, witty personality
- Varied reaction styles (amused, critical, surprised, teasing)
- Clear scenario announcements
- Honest but respectful feedback
- Quick comedic timing
- Game flow management

See `src/agent.py` for the complete system prompt.

## 📝 Customization

### Adding Scenarios

Edit `data/scenarios.json` to add new scenarios:

```json
{
  "id": 21,
  "scenario": "Your custom improv scenario here",
  "difficulty": "medium"
}
```

### Modifying Host Personality

Update the system prompt in `src/agent.py` under the `Assistant` class `instructions` parameter.

### Changing TTS Voice

Modify the TTS configuration in `src/agent.py`:

```python
tts=murf.TTS(
    voice="en-US-matthew",  # Change voice
    style="Conversation",    # Change style
    text_pacing=True
)
```

Available Murf voices: matthew, sarah, emma, etc.

### Adjusting Round Count

Change `max_rounds` in `start_new_round` function call:

```python
start_game(room_name, player_name, max_rounds=5)  # 5 rounds instead of 3
```

## 🚀 Deployment

This project is production-ready and includes a working `Dockerfile`. Deploy to:
- LiveKit Cloud
- AWS/GCP/Azure
- Self-hosted servers

See the [LiveKit deployment guide](https://docs.livekit.io/agents/ops/deployment/) for details.

## 📊 Project Structure

```
backend/
├── src/
│   ├── agent.py              # Main improv host agent (300+ lines)
│   ├── improv_state.py       # Game state management (200+ lines)
│   └── __init__.py
├── data/
│   └── scenarios.json        # 20 improv scenarios
├── .env.example              # Environment template
├── .env.local                # Your API keys (gitignored)
├── pyproject.toml            # Dependencies
└── README.md
```

## 🔧 Troubleshooting

### Common Issues

**Backend won't start**
- Check Python version: `python --version` (need 3.12+)
- Verify API keys in `.env.local`
- Run `download-files` command first

**Agent not responding**
- Check all API keys are valid
- Verify LiveKit server is running
- Check backend logs for errors

**Slow TTS**
- Murf Falcon is the fastest TTS API
- Check your internet connection
- Verify MURF_API_KEY is correct

## 🧪 Testing

### Console Mode (No Frontend)
```bash
uv run python src/agent.py console
```

### Development Mode (With Frontend)
```bash
uv run python src/agent.py dev
```

### Production Mode
```bash
uv run python src/agent.py start
```

## 📈 Performance

- **TTS Latency**: <1 second (Murf Falcon)
- **STT Accuracy**: 95%+ (AssemblyAI)
- **LLM Response**: 1-2 seconds (Gemini 2.5 Flash)
- **Total Latency**: 2-3 seconds end-to-end

## 🔐 Security

- Never commit `.env.local` to git
- Rotate API keys regularly
- Use environment variables for all secrets
- Enable rate limiting in production

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or pull requests.

## 👨‍💻 Author

**Gangadhar**
- GitHub: [@Gangadhar-NG-CODER](https://github.com/Gangadhar-NG-CODER)
- LinkedIn: [Connect](https://linkedin.com/in/gangadhar)

## 📄 License

MIT License - See [LICENSE](../LICENSE) file for details

## 🙏 Acknowledgments

- **Murf AI** - Falcon TTS API
- **LiveKit** - Voice agent framework
- **Google** - Gemini LLM
- **AssemblyAI** - Speech recognition

---

**Built with ❤️ for the Murf AI Voice Agents Challenge - Day 10**

[⬆ Back to Top](#improv-battle---backend-python)
