# Modern Mail agent integrations

Canonical source: the private ModernMail/modern-mail repository, integrations/agents/. This public distribution is a one-way snapshot only; changes must originate in the private source. No application code or private Git history is distributed.

- anthropic/: Claude plugin bundle and remote MCP configuration.
- openai/: OpenAI package source; package.py builds the archive.
- shared/: common guidance and connection metadata.

main tracks latest source, not an approved platform release. Platform releases use separate immutable anthropic-vX.Y.Z and openai-vX.Y.Z tags and reviewed GitHub release assets. SOURCE.json records the exact source commit and per-file hashes. Never infer directory approval or OAuth qualification from a source snapshot.

Sign in through the host OAuth flow; never paste tokens into package files. Review and purchase letters in Modern Mail.
