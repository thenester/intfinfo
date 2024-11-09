# intfinfo

[![GitHub Actions Build](https://github.com/thenester/intfinfo/actions/workflows/build.yml/badge.svg)](https://github.com/thenester/intfinfo/actions/workflows/build.yml)

Displays tabulated network interfaces information.

Usage:

```bash
Usage: intfinfo [OPTIONS]                                                                                          
                                                                                                                   
 Displays tabulated network interfaces information.                                                                
                                                                                                                   
╭─ Options ───────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --interface           -i      TEXT  Interface name [default: None]                                              │
│ --install-completion                Install completion for the current shell.                                   │
│ --show-completion                   Show completion for the current shell, to copy it or customize the          │
│                                     installation.                                                               │
│ --help                              Show this message and exit.                                                 │
╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
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
