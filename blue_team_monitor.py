import socket
import argparse
import sys

def check_ports(target, ports_to_check, timeout=0.5):
    open_ports = set()
    for port in ports_to_check:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.add(port)
        except socket.gaierror:
            print(f"Could not resolve hostname: {target}")
            sys.exit(1)
        except socket.error as e:
            print(f"Socket error on port {port}: {e}")
        finally:
            sock.close()
    return open_ports

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Local port monitor")
    parser.add_argument("--target", type=str, default="127.0.0.1", help="Target host to check")
    parser.add_argument("--expected", type=str, default="22,80,443", help="Comma-separated list of expected open ports")
    parser.add_argument("--range", type=str, default="1-1024", help="Port range to scan")
    parser.add_argument("--timeout", type=float, default=0.5, help="Timeout in seconds per port")
    args = parser.parse_args()

    try:
        expected_ports = {int(p.strip()) for p in args.expected.split(",")}
        start, end = map(int, args.range.split("-"))
        ports_to_check = range(start, end + 1)
    except ValueError:
        print("Invalid port range or expected ports format.")
        sys.exit(1)

    print(f"Scanning {args.target} for open ports ({start}-{end})...")
    found_ports = check_ports(args.target, ports_to_check, args.timeout)

    unexpected_ports = found_ports - expected_ports

    print(f"Expected open ports: {expected_ports}")
    print(f"Found open ports:    {found_ports}")

    if unexpected_ports:
        print(f"Unexpected open ports detected: {unexpected_ports}")
    else:
        print("No unexpected ports found.")
