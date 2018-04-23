"""Tests for the ansible percona repository role."""
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_percona_release_repo_package(host):
    """Test that the percona-release package is installed."""
    percona_release_pkg = host.package("percona-release")

    assert percona_release_pkg.is_installed
