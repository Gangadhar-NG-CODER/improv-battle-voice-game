'use client';

import { useVoiceAssistant } from '@livekit/components-react';
import { useState, useEffect } from 'react';

export function StageView() {
  const { state, audioTrack } = useVoiceAssistant();
  const [currentRound, setCurrentRound] = useState(1);
  const [maxRounds] = useState(3);
  const [scenario, setScenario] = useState('');
  const [showScenario, setShowScenario] = useState(false);

  // Determine icon and status based on agent state
  const getStatusInfo = () => {
    switch (state) {
      case 'speaking':
        return { icon: '🎭', label: 'Host is speaking...', color: 'text-purple-400' };
      case 'listening':
        return { icon: '🎤', label: 'Your turn to perform!', color: 'text-green-400' };
      case 'thinking':
        return { icon: '🤔', label: 'Host is thinking...', color: 'text-yellow-400' };
      default:
        return { icon: '⏸️', label: 'Ready', color: 'text-slate-400' };
    }
  };

  const statusInfo = getStatusInfo();

  // Spotlight color based on state
  const getSpotlightColor = () => {
    switch (state) {
      case 'speaking':
        return 'from-purple-500/30 via-purple-900/20';
      case 'listening':
        return 'from-green-500/30 via-green-900/20';
      case 'thinking':
        return 'from-yellow-500/30 via-yellow-900/20';
      default:
        return 'from-slate-500/20 via-slate-900/10';
    }
  };

  return (
    <div className="relative flex h-screen flex-col overflow-hidden bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950">
      {/* Round Indicator - Theater Lights */}
      <div className="absolute left-4 top-4 z-20 md:left-8 md:top-8">
        <div className="rounded-lg border border-yellow-500/30 bg-slate-900/80 px-4 py-2 backdrop-blur-sm">
          <div className="flex items-center gap-2">
            {[...Array(maxRounds)].map((_, i) => (
              <div
                key={i}
                className={`h-3 w-3 rounded-full transition-all ${
                  i < currentRound
                    ? 'bg-yellow-400 shadow-lg shadow-yellow-400/50'
                    : 'bg-slate-600'
                }`}
              />
            ))}
            <span className="ml-2 text-sm font-semibold text-yellow-400">
              Round {currentRound}/{maxRounds}
            </span>
          </div>
        </div>
      </div>

      {/* Status Indicator */}
      <div className="absolute right-4 top-4 z-20 md:right-8 md:top-8">
        <div className="rounded-lg border border-purple-500/30 bg-slate-900/80 px-4 py-2 backdrop-blur-sm">
          <div className="flex items-center gap-2">
            <span className="text-xl">{statusInfo.icon}</span>
            <span className={`text-sm font-semibold ${statusInfo.color}`}>
              {statusInfo.label}
            </span>
          </div>
        </div>
      </div>

      {/* Scenario Card */}
      {showScenario && scenario && (
        <div className="absolute left-1/2 top-20 z-20 w-full max-w-2xl -translate-x-1/2 px-4 md:top-24">
          <div className="animate-slide-down rounded-lg border-2 border-purple-500/50 bg-white p-6 shadow-2xl">
            <div className="mb-2 flex items-center gap-2">
              <span className="text-2xl">📋</span>
              <h3 className="font-bold text-slate-900" style={{ fontFamily: 'Courier New, monospace' }}>
                CUE CARD
              </h3>
            </div>
            <p className="text-slate-700" style={{ fontFamily: 'Courier New, monospace' }}>
              {scenario}
            </p>
          </div>
        </div>
      )}

      {/* Main Stage Area */}
      <div className="relative flex flex-1 items-center justify-center">
        {/* Spotlight */}
        <div
          className={`absolute h-[500px] w-[500px] rounded-full bg-gradient-radial ${getSpotlightColor()} to-transparent blur-3xl transition-all duration-500 ${
            state === 'speaking' || state === 'listening' ? 'animate-pulse' : ''
          }`}
        />

        {/* Center Icon */}
        <div className="relative z-10 flex flex-col items-center gap-6">
          <div
            className={`text-9xl transition-transform duration-300 ${
              state === 'speaking' || state === 'listening' ? 'scale-110' : 'scale-100'
            }`}
          >
            {statusInfo.icon}
          </div>

          {/* Audio Visualizer */}
          {(state === 'speaking' || state === 'listening') && (
            <div className="flex items-end gap-1">
              {[...Array(7)].map((_, i) => (
                <div
                  key={i}
                  className={`w-2 rounded-full ${
                    state === 'speaking' ? 'bg-purple-500' : 'bg-green-500'
                  }`}
                  style={{
                    height: `${Math.random() * 40 + 20}px`,
                    animation: `pulse ${Math.random() * 0.5 + 0.5}s ease-in-out infinite`,
                    animationDelay: `${i * 0.1}s`,
                  }}
                />
              ))}
            </div>
          )}
        </div>
      </div>

      {/* Stage Floor */}
      <div className="relative h-32 bg-gradient-to-t from-amber-950/50 to-transparent">
        {/* Audience Silhouettes */}
        <div className="absolute bottom-0 left-0 right-0 flex items-end justify-center gap-1 px-4 pb-2">
          {[...Array(20)].map((_, i) => (
            <div
              key={i}
              className="h-8 w-4 rounded-t-full bg-slate-950/80"
              style={{
                height: `${Math.random() * 20 + 20}px`,
              }}
            />
          ))}
        </div>
      </div>

      {/* Control Bar */}
      <div className="absolute bottom-4 left-1/2 z-20 -translate-x-1/2">
        <div className="flex items-center gap-4 rounded-full border border-purple-500/30 bg-slate-900/80 px-6 py-3 backdrop-blur-sm">
          <button className="text-2xl transition-transform hover:scale-110">🎤</button>
          <button className="text-2xl transition-transform hover:scale-110">💬</button>
          <button className="text-2xl transition-transform hover:scale-110">❌</button>
        </div>
      </div>
    </div>
  );
}
