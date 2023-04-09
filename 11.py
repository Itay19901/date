import socket

# Define the placeholders and their corresponding values
replacements = {
    "[monday]": "monday",
    "[CURRENT_DATE]": "27/03/2023"
}

# Read the file contents and replace the placeholders with their values
with open("day of week", "r") as file:
    content = file.read()
    for placeholder, value in replacements.items():
        content = content.replace(placeholder, value)

# Create a TCP socket and listen on port 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", 8080))
sock.listen()

# Serve the file contents to any incoming connections
while True:
    conn, addr = sock.accept()
    conn.sendall(content.encode())
    conn.close