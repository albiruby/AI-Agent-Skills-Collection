# Start here (10 minutes, Gemini app)

1. Create a Gem named **Image Consistency Director**; paste block A from `GEM-INSTRUCTIONS.md`.
2. Open the Gem and say: "New project: <one sentence>." Answer the six intake questions.
3. Approve the **LOCK STYLE & THEME** block it writes. Save it as `STYLE_BIBLE.md`.
4. Ask for 3 probes (object, character, scene). Generate them in a normal Gemini chat with the lock block pasted. Pick one anchor per subject and save it as `ANCHOR_<type>_<name>_v1.png`.
5. Ask the Gem for a character sheet prompt (template 3) and generate it; approve it as the character anchor.
6. For each asset: new message, paste the two-part prompt, attach the anchors.
7. Every 5-10 assets: attach anchor + outputs and run the QA prompt (template 10).
8. If something drifts: start a fresh chat with lock + anchors, then use template 4 or 11.
9. Using Google Flow? Fill `FLOW-3-SLOTS.md` into the three slots.
10. Many assets? Use `pack_to_json.py` and `batch_generate.py` (see `AI-STUDIO-AND-API.md`).
