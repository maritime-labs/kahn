# -*- coding: utf-8 -*-
# (c) 2022 Andreas Motl <andreas.motl@panodata.org>
# License: GNU Affero General Public License, Version 3
import re

from click.testing import CliRunner

from kahn.cli import cli


def test_cli_version():
    """Test kahn --version"""
    runner = CliRunner()

    result = runner.invoke(cli, ["--version"])

    assert re.match(r"cli, version \d+\.\d+\.\d+", result.stdout) is not None
