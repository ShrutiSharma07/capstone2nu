#!/usr/bin/env python
#   -*- coding: utf-8 -*-

import os
import subprocess
import sys
import glob
import shutil

from sys import version_info
py3 = version_info[0] == 3
py2 = not py3
if py2:
    FileNotFoundError = OSError


def install_pyb():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pybuilder"])
    except subprocess.CalledProcessError as e:
        sys.exit(e.returncode)


script_dir = os.path.dirname(os.path.realpath(__file__))
exit_code = 0

try:
    subprocess.check_call(["pyb", "--version"])
except FileNotFoundError as e:
    if py3 or py2 and e.errno == 2:
        install_pyb()
    else:
        raise
except subprocess.CalledProcessError as e:
    if e.returncode == 127:
        install_pyb()
    else:
        sys.exit(e.returncode)

try:
    from pybuilder.cli import main
    # verbose, debug, skip all optional...
    if main("-v", "-X", "-o", "--reset-plugins", "clean", "package"):
        raise RuntimeError("PyBuilder build failed")

    from pybuilder.reactor import Reactor
    reactor = Reactor.current_instance()
    project = reactor.project
    dist_dir = project.expand_path("$dir_dist")

    for src_file in glob.glob(os.path.join(dist_dir, "*")):
        file_name = os.path.basename(src_file)
        target_file_name = os.path.join(script_dir, file_name)
        if os.path.exists(target_file_name):
            if os.path.isdir(target_file_name):
                shutil.rmtree(target_file_name)
            else:
                os.remove(target_file_name)
        shutil.move(src_file, script_dir)
    setup_args = sys.argv[1:]
    subprocess.check_call([sys.executable, "setup.py"] + setup_args, cwd=script_dir)
except subprocess.CalledProcessError as e:
    exit_code = e.returncode
sys.exit(exit_code)
