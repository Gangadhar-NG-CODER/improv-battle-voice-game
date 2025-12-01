import React from 'react';
import { Button } from '@/components/livekit/button';

interface WelcomeViewProps {
  startButtonText: string;
  onStartCall: () => void;
}

export const WelcomeView = ({
  startButtonText,
  onStartCall,
  ref,
}: React.ComponentProps<'div'> & WelcomeViewProps) => {
  const [name, setName] = React.useState('');

  return (
    <div
      ref={ref}
      className="relative flex min-h-screen items-center justify-center overflow-hidden bg-gradient-to-br from-indigo-950 via-purple-950 to-pink-950"
    >
      {/* Animated mesh gradient background */}
      <div className="absolute inset-0">
        <div className="absolute top-0 left-1/4 h-96 w-96 rounded-full bg-purple-600/30 blur-3xl animate-pulse"></div>
        <div className="absolute bottom-0 right-1/4 h-96 w-96 rounded-full bg-pink-600/30 blur-3xl animate-pulse [animation-delay:1.5s]"></div>
        <div className="absolute top-1/2 left-1/2 h-96 w-96 -translate-x-1/2 -translate-y-1/2 rounded-full bg-indigo-600/20 blur-3xl animate-pulse [animation-delay:3s]"></div>
      </div>

      {/* Grid pattern overlay */}
      <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,.02)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,.02)_1px,transparent_1px)] bg-[size:64px_64px]"></div>

      {/* Main content */}
      <div className="relative z-10 w-full max-w-3xl px-6">
        {/* Header */}
        <div className="mb-10 text-center">
          {/* Icon */}
          <div className="mb-6 flex justify-center">
            <div className="relative">
              <div className="absolute inset-0 rounded-full bg-gradient-to-r from-purple-600 to-pink-600 blur-2xl opacity-50"></div>
              <div className="relative flex h-20 w-20 items-center justify-center rounded-full bg-gradient-to-br from-purple-600 to-pink-600 shadow-2xl">
                <svg
                  width="40"
                  height="40"
                  viewBox="0 0 64 64"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M32 8C20 8 12 16 12 28C12 36 16 42 22 46C24 47 26 48 28 48C30 48 32 47 32 45C32 43 30 42 28 42C26 42 24 41 22 40C18 37 16 33 16 28C16 19 22 12 32 12C42 12 48 19 48 28C48 33 46 37 42 40C40 41 38 42 36 42C34 42 32 43 32 45C32 47 34 48 36 48C38 48 40 47 42 46C48 42 52 36 52 28C52 16 44 8 32 8Z"
                    fill="white"
                  />
                  <circle cx="24" cy="26" r="3" fill="#fbbf24" />
                  <circle cx="40" cy="26" r="3" fill="#fbbf24" />
                  <path
                    d="M22 34C24 38 28 40 32 40C36 40 40 38 42 34"
                    stroke="#fbbf24"
                    strokeWidth="2.5"
                    strokeLinecap="round"
                  />
                </svg>
              </div>
            </div>
          </div>

          {/* Title */}
          <h1 className="mb-4 bg-gradient-to-r from-white via-purple-200 to-pink-200 bg-clip-text text-6xl font-black tracking-tight text-transparent md:text-7xl">
            Improv Battle
          </h1>
          <p className="text-xl font-medium text-purple-200/80">
            Think Fast. Act Faster. Make Us Laugh.
          </p>
        </div>

        {/* Main card */}
        <div className="group relative">
          {/* Glow effect */}
          <div className="absolute -inset-0.5 rounded-3xl bg-gradient-to-r from-purple-600 to-pink-600 opacity-20 blur-xl transition duration-1000 group-hover:opacity-30"></div>

          {/* Card content */}
          <div className="relative rounded-3xl border border-white/10 bg-gradient-to-br from-white/10 to-white/5 p-8 shadow-2xl backdrop-blur-2xl md:p-10">
            {/* Features */}
            <div className="mb-8 grid grid-cols-4 gap-3">
              <div className="group/item relative overflow-hidden rounded-2xl border border-white/10 bg-gradient-to-br from-purple-500/10 to-transparent p-4 transition-all hover:scale-105 hover:border-purple-500/50">
                <div className="absolute inset-0 bg-gradient-to-br from-purple-500/0 to-purple-500/10 opacity-0 transition-opacity group-hover/item:opacity-100"></div>
                <div className="relative flex flex-col items-center gap-2">
                  <div className="text-3xl">🎤</div>
                  <p className="text-xs font-semibold text-white/90">Voice First</p>
                </div>
              </div>

              <div className="group/item relative overflow-hidden rounded-2xl border border-white/10 bg-gradient-to-br from-pink-500/10 to-transparent p-4 transition-all hover:scale-105 hover:border-pink-500/50">
                <div className="absolute inset-0 bg-gradient-to-br from-pink-500/0 to-pink-500/10 opacity-0 transition-opacity group-hover/item:opacity-100"></div>
                <div className="relative flex flex-col items-center gap-2">
                  <div className="text-3xl">🎭</div>
                  <p className="text-xs font-semibold text-white/90">Wild Scenarios</p>
                </div>
              </div>

              <div className="group/item relative overflow-hidden rounded-2xl border border-white/10 bg-gradient-to-br from-indigo-500/10 to-transparent p-4 transition-all hover:scale-105 hover:border-indigo-500/50">
                <div className="absolute inset-0 bg-gradient-to-br from-indigo-500/0 to-indigo-500/10 opacity-0 transition-opacity group-hover/item:opacity-100"></div>
                <div className="relative flex flex-col items-center gap-2">
                  <div className="text-3xl">⚡</div>
                  <p className="text-xs font-semibold text-white/90">Real Reactions</p>
                </div>
              </div>

              <div className="group/item relative overflow-hidden rounded-2xl border border-white/10 bg-gradient-to-br from-purple-500/10 to-transparent p-4 transition-all hover:scale-105 hover:border-purple-500/50">
                <div className="absolute inset-0 bg-gradient-to-br from-purple-500/0 to-purple-500/10 opacity-0 transition-opacity group-hover/item:opacity-100"></div>
                <div className="relative flex flex-col items-center gap-2">
                  <div className="text-3xl">🎬</div>
                  <p className="text-xs font-semibold text-white/90">3 Rounds</p>
                </div>
              </div>
            </div>

            {/* How it works */}
            <div className="mb-8 rounded-2xl border border-white/10 bg-gradient-to-br from-purple-500/10 via-pink-500/5 to-transparent p-6 backdrop-blur-sm">
              <h2 className="mb-5 text-center text-lg font-bold text-white">How It Works</h2>
              <div className="space-y-4">
                <div className="flex items-start gap-4">
                  <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-gradient-to-br from-purple-500 to-pink-500 text-sm font-bold text-white shadow-lg">
                    1
                  </div>
                  <p className="pt-1 text-sm leading-relaxed text-white/80">
                    Host sets up a wild improv scenario
                  </p>
                </div>
                <div className="flex items-start gap-4">
                  <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-gradient-to-br from-purple-500 to-pink-500 text-sm font-bold text-white shadow-lg">
                    2
                  </div>
                  <p className="pt-1 text-sm leading-relaxed text-white/80">
                    You improvise the character and situation
                  </p>
                </div>
                <div className="flex items-start gap-4">
                  <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-gradient-to-br from-purple-500 to-pink-500 text-sm font-bold text-white shadow-lg">
                    3
                  </div>
                  <p className="pt-1 text-sm leading-relaxed text-white/80">
                    Host reacts with honest feedback and moves on
                  </p>
                </div>
              </div>
            </div>

            {/* Form */}
            <div className="space-y-5">
              <div>
                <label htmlFor="name" className="mb-2 block text-sm font-semibold text-white/90">
                  Your Stage Name
                </label>
                <input
                  id="name"
                  type="text"
                  placeholder="Enter your name"
                  value={name}
                  onChange={(e) => setName(e.target.value)}
                  className="h-14 w-full rounded-xl border border-white/20 bg-white/10 px-5 text-lg text-white placeholder:text-white/40 backdrop-blur-sm transition-all focus:border-purple-500 focus:bg-white/15 focus:outline-none focus:ring-2 focus:ring-purple-500/50"
                  required
                />
              </div>

              <Button
                variant="primary"
                size="lg"
                onClick={() => {
                  if (name.trim()) {
                    localStorage.setItem('playerName', name.trim());
                    onStartCall();
                  }
                }}
                disabled={!name.trim()}
                className="group/btn relative h-16 w-full overflow-hidden rounded-xl bg-gradient-to-r from-purple-600 to-pink-600 text-lg font-bold text-white shadow-2xl shadow-purple-500/50 transition-all hover:scale-[1.02] hover:shadow-purple-500/70 disabled:cursor-not-allowed disabled:opacity-50 disabled:hover:scale-100"
              >
                <div className="absolute inset-0 bg-gradient-to-r from-purple-500 to-pink-500 opacity-0 transition-opacity group-hover/btn:opacity-100"></div>
                <span className="relative flex items-center justify-center gap-3">
                  <span className="text-2xl">🎤</span>
                  <span>Start Improv Battle</span>
                  <svg
                    className="h-5 w-5 transition-transform group-hover/btn:translate-x-1"
                    fill="none"
                    viewBox="0 0 24 24"
                    stroke="currentColor"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M13 7l5 5m0 0l-5 5m5-5H6"
                    />
                  </svg>
                </span>
              </Button>
            </div>

            {/* Footer */}
            <div className="mt-6 text-center">
              <p className="text-xs font-medium text-white/50">
                Powered by Murf Falcon TTS • The Fastest Voice AI
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
