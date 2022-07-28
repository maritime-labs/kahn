# -*- coding: utf-8 -*-
# (c) 2022 Andreas Motl <andreas.motl@panodata.org>
# License: GNU Affero General Public License, Version 3
import re
import shlex
from unittest import mock

from click.testing import CliRunner

from kahn.cli import cli


def test_cli_version():
    """
    Test `kahn --version`.
    """
    runner = CliRunner()
    result = runner.invoke(cli, ["--version"], catch_exceptions=False)
    assert re.match(r"cli, version \d+\.\d+\.\d+", result.stdout) is not None


@mock.patch("kahn.cli.ForwardingEngine")
def test_cli_forward(_, mock_serial):
    """
    Test `kahn forward`.
    """
    runner = CliRunner()
    result = runner.invoke(
        cli,
        shlex.split("--verbose forward --source=serial:///dev/foo --target=file:///dev/bar"),
        catch_exceptions=False,
    )
    assert result.stdout == "Ready.\n"
