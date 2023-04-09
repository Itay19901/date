import socket

def replace_placeholders():
    with open("day of week.txt", "r") as f:
        content = f.read()
        content = content.replace("[DAY_OF_WEEK]", "Sunday")
        content = content.replace("[CURRENT_DATE]", "01.01.2022")
    return content.encode()

def serve_file():
    host = ""
    port = 8080
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    while True:
        conn, addr = s.accept()
        print("Connected by", addr)
        data = conn.recv(1024)
        if not data:
            break
        response = b"HTTP/1.1 200 OK\r\n"
        response += b"Content-Type: text/plain\r\n"
        response += b"Content-Length: " + str(len(replace_placeholders())).encode() + b"\r\n"
        response += b"\r\n"
        response += replace_placeholders()
        conn.sendall(response)
        conn.close()
