# Ansible role - satisfactory
[![License](https://img.shields.io/github/license/claranet/ansible-role-satisfactory?style=flat-square)](LICENSE)
[![Release](https://img.shields.io/github/v/release/claranet/ansible-role-satisfactory?style=flat-square)](https://github.com/claranet/ansible-role-satisfactory/releases)
[![Status](https://img.shields.io/github/actions/workflow/status/claranet/ansible-role-satisfactory/molecule.yml?style=flat-square&label=tests)](https://github.com/claranet/ansible-role-satisfactory/actions?query=workflow%3A%22Ansible+Molecule%22)
[![Ansible version](https://img.shields.io/badge/ansible-%3E%3D2.10-black.svg?style=flat-square&logo=ansible)](https://github.com/ansible/ansible)
[![Ansible Galaxy](https://img.shields.io/badge/ansible-galaxy-black.svg?style=flat-square&logo=ansible)](https://galaxy.ansible.com/claranet/satisfactory)

> :star: Star us on GitHub — it motivates us a lot!

![](satisfactory_logo.png)

Install and configure Satisfactory dedicated server

## :warning: Requirements

Ansible >= 2.10

## :zap: Installation

```bash
ansible-galaxy install claranet.satisfactory
```

## :gear: Role variables

Variable                          | Default value                                                                                | Description
----------------------------------|----------------------------------------------------------------------------------------------|------------
satisfactory_user                 | steam                                                                                        | Server daemon users
satisfactory_user_home            | /home/`{{ satisfactory_user }}`                                                              | Daemon user's home
satisfactory_service_name         | satisfactory                                                                                 | SystemD service name (useful for multi instances)
satisfactory_install_dir          | `{{ satisfactory_user_home }}`/SatisfactoryDedicatedServer/`{{ satisfactory_service_name }}` | Installation directory
satisfactory_multihome            | _null_                                                                                       | Bind the server process to a specific IP address rather than all available interfaces
satisfactory_serverqueryport      | 15777                                                                                        | Override the Query Port the server uses. This is the port specified in the Server Manager in the client UI to establish a server connection. This can be set freely. The default port is UDP/15777
satisfactory_beaconport           | 15000                                                                                        | Override the Beacon Port the server uses This port currently cannot be set freely. The default port is UDP/15000. If this port is already in use, the server will step up to the next port until an available one is found
satisfactory_port                 | 7777                                                                                         | Override the Game Port the server uses. This is the primary port used to communicate game telemetry with the client. The default port is UDP/7777. If it is already in use, the server will step up to the next port until an available one is found
satisfactory_log                  | true                                                                                         | Forces the server to display logs in a window (on Windows) or in the active terminal (on Linux). This option is implicit by default when launching on Linux
satisfactory_maxplayers           | 16                                                                                           | Maximum players in game
satisfactory_autopause            | true                                                                                         | Pause the game when no one is connected
satisfactory_autosaveondisconnect | true                                                                                         | Save the session when the last player disconnects
satisfactory_experimental         | false                                                                                        | Use the experimental branch of the game server

## :arrows_counterclockwise: Dependencies

N/A

## :pencil2: Example Playbook

```yaml
---
- hosts: all
  roles:
    - role: claranet.satisfactory
      satisfactory_port: 8000

    # Create another instance on the same server
    - role: claranet.satisfactory
      satisfactory_service_name: satisfactory-test
      satisfactory_port: 8001
      satisfactory_serverqueryport: 15778
      satisfactory_beaconport: 15001

```

## :closed_lock_with_key: [Hardening](HARDENING.md)

## :heart_eyes_cat: [Contributing](CONTRIBUTING.md)

## :copyright: [License](LICENSE)

[Mozilla Public License Version 2.0](https://www.mozilla.org/en-US/MPL/2.0/)
