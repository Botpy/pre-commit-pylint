#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""A wrapper for pylint that implements score limit and Python 3 porting check.
"""
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import re
import sys

import six
from pylint import epylint as lint


# Code copy from:
# https://github.com/sebdah/git-pylint-commit-hook/blob/master/git_pylint_commit_hook/commit_hook.py#L84-L98
_SCORE_REGEXP = re.compile(
    r'^\s+Your\ code\ has\ been\ rated\ at\ (\-?[0-9\.]+)/10')


def _parse_score(output):
    """Parse the score out of pylint's output as a float
    If the score is not found, return 0.0.
    """
    # If output is empty that means the file is empty.
    if output.strip() == "":
        return 10.0

    for line in output.splitlines():
        if isinstance(line, six.binary_type):
            line = line.decode("utf-8")

        match = re.match(_SCORE_REGEXP, line)
        if match:
            return float(match.group(1))
    return 0.0


def _run_pylint(argv=None):
    return lint.py_run(" ".join(argv), return_std=True)


def check_score(argv=None):
    """Check score limit."""

    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(__name__)
    parser.add_argument('filenames', nargs='*', help='filenames to check.')

    parser.add_argument("--limit", default=8.0, type=float,
                        help=('Score limit, files with a lower score will '
                              'stop the commit. Default: 8.0'))

    ns, argv = parser.parse_known_args(argv)

    all_passed = True

    for i, filename in enumerate(ns.filenames):
        print("Running pylint on %s (file %d/%d).." % (
            filename, i + 1, len(ns.filenames)), end="\t")

        pylint_stdout, pylint_stderr = _run_pylint([filename] + argv)

        output = pylint_stdout.getvalue()
        score = _parse_score(output)
        passed = score >= ns.limit
        print("%.2f/%.2f" % (score, ns.limit), end="\t")

        if (not passed):
            print("FAILED")
            print(output)
            all_passed = False
        else:
            print("PASSED")

    sys.exit(all_passed - 1)


def check_py3k():
    """Check Python3 porting."""
    argv = sys.argv[1:]
    check_score(argv + ["--py3k", "--limit=10"])
