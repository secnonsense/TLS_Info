import ssl, socket

file=open("input.txt","r")
output=open("output.txt", "w")
hosts = file.readlines() 
for host in hosts:
  try:
    hostname=host.strip()
    context = ssl.create_default_context()
    with context.wrap_socket(socket.socket(), server_hostname=hostname) as sock:
        sock.settimeout(4)
        sock.connect((hostname, 443))
        cert = sock.getpeercert()

    #subject = dict(x[0] for x in cert['subject'])
    #issued_to = subject['commonName']
    issuer = dict(x[0] for x in cert['issuer'])
    issued_by = issuer['commonName']
    output.write("Site: " + hostname + " - issuer: " + issuer['organizationName'] + "\n")
    print("Site: " + hostname + " - Issuer: " + issuer['organizationName'])
  except:
    continue
output.close()
file.close()
