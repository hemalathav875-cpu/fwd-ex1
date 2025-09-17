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
httpd.serve_forever()