import socket
import argparse
import sys

def scan_ports(target, ports, timeout=1):
    print(f"Scanning {target}...")
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open.")
            else:
                print(f"Port {port} is closed.")
        except socket.gaierror:
            print(f"Could not resolve hostname: {target}")
            sys.exit(1)
        except socket.error as e:
            print(f"Socket error on port {port}: {e}")
        finally:
            sock.close()
    print("Scan complete.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple TCP port scanner")
    parser.add_argument("--target", type=str, default="scanme.nmap.org", help="Target host to scan")
    parser.add_argument("--ports", type=str, default="22,80,443", help="Comma-separated list of ports")
    parser.add_argument("--timeout", type=float, default=1, help="Timeout in seconds per port")
    args = parser.parse_args()

    try:
        ports = [int(p.strip()) for p in args.ports.split(",")]
    except ValueError:
        print("Ports must be integers separated by commas.")
        sys.exit(1)
    scan_ports(args.target, ports, args.timeout)
