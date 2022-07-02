from email import message
import http.server

from http.server import *

host = "localhost"
port = 80

class Handler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200);
		
		self.send_header("Content-type", "text/plain")
		self.end_headers()
		
		self.wfile.write(f"Server running on http://{host}:{port}".encode("utf8"))
  
		print(self.headers)
  

if __name__ == "__main__":
	server = HTTPServer((host, port), Handler)
	
	print(f"Started on http://{host}:{port}")
	 
	try:
		server.serve_forever()
	except:
		pass

	server.server_close()
 
	print("Stopped")