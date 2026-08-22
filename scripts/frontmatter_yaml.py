#!/usr/bin/env python3
"""Strict YAML parsing shared by guide validation and sync preflight.

PyYAML's safe loader is used instead of the repository's tolerant regex
extractor so malformed metadata cannot pass validation and then be interpreted
differently by downstream consumers.  Duplicate keys are rejected because a
last-key-wins result hides which value an author intended.
"""

from __future__ import annotations

from typing import Any

import yaml


class FrontmatterError(ValueError):
    """Raised when a frontmatter block is not safe, unambiguous metadata."""


class _UniqueKeyLoader(yaml.SafeLoader):
    """SafeLoader variant that rejects duplicate mapping keys."""


def _construct_unique_mapping(
    loader: _UniqueKeyLoader,
    node: yaml.nodes.MappingNode,
    deep: bool = False,
) -> dict[Any, Any]:
    loader.flatten_mapping(node)
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            hash(key)
        except TypeError as exc:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                "found an unhashable mapping key",
                key_node.start_mark,
            ) from exc
        if key in mapping:
            raise yaml.constructor.ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"found duplicate key {key!r}",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


_UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_unique_mapping,
)


# These fields are strings in docs/skill-template.md.  PyYAML follows YAML 1.1
# scalar rules, so an unquoted ISO code such as `NO` becomes boolean False.
# Rejecting that coercion protects MCP jurisdiction routing and other consumers.
_STRING_FIELDS = {
    "name",
    "description",
    "jurisdiction",
    "category",
    "tax_year_notes",
    "verified_by",
    "reviewed_by",
    "review_status",
    "license",
}


def _problem_text(exc: yaml.YAMLError) -> str:
    problem = getattr(exc, "problem", None) or exc.__class__.__name__
    mark = getattr(exc, "problem_mark", None)
    if mark is None:
        return str(problem)
    return f"line {mark.line + 1}, column {mark.column + 1}: {problem}"


def load_frontmatter(block: str) -> dict[str, Any]:
    """Parse one frontmatter block or raise :class:`FrontmatterError`.

    The returned value must be a mapping with string keys.  Known string fields
    and ``depends_on`` receive small type checks so valid-but-misinterpreted YAML
    (notably ``jurisdiction: NO``) also fails closed.
    """

    try:
        metadata = yaml.load(block, Loader=_UniqueKeyLoader)
    except yaml.YAMLError as exc:
        raise FrontmatterError(_problem_text(exc)) from exc

    if not isinstance(metadata, dict):
        actual = "null" if metadata is None else type(metadata).__name__
        raise FrontmatterError(f"frontmatter root must be a mapping, got {actual}")

    non_string_keys = [key for key in metadata if not isinstance(key, str)]
    if non_string_keys:
        raise FrontmatterError(
            f"frontmatter keys must be strings, got {non_string_keys[0]!r}"
        )

    for key in sorted(_STRING_FIELDS & metadata.keys()):
        value = metadata[key]
        if not isinstance(value, str):
            raise FrontmatterError(
                f"`{key}` must be a string, got {type(value).__name__}"
            )

    if "depends_on" in metadata:
        dependencies = metadata["depends_on"]
        if not isinstance(dependencies, list):
            raise FrontmatterError(
                f"`depends_on` must be a YAML list, got {type(dependencies).__name__}"
            )
        if any(not isinstance(item, str) or not item.strip() for item in dependencies):
            raise FrontmatterError("`depends_on` entries must be non-empty strings")

    return metadata
