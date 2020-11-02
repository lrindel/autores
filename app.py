import http.server
import json
import urllib.request
import re

autores = [
	{
		"autorid":0,
		"nombre":"pato"
	},
	{
		"autorid":1,
		"nombre":"tero"
	},
	{
		"autorid":2,
		"nombre":"loco"
	}
]

class AutoresHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
	def do_GET(self): 
		response = ""
		
		print(self.path)
		
		if (self.path == "/autores/"):
			response = json.dumps(autores, indent=2)
			
		else:
			m = re.search("/autor/([0-9]+)/", self.path)
			if (m):
				print(m.group(1))
				autor = [l for l in autores if l["autorid"] == int(m.group(1))][0]
				response = json.dumps(autor, indent=2)
			
		self.wfile.write(b"HTTP/1.1 200 OK\n")
		self.wfile.write(b"\n")
		self.wfile.write(response.encode())

httpd = http.server.HTTPServer(("",8081), AutoresHTTPRequestHandler)
httpd.serve_forever()