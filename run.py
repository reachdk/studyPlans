"""Render studyPlans artifact prompts."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


CONFIG = Path(__file__).with_name("config.yaml")
VERIFY = Path(__file__).parent / "prompts" / "verify.md"


def load_config() -> dict:
    # ponytail: use Ruby's bundled YAML parser until Python dependencies are formalized.
    result = subprocess.run(
        [
            "ruby",
            "-ryaml",
            "-rjson",
            "-e",
            "print JSON.generate(YAML.load_file(ARGV.fetch(0)))",
            str(CONFIG),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


def get_artifact(config: dict, name: str) -> dict:
    artifact = config["artifacts"].get(name)
    if artifact is None:
        raise ValueError(f"unknown artifact: {name}")
    if not artifact["enabled"]:
        raise ValueError(f"artifact is disabled: {name}")
    return artifact


def render_prompt(name: str) -> str:
    config = load_config()
    artifact = get_artifact(config, name)

    return "\n\n".join(
        (
            config["generation"]["common_instruction"].strip(),
            artifact["instruction"].strip(),
        )
    )


def render_verify(name: str) -> str:
    config = load_config()
    artifact = get_artifact(config, name)
    contract = "\n\n".join(
        (
            config["generation"]["common_instruction"].strip(),
            artifact["instruction"].strip(),
        )
    )
    return f"{VERIFY.read_text().strip()}\n\n## Artifact Contract\n\n{contract}"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["artifacts", "prompt", "verify"])
    parser.add_argument("artifact", nargs="?")
    args = parser.parse_args()

    try:
        if args.command == "artifacts":
            config = load_config()
            print(
                "\n".join(
                    name
                    for name, artifact in config["artifacts"].items()
                    if artifact["enabled"]
                )
            )
            return

        if args.artifact is None:
            parser.error(f"{args.command} requires an artifact")
        renderer = render_prompt if args.command == "prompt" else render_verify
        print(renderer(args.artifact))
    except (FileNotFoundError, KeyError, ValueError, subprocess.CalledProcessError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
