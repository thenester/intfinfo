#! /usr/bin/env python3
#
# MIT License
#
# Copyright (c) 2024 Denys Nesterenko
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Displays tabulated network interfaces information."""

from ipaddress import IPv4Network
from os import path
from typing import Optional
from typing_extensions import Annotated

import typer
import netifaces
from tabulate import tabulate

app = typer.Typer()


@app.command()
def main(
    interface_list: Annotated[Optional[list[str]],
                              typer.Option("--interface", "-i",
                                           help="Interface name")] = None
) -> None:
    """Displays tabulated network interfaces information."""
    interfaces = netifaces.interfaces()
    data = []

    for iface in interfaces:
        if interface_list and iface not in interface_list:
            continue

        interface_info = netifaces.ifaddresses(iface)

        mac_addr_str = None
        if interface_info.get(netifaces.AF_LINK) and \
                len(interface_info[netifaces.AF_LINK]) > 0:
            mac_addr_str = interface_info[netifaces.AF_LINK][0]["addr"]

        ipv4_addr_str = None
        if interface_info.get(netifaces.AF_INET) and \
                len(interface_info[netifaces.AF_INET]) > 0:
            ipv4_addr = interface_info[netifaces.AF_INET][0]["addr"]
            prefixlen = IPv4Network(
                f"0.0.0.0/{interface_info[netifaces.AF_INET][0]['netmask']}").prefixlen

            ipv4_addr_str = f"{ipv4_addr}/{prefixlen}"

        ipv6_addr_str = None
        if interface_info.get(netifaces.AF_INET6) and \
                len(interface_info[netifaces.AF_INET6]) > 0:
            ipv6_addr = \
                interface_info[netifaces.AF_INET6][0]["addr"].split("%")[0]
            prefixlen = \
                interface_info[netifaces.AF_INET6][0]["netmask"].split("/")[-1]

            ipv6_addr_str = f"{ipv6_addr}/{prefixlen}"

        status_str = None
        operstate_file_path = f"/sys/class/net/{iface}/operstate"
        if path.isfile(operstate_file_path):
            with open(operstate_file_path, "r", encoding="ascii") as operstate_file:
                status = operstate_file.readline().rstrip() == "up"
                status_str = "Up" if status else "Down"

        mtu_str = None
        mtu_file_path = f"/sys/class/net/{iface}/mtu"
        if path.isfile(mtu_file_path):
            with open(mtu_file_path, "r", encoding="ascii") as mtu_file_path:
                mtu_str = mtu_file_path.readline().rstrip()

        data.append([iface, status_str, mac_addr_str,
                     mtu_str, ipv4_addr_str, ipv6_addr_str])

    print(tabulate(
        data,
        headers=["Interface", "Status", "MAC", "MTU", "IPv4", "IPv6"],
        tablefmt="rounded_outline",
        missingval="N/A"))


if __name__ == "__main__":
    app()
