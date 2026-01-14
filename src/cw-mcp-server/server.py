#!/usr/bin/env python3

# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

"""Compatibility wrapper for running the MCP server from the legacy path."""

from __future__ import annotations

import os
import sys

# Ensure the parent src/ directory is on sys.path so cw_mcp_server is importable.
_current_dir = os.path.dirname(os.path.abspath(__file__))
_src_dir = os.path.dirname(_current_dir)
if _src_dir not in sys.path:
    sys.path.insert(0, _src_dir)

from cw_mcp_server.server import main


if __name__ == "__main__":
    main()
