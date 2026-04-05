"""GroundTruth CLI entry point."""

import click
from groundtruth import __version__


@click.group()
@click.version_option(__version__)
def main() -> None:
    """GroundTruth — civic accountability infrastructure."""


@main.command()
@click.argument("source")
def ingest(source: str) -> None:
    """Ingest a data source (URL or file path)."""
    click.echo(f"Ingesting: {source}")


@main.command()
@click.argument("brief_hash")
def verify(brief_hash: str) -> None:
    """Verify a published brief by its SHA256 hash."""
    click.echo(f"Verifying: {brief_hash}")


@main.command()
@click.argument("topic")
def brief(topic: str) -> None:
    """Generate an accountability brief for a topic."""
    click.echo(f"Generating brief for: {topic}")
