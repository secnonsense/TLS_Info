import ssl, socket

file=open("500.txt","r")
output=open("output.txt", "w")
hosts = file.readlines() 
for host in hosts:
  try:
    hostname=host.strip()
    ctx = ssl.create_default_context()
    with ctx.wrap_socket(socket.socket(), server_hostname=hostname) as s:
        s.settimeout(4)
        s.connect((hostname, 443))
        cert = s.getpeercert()

    #subject = dict(x[0] for x in cert['subject'])
    #issued_to = subject['commonName']
    issuer = dict(x[0] for x in cert['issuer'])
    issued_by = issuer['commonName']
    output.write("Site: " + hostname + " - issuer: " + issuer['organizationName'] + "\n")
    print("Site: " + hostname + " - issuer: " + issuer['organizationName'])
  except:
    continue
output.close()
file.close()
