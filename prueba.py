import requests

# Rutas absolutas de los archivos de certificado y clave
cert_absolute_path = r'C:\Users\pablo\Desktop\UM\Ingenieria de Software\microservicios\docker\traefik\config\certs\microservicio-cert.pem'
key_absolute_path = r'C:\Users\pablo\Desktop\UM\Ingenieria de Software\microservicios\docker\traefik\config\certs\microservicio-key.pem'
ca_cert_path = r'C:\Users\pablo\AppData\Local\mkcert\rootCA.pem'

print(f"Cert path: {cert_absolute_path}")
print(f"Key path: {key_absolute_path}")

cert = (cert_absolute_path, key_absolute_path)

try:
    response = requests.get('https://microserviceclient.microservicio.localhost/api/v1/findById/1', cert=cert, verify=ca_cert_path)
    response.raise_for_status()
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Ocurrió un error: {e}")



