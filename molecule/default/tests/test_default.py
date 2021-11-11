#!/usr/bin/env python

import os
import stat
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_steam_user(host):
    user = host.user("steam")
    assert user.exists
    assert user.home == f"/home/{user.name}"
    assert user.group == "steam"


def test_systemd_service_file(host):
    user_name = "root"
    file_name = "/etc/systemd/system/satisfactory.service"
    file = host.file(file_name)
    assert file.exists
    assert file.is_file
    assert file.user == user_name
    assert file.group == user_name
    assert file.mode == 0o644


def test_systemd_service(host):
    service = host.service("satisfactory.service")
    assert service.is_enabled
    assert service.is_running


def test_satisfactory_server(host):
    socket = host.socket("udp://0.0.0.0:7777")
    assert socket.is_listening


def test_systemd_service_test_file(host):
    user_name = "root"
    file_name = "/etc/systemd/system/satisfactory-test.service"
    file = host.file(file_name)
    assert file.exists
    assert file.is_file
    assert file.user == user_name
    assert file.group == user_name
    assert file.mode == 0o644


def test_systemd_service_test(host):
    service = host.service("satisfactory-test.service")
    assert service.is_enabled
    assert service.is_running


def test_satisfactory_server_test(host):
    socket = host.socket("udp://0.0.0.0:7778")
    assert socket.is_listening
