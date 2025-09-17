
## EX01 Developing a Simple Webserver
## Date:

## AIM:
To develop a simple webserver to serve html pages and display the list of protocols in TCP/IP Protocol Suite.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
~~~
from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>TCP Protocol Overview</title>
  <style>
    table {
      width: 80%;
      border-collapse: collapse;
      margin: 20px auto;
      font-family: Arial, sans-serif;
    }
    th, td {
      border: 1px solid #ccc;
      padding: 10px;
      text-align: left;
    }
    th {
      background-color: #f2f2f2;
    }
    caption {
      caption-side: top;
      font-weight: bold;
      margin-bottom: 10px;
      font-size: 1.2em;
    }
  </style>
</head>
<body>

<table>
  <caption>TCP Protocol Key Features</caption>
  <tr>
    <th>Feature</th>
    <th>Explanation</th>
  </tr>
  <tr>
    <td>Protocol</td>
    <td>Transmission Control Protocol (TCP) — a connection-oriented protocol in the Transport Layer of the OSI model.</td>
  </tr>
  <tr>
    <td>Connection Type</td>
    <td>Connection-oriented; requires a handshake (SYN, SYN-ACK, ACK) before data transfer.</td>
  </tr>
  <tr>
    <td>Reliability</td>
    <td>Ensures reliable delivery of packets by using acknowledgments and retransmissions if needed.</td>
  </tr>
  <tr>
    <td>Flow Control</td>
    <td>Uses sliding window mechanism to prevent sender from overwhelming the receiver.</td>
  </tr>
  <tr>
    <td>Error Checking</td>
    <td>Uses checksums to verify data integrity.</td>
  </tr>
  <tr>
    <td>Segmentation</td>
    <td>Data from the application layer is split into segments for transmission.</td>
  </tr>
  <tr>
    <td>Port Numbers</td>
    <td>Uses source and destination port numbers to identify applications.</td>
  </tr>
  <tr>
    <td>Use Cases</td>
    <td>Web browsing (HTTP/HTTPS), Email (SMTP/IMAP/POP3), File transfers (FTP), etc.</td>
  </tr>
</table>

</body>
</html>


"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>TCP Protocol Overview</title>
  <style>
    table {
      width: 80%;
      border-collapse: collapse;
      margin: 20px auto;
      font-family: Arial, sans-serif;
    }
    th, td {
      border: 1px solid #ccc;
      padding: 10px;
      text-align: left;
    }
    th {
      background-color: #f2f2f2;
    }
    caption {
      caption-side: top;
      font-weight: bold;
      margin-bottom: 10px;
      font-size: 1.2em;
    }
  </style>
</head>
<body>

<table>
  <caption>TCP Protocol Key Features</caption>
  <tr>
    <th>Feature</th>
    <th>Explanation</th>
  </tr>
  <tr>
    <td>Protocol</td>
    <td>Transmission Control Protocol (TCP) — a connection-oriented protocol in the Transport Layer of the OSI model.</td>
  </tr>
  <tr>
    <td>Connection Type</td>
    <td>Connection-oriented; requires a handshake (SYN, SYN-ACK, ACK) before data transfer.</td>
  </tr>
  <tr>
    <td>Reliability</td>
    <td>Ensures reliable delivery of packets by using acknowledgments and retransmissions if needed.</td>
  </tr>
  <tr>
    <td>Flow Control</td>
    <td>Uses sliding window mechanism to prevent sender from overwhelming the receiver.</td>
  </tr>
  <tr>
    <td>Error Checking</td>
    <td>Uses checksums to verify data integrity.</td>
  </tr>
  <tr>
    <td>Segmentation</td>
    <td>Data from the application layer is split into segments for transmission.</td>
  </tr>
  <tr>
    <td>Port Numbers</td>
    <td>Uses source and destination port numbers to identify applications.</td>
  </tr>
  <tr>
    <td>Use Cases</td>
    <td>Web browsing (HTTP/HTTPS), Email (SMTP/IMAP/POP3), File transfers (FTP), etc.</td>
  </tr>
</table>

</body>
</html>


"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>TCP Protocol Overview</title>
  <style>
    table {
      width: 80%;
      border-collapse: collapse;
      margin: 20px auto;
      font-family: Arial, sans-serif;
    }
    th, td {
      border: 1px solid #ccc;
      padding: 10px;
      text-align: left;
    }
    th {
      background-color: #f2f2f2;
    }
    caption {
      caption-side: top;
      font-weight: bold;
      margin-bottom: 10px;
      font-size: 1.2em;
    }
  </style>
</head>
<body>

<table>
  <caption>TCP Protocol Key Features</caption>
  <tr>
    <th>Feature</th>
    <th>Explanation</th>
  </tr>
  <tr>
    <td>Protocol</td>
    <td>Transmission Control Protocol (TCP) — a connection-oriented protocol in the Transport Layer of the OSI model.</td>
  </tr>
  <tr>
    <td>Connection Type</td>
    <td>Connection-oriented; requires a handshake (SYN, SYN-ACK, ACK) before data transfer.</td>
  </tr>
  <tr>
    <td>Reliability</td>
    <td>Ensures reliable delivery of packets by using acknowledgments and retransmissions if needed.</td>
  </tr>
  <tr>
    <td>Flow Control</td>
    <td>Uses sliding window mechanism to prevent sender from overwhelming the receiver.</td>
  </tr>
  <tr>
    <td>Error Checking</td>
    <td>Uses checksums to verify data integrity.</td>
  </tr>
  <tr>
    <td>Segmentation</td>
    <td>Data from the application layer is split into segments for transmission.</td>
  </tr>
  <tr>
    <td>Port Numbers</td>
    <td>Uses source and destination port numbers to identify applications.</td>
  </tr>
  <tr>
    <td>Use Cases</td>
    <td>Web browsing (HTTP/HTTPS), Email (SMTP/IMAP/POP3), File transfers (FTP), etc.</td>
  </tr>
</table>

</body>
</html>


"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>TCP Protocol Overview</title>
  <style>
    table {
      width: 80%;
      border-collapse: collapse;
      margin: 20px auto;
      font-family: Arial, sans-serif;
    }
    th, td {
      border: 1px solid #ccc;
      padding: 10px;
      text-align: left;
    }
    th {
      background-color: #f2f2f2;
    }
    caption {
      caption-side: top;
      font-weight: bold;
      margin-bottom: 10px;
      font-size: 1.2em;
    }
  </style>
</head>
<body>

<table>
  <caption>TCP Protocol Key Features</caption>
  <tr>
    <th>Feature</th>
    <th>Explanation</th>
  </tr>
  <tr>
    <td>Protocol</td>
    <td>Transmission Control Protocol (TCP) — a connection-oriented protocol in the Transport Layer of the OSI model.</td>
  </tr>
  <tr>
    <td>Connection Type</td>
    <td>Connection-oriented; requires a handshake (SYN, SYN-ACK, ACK) before data transfer.</td>
  </tr>
  <tr>
    <td>Reliability</td>
    <td>Ensures reliable delivery of packets by using acknowledgments and retransmissions if needed.</td>
  </tr>
  <tr>
    <td>Flow Control</td>
    <td>Uses sliding window mechanism to prevent sender from overwhelming the receiver.</td>
  </tr>
  <tr>
    <td>Error Checking</td>
    <td>Uses checksums to verify data integrity.</td>
  </tr>
  <tr>
    <td>Segmentation</td>
    <td>Data from the application layer is split into segments for transmission.</td>
  </tr>
  <tr>
    <td>Port Numbers</td>
    <td>Uses source and destination port numbers to identify applications.</td>
  </tr>
  <tr>
    <td>Use Cases</td>
    <td>Web browsing (HTTP/HTTPS), Email (SMTP/IMAP/POP3), File transfers (FTP), etc.</td>
  </tr>
</table>

</body>
</html>


"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>TCP Protocol Overview</title>
  <style>
    table {
      width: 80%;
      border-collapse: collapse;
      margin: 20px auto;
      font-family: Arial, sans-serif;
    }
    th, td {
      border: 1px solid #ccc;
      padding: 10px;
      text-align: left;
    }
    th {
      background-color: #f2f2f2;
    }
    caption {
      caption-side: top;
      font-weight: bold;
      margin-bottom: 10px;
      font-size: 1.2em;
    }
  </style>
</head>
<body>

<table>
  <caption>TCP Protocol Key Features</caption>
  <tr>
    <th>Feature</th>
    <th>Explanation</th>
  </tr>
  <tr>
    <td>Protocol</td>
    <td>Transmission Control Protocol (TCP) — a connection-oriented protocol in the Transport Layer of the OSI model.</td>
  </tr>
  <tr>
    <td>Connection Type</td>
    <td>Connection-oriented; requires a handshake (SYN, SYN-ACK, ACK) before data transfer.</td>
  </tr>
  <tr>
    <td>Reliability</td>
    <td>Ensures reliable delivery of packets by using acknowledgments and retransmissions if needed.</td>
  </tr>
  <tr>
    <td>Flow Control</td>
    <td>Uses sliding window mechanism to prevent sender from overwhelming the receiver.</td>
  </tr>
  <tr>
    <td>Error Checking</td>
    <td>Uses checksums to verify data integrity.</td>
  </tr>
  <tr>
    <td>Segmentation</td>
    <td>Data from the application layer is split into segments for transmission.</td>
  </tr>
  <tr>
    <td>Port Numbers</td>
    <td>Uses source and destination port numbers to identify applications.</td>
  </tr>
  <tr>
    <td>Use Cases</td>
    <td>Web browsing (HTTP/HTTPS), Email (SMTP/IMAP/POP3), File transfers (FTP), etc.</td>
  </tr>
</table>

</body>
</html>


"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
~~~


## OUTPUT:
![alt text](<Screenshot 2025-09-17 151716.png>)
![alt text](<Screenshot 2025-09-17 151852.png>)

## RESULT:
The program for implementing simple webserver is executed successfully.

