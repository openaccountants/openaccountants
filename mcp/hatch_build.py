"""Bundle the generated skill packages into MCP sdists and wheels."""

from __future__ import annotations

from pathlib import Path

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    """Include external repo data without copying it into the working tree."""

    def initialize(self, version: str, build_data: dict) -> None:
        project_root = Path(self.root)
        source_packages = project_root.parent / "packages"
        sdist_packages = project_root / "_bundled_packages"

        if source_packages.is_dir():
            packages = source_packages
        elif sdist_packages.is_dir():
            packages = sdist_packages
        else:
            raise RuntimeError(
                "Cannot build openaccountants-mcp without the generated packages/ tree"
            )

        if not any(packages.rglob("*.md")):
            raise RuntimeError(f"No skill markdown found under {packages}")

        destination = (
            "_bundled_packages"
            if self.target_name == "sdist"
            else "openaccountants_mcp/packages"
        )
        build_data["force_include"][str(packages)] = destination
