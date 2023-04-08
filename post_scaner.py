import socket

links = ["facebook.com", "google.com"]  # Add website links here
scan_ports = [21,
22,
23,
25,
53,
80,
110,
135,
139,
143,
161,
389,
443,
445,
3389]


open_ports = []

total_scans = len(links) * len(scan_ports)
current_scan = 0

for link in links:
    for port in scan_ports:
        current_scan += 1
        progress = int((current_scan / total_scans) * 100)
        print(f"Scanning port {port} on {link}... {progress}% complete", end='\r')
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((link, port))
            if result == 0:
                print(f"Port {port} is open on {link}")
                open_ports.append((link, port))
            sock.close()
        except socket.error:
            pass

if len(open_ports) > 0:
    with open("hack.txt", "a") as f:
        f.write("Open ports:\n")
        for website, port in open_ports:
            f.write(f"{website}:{port}\n")
