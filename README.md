Two Python scripts that demonstrate core network/security concepts:

`blue_team_monitor.py`: scans a host (default: `127.0.0.1`) across a port range, compares found open ports to an expected list, and flags unexpected ports.

`red_team_scanner.py`: a TCP port scanner that checks a short list of ports on a target and prints open/closed status.

Both scripts use Python's `socket` module and support command-line arguments and basic error handling.

Disclaimer: **Only scan systems you own or have explicit permission to test.** These tools are for learning and authorized testing only.

Requirements: Python 3.x 

**How to Run:**

`python3 blue_team_monitor.py --target 127.0.0.1 --expected 22,80,443 --range 1-1024 --timeout 0.5`

**Defaults:**

--target = 127.0.0.1

--expected = 22,80,443

--range = 1-1024

--timeout = 0.5


`python3 red_team_scanner.py --target scanme.nmap.org --ports 22,80,443 --timeout 1`

**Defaults:**

--target = scanme.nmap.org

--ports = 22,80,443

--timeout = 1.0
