import http.server
import socketserver
import socket




class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            # 尝试获取请求的文件
            f = self.send_head()
            if f:
                self.copyfile(f, self.wfile)
                f.close()
        except FileNotFoundError:
            # 如果文件不存在，返回404页面
            self.send_error(404, "File not found")
            error_page = open("404.html", "rb")
            self.copyfile(error_page, self.wfile)
            error_page.close()

PORT = 80

def get_local_ip():
    try:
        # 获取主机名
        host_name = socket.gethostname()
        # 获取本机IP地址
        ip_address = socket.gethostbyname(host_name)
        return ip_address
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    local_ip = get_local_ip()
    

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Serving at Port:{PORT}")
    print("Please visit http://", local_ip )
    print("Press Ctrl+C to quilt")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass

