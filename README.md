# 🎭 Improv Battle - Voice Improv Game Show

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![Next.js 15](https://img.shields.io/badge/Next.js-15-black)](https://nextjs.org/)
[![LiveKit](https://img.shields.io/badge/LiveKit-Agents-green)](https://livekit.io/)

> **DAY 10 of the Murf AI Voice Agents Challenge**
>
> A voice-first improv game show where an AI host puts you through hilarious scenarios and reacts with honest, varied feedback. Think fast, act faster, make us laugh!

![Improv Battle](https://img.shields.io/badge/Status-Production%20Ready-success)

## 🎬 What Is This?

**Improv Battle** is an interactive voice game where you perform short-form improv scenes while an AI host watches, reacts, and judges your performance. It's like being on a TV improv show, but powered by cutting-edge voice AI.

### Game Flow

1. **Welcome** - Host greets you and asks for your name
2. **Round 1-3** - Host announces a wild scenario, you improvise, host reacts
3. **Final Summary** - Host summarizes your improv style and performance

### Example Scenarios

- "You are a barista who has to tell a customer that their latte is actually a portal to another dimension."
- "You are a time-travelling tour guide explaining modern smartphones to someone from the 1800s."
- "You are a restaurant waiter who must calmly tell a customer that their order has escaped the kitchen."

## ✨ Features

### 🎭 AI Improv Host
- High-energy, charismatic TV host personality
- Varied reactions (amused, critical, surprised, teasing)
- Honest but respectful feedback
- Quick comedic timing

### 🎤 Voice-First Experience
- Natural conversation with AI
- Real-time speech recognition
- Ultra-fast TTS responses (Murf Falcon)
- Smooth turn-taking

### 🎬 20 Unique Scenarios
- Wild, creative situations
- Different difficulty levels
- Never repeats in same session
- Encourages character work

### 🎨 Theatrical UI
- Stage curtain design
- Spotlight effects
- Round indicator (theater lights)
- Scenario cue cards
- Audience silhouettes

## 🏗️ Tech Stack

### Backend
- **Framework**: LiveKit Agents Python SDK
- **LLM**: Google Gemini 2.5 Flash
- **TTS**: Murf Falcon (fastest TTS API)
- **STT**: AssemblyAI
- **Turn Detection**: Multilingual Model

### Frontend
- **Framework**: Next.js 15 (App Router)
- **UI**: React 19 + Tailwind CSS 4
- **Voice SDK**: LiveKit Components React
- **Animations**: CSS animations + transitions

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- Node.js 18+
- pnpm (or npm)
- [uv](https://docs.astral.sh/uv/) package manager

### 1. Clone and Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd DAY10
```

### 2. Backend Setup

```bash
cd backend

# Install dependencies
uv sync

# Copy environment variables
cp .env.example .env.local

# Edit .env.local with your API keys:
# - LIVEKIT_URL, LIVEKIT_API_KEY, LIVEKIT_API_SECRET
# - MURF_API_KEY
# - ASSEMBLYAI_API_KEY
# - GOOGLE_API_KEY

# Download required models
uv run python src/agent.py download-files

# Run the agent
uv run python src/agent.py dev
```

### 3. Frontend Setup

```bash
cd frontend

# Install dependencies
pnpm install

# Copy environment variables
cp .env.example .env.local

# Edit .env.local with your LiveKit credentials

# Run the development server
pnpm dev
```

### 4. Play the Game

1. Open http://localhost:3000 in your browser
2. Enter your stage name
3. Click "Take The Stage"
4. Follow the host's instructions
5. Improvise your heart out!

## 📁 Project Structure

```
DAY10/
├── backend/
│   ├── src/
│   │   ├── agent.py          # Main improv host agent
│   │   └── improv_state.py   # Game state management
│   ├── data/
│   │   └── scenarios.json    # 20 improv scenarios
│   ├── pyproject.toml
│   └── README.md
├── frontend/
│   ├── app/
│   │   ├── page.tsx          # Main entry
│   │   └── session/page.tsx  # Game session
│   ├── components/
│   │   └── app/
│   │       ├── welcome-view.tsx    # Theatrical welcome page
│   │       └── stage-view.tsx      # Live performance stage
│   ├── package.json
│   └── README.md
└── README.md
```

## 🎮 How to Play

### Tips for Great Improv

1. **Commit to the character** - Go all in, don't hold back
2. **Yes, and...** - Build on the scenario, don't deny it
3. **Be specific** - Details make it funnier
4. **React emotionally** - Show how your character feels
5. **Have fun** - The host can tell when you're enjoying it

### Ending a Scene

- Say "End scene" when you're done
- Or just pause and the host will react
- Or let the host interrupt if they want

### Early Exit

- Say "stop game" or "end show" to quit early
- Host will gracefully wrap up

## 🎨 Customization

### Add More Scenarios

Edit `backend/data/scenarios.json`:

```json
{
  "id": 21,
  "scenario": "Your custom scenario here",
  "difficulty": "medium"
}
```

### Change Round Count

In `backend/src/agent.py`, modify:

```python
start_game(room_name, player_name, max_rounds=5)  # 5 rounds instead of 3
```

### Adjust Host Personality

Edit the system prompt in `backend/src/agent.py` under `Assistant` class.

### Change UI Theme

Modify colors in `frontend/components/app/welcome-view.tsx` and `stage-view.tsx`.

## 🧪 Testing

### Backend Console Mode

Test the agent without the frontend:

```bash
cd backend
uv run python src/agent.py console
```

### Frontend Development

```bash
cd frontend
pnpm dev
```

## 🚀 Deployment

### Backend

Deploy to LiveKit Cloud, AWS, GCP, or self-hosted servers.

See [LiveKit deployment guide](https://docs.livekit.io/agents/ops/deployment/).

### Frontend

Deploy to Vercel, Netlify, or any Next.js hosting platform.

```bash
cd frontend
pnpm build
```

## 📝 API Keys Required

- **LiveKit**: Get from [LiveKit Cloud](https://cloud.livekit.io/)
- **Murf AI**: Get from [Murf AI](https://murf.ai/)
- **AssemblyAI**: Get from [AssemblyAI](https://www.assemblyai.com/)
- **Google Gemini**: Get from [Google AI Studio](https://aistudio.google.com/)

## 🤝 Contributing

This project is part of the Murf AI Voice Agents Challenge. Feel free to:
- Fork and adapt for your own games
- Add new scenarios
- Improve the UI
- Share your performances!

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Fork and adapt for your own games
- Add new scenarios
- Improve the UI
- Share your performances!

## 👨‍💻 Author

**Gangadhar**
- GitHub: [@Gangadhar-NG-CODER](https://github.com/Gangadhar-NG-CODER)
- LinkedIn: [Connect with me](https://linkedin.com/in/gangadhar)

## 📄 License

MIT License - See [LICENSE](LICENSE) file for details.

## 🎬 Demo Video

[Watch the demo on LinkedIn](#)

## 🙏 Acknowledgments

- **Murf AI** for the amazing Falcon TTS API
- **LiveKit** for the voice agent framework
- **Google Gemini** for the LLM
- **AssemblyAI** for speech recognition

## 📊 Project Stats

- **Lines of Code**: ~3,000+
- **Components**: 15+
- **Scenarios**: 20 unique improv situations
- **Development Time**: Day 10 of challenge

---

**Built with ❤️ for the Murf AI Voice Agents Challenge - Day 10**

*Think Fast. Act Faster. Make Us Laugh.* 🎭

**Tags**: #MurfAIVoiceAgentsChallenge #10DaysofAIVoiceAgents #VoiceAI #ImprovComedy #LiveKit
