# intfinfo

[![GitHub Actions Build](https://github.com/thenester/intfinfo/actions/workflows/build.yml/badge.svg)](https://github.com/thenester/intfinfo/actions/workflows/build.yml)

A sandbox for testing GitHub Actions and PyOxydizer for a small Python project implementing displaying the network interfaces information.

Usage:

```bash
Usage: intfinfo [OPTIONS]

  Displays tabulated network interfaces information.

Options:
  -i, --interface iface_name  Network interface name
  --help                      Show this message and exit.
```

Output example:

```bash
╭─────────────┬──────────┬───────────────────┬───────┬─────────────────┬─────────────────────────────╮
│ Interface   │ Status   │ MAC               │   MTU │ IPv4            │ IPv6                        │
├─────────────┼──────────┼───────────────────┼───────┼─────────────────┼─────────────────────────────┤
│ lo          │ Down     │ 00:00:00:00:00:00 │ 65536 │ 127.0.0.1/8     │ ::1/128                     │
│ eth0        │ Up       │ 00:15:5d:55:8a:0f │  1500 │ 172.29.52.39/20 │ fe80::215:5dff:fe55:8a0f/64 │
╰─────────────┴──────────┴───────────────────┴───────┴─────────────────┴─────────────────────────────╯
```

## PyOxidizer

As was found, PyOxidizer with existing the configuration gives no performance improvement.

```bash
~$ time uv run intfinfo && time ./build/x86_64-unknown-linux-gnu/debug/install/intfinfo/intfinfo
╭─────────────┬──────────┬───────────────────┬───────┬─────────────────┬─────────────────────────────╮
│ Interface   │ Status   │ MAC               │   MTU │ IPv4            │ IPv6                        │
├─────────────┼──────────┼───────────────────┼───────┼─────────────────┼─────────────────────────────┤
│ lo          │ Down     │ 00:00:00:00:00:00 │ 65536 │ 127.0.0.1/8     │ ::1/128                     │
│ eth0        │ Up       │ 00:15:5d:55:8a:0f │  1500 │ 172.29.52.39/20 │ fe80::215:5dff:fe55:8a0f/64 │
╰─────────────┴──────────┴───────────────────┴───────┴─────────────────┴─────────────────────────────╯
uv run intfinfo  0.04s user 0.02s system 102% cpu 0.057 total
╭─────────────┬──────────┬───────────────────┬───────┬─────────────────┬─────────────────────────────╮
│ Interface   │ Status   │ MAC               │   MTU │ IPv4            │ IPv6                        │
├─────────────┼──────────┼───────────────────┼───────┼─────────────────┼─────────────────────────────┤
│ lo          │ Down     │ 00:00:00:00:00:00 │ 65536 │ 127.0.0.1/8     │ ::1/128                     │
│ eth0        │ Up       │ 00:15:5d:55:8a:0f │  1500 │ 172.29.52.39/20 │ fe80::215:5dff:fe55:8a0f/64 │
╰─────────────┴──────────┴───────────────────┴───────┴─────────────────┴─────────────────────────────╯
./build/x86_64-unknown-linux-gnu/debug/install/intfinfo/intfinfo  0.05s user 0.01s system 99% cpu 0.057 total
```
