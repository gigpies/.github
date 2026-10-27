# Contributing to GigPies

GigPies is a **terminal application (TUI)** for live-band audio and lighting.
[Choose the module](https://github.com/gigpies/gigpies/blob/main/docs/README.md)
that owns your change. Small fixes can go straight to a pull request; discuss
large features in an issue first.

1. Fork the repository and create a branch.
2. Use its pinned Rust toolchain. Follow the local build/test guide.
3. Keep the change focused, add relevant tests and update the owning guide.
4. Open a PR explaining the problem, result and checks you ran.

PRs need passing CI, resolved review conversations and a maintainer review.
The maintainer retains an administrative override for repository maintenance.
Fork Actions require maintainer approval before running. CI uses hosted runners,
synthetic inputs and no audio/MIDI/DMX hardware.

For TUI changes, include a screenshot and terminal dimensions. Report hardware
and listening results separately from software tests. Keep recordings, credentials,
private device settings and generated media out of commits.

Each repository's license applies to its contributions. Lux has no project
license selected yet; discuss code contributions there with the maintainer first.
[Security reports](SECURITY.md) · [Automation and releases](AUTOMATION.md)
