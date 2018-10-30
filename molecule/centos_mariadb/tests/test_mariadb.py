import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_mysql_is_installed(host):
    mysql = host.package("MariaDB-server")
    assert mysql.is_installed
    assert mysql.version.startswith("10.1")


def test_mysql_running_and_enabled(host):
    mysql = host.service("mariadb")
    assert mysql.is_running
    assert mysql.is_enabled


@pytest.mark.parametrize("db", [
    ("mydb1"),
    ("mydb2"),
])
def test_dbs_exist_and_are_accessible(host, db):
    output = host.check_output("mysql -e 'show databases;' mysql")
    assert db in output
