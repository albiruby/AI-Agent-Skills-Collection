---
name: game-multiplayer-networking
description: Design multiplayer and online features: architecture (client-server, P2P, relay, rollback), sync models, matchmaking, lobbies, voice/chat, anti-cheat, backend services, leaderboards, cloud saves, cost and security.
---

# Multiplayer & Online

## Decide scope
Local co-op/split-screen, async (turn-based, ghost/leaderboard), online co-op (2-8), competitive PvP, large-scale (MMO/BR). Cost and complexity rise steeply; avoid real-time online for solo/small teams unless core to the pitch.

## Architecture
| Model | Use for | Notes |
|---|---|---|
| Authoritative dedicated server | competitive, persistent worlds | best anti-cheat, higher cost |
| Listen-server / host-client | co-op, casual | host advantage, NAT/relay needed |
| P2P + relay (lockstep) | RTS/fighting | requires determinism |
| Rollback netcode | fighting, fast 1v1 | deterministic sim, input prediction |
| Turn-based via REST/WebSocket | cards, strategy, async | simple, cheap |

## Sync techniques
Client-side prediction + server reconciliation, entity interpolation, snapshot delta compression, interest management (relevancy), lag compensation (rewind hitboxes), tick rates (e.g. 20-128 Hz by genre), unreliable vs reliable channels, bandwidth budget per player, authoritative inventory/economy always server-side.

## Services & tools
Netcode: Unity Netcode for GameObjects/Entities, Mirror, Fish-Net, Photon (PUN/Fusion/Quantum), Unreal replication, Godot high-level multiplayer/ENet/WebRTC, Colyseus, Nakama, Steam Networking/Epic Online Services/PlayFab/Firebase. Web: WebSocket (TCP) vs WebRTC DataChannel/WebTransport (UDP-like).
Features: auth (guest, platform, OAuth), lobbies/party, matchmaking (Elo/Glicko/TrueSkill, region/ping), voice/text chat (moderation, report/block), friends, leaderboards, cloud saves, replays, spectator, reconnection.

## Security & fair play
Never trust the client; validate inputs, rate-limit, sign IAP receipts server-side, obfuscation is not security, anti-cheat (EAC/BattlEye/server analytics) only for PvP at scale, DDoS protection, GDPR/COPPA aware (chat with minors).

## Ops
Load testing, bot clients, simulated latency/packet loss (100-300 ms, 2-5% loss) in QA, region deployment, autoscaling (Agones, Hathora, Multiplay, GameLift), cost model per CCU, monitoring/alerts.

## Output
Architecture diagram (Mermaid), sync design, message/protocol list, service matrix, cost estimate approach, security checklist, test plan under bad network.
