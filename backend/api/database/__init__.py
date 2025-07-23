import ipaddress
import socket

def ip_validator() -> str | None:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_local = s.getsockname()[0]
        s.close
        
        ip = ipaddress.ip_address(ip_local)
        if isinstance(ip_local, ipaddress.IPv4Address):
            return "IPv4"
        elif isinstance(ip, ipaddress.IPv6Address):
            return "IPv6"
        
    except Exception:
        return "inválido"