import ssl, socket, argparse

parser = argparse.ArgumentParser()

parser.add_argument("-n", "--name", help="Display Common Name of Certificate", action="store_true")
parser.add_argument("-x", "--selected_cipher", help="Display the negotiated cipher", action="store_true")
parser.add_argument("-s", "--subject", help="Display the Certificate subject information", action="store_true")
parser.add_argument("-c", "--ciphers", help="Display ciphers offered by server", action="store_true")
parser.add_argument("-i", "--issuer", help="Diplay Certificate Issuer", action="store_true")
parser.add_argument("-f", "--file", help="Specify input file with a list of hostnames to be checked", action="store")
parser.add_argument("-o", "--out", help="Specify output file", action="store")
parser.add_argument("-d", "--domain", help="Specify domain name of host to be checked", action="store")

args = parser.parse_args()

if (not args.domain and not args.file) or (args.domain and args.file):
        print("\nEither a single site's domain or a file containing sites must be used as input\n")
        parser.print_help()
        quit()

if args.out:
  output=open(args.out, "w")

def process_ssl(host):  
    hostname=host.strip()
    context = ssl.create_default_context()
    with context.wrap_socket(socket.socket(), server_hostname=hostname) as sock:
        sock.settimeout(4)
        sock.connect((hostname, 443))
        ciphers = sock.shared_ciphers()
        selected_cipher = sock.cipher()
        cert = sock.getpeercert()

    subject = dict(x[0] for x in cert['subject'])
    issued_to = subject['commonName']
    issuer = dict(x[0] for x in cert['issuer'])
    issued_by = issuer['commonName']

    print(f"Site: {hostname}")
    if args.out:
      output.write("Site: " + hostname)
    if args.issuer:
      print(f"Issuer:  {issuer['organizationName']}")
      if args.out:
        output.write("\nIssuer: " + issuer['organizationName'])
    if args.subject:
      print(f"Subject: {subject}")
      if args.out:
        output.write("\nSubject: " + subject)
    if args.name:
      print(f"Certificate Common Name: {issued_to}")
      if args.out:
        output.write("\nCertificate Common Name: " + issued_to)
    if args.selected_cipher:
      print(f"Selected cipher: {selected_cipher}")
      if args.out:
        output.write("\nSelected cipher: " + str(selected_cipher))
    if args.ciphers:
      print(f"\nCiphers offered by server {ciphers}")
      if args.out:
        output.write("\nCiphers offered by server " + str(ciphers))
    print("\n")
    if args.out:
      output.write("\n\n")


def main():
  if args.file:
    file=open(args.file,"r")
    hosts = file.readlines() 
    for host in hosts:
      try:
        process_ssl(host)
      except:
        continue
  elif args.domain:
    process_ssl(args.domain)
  else:
    print("No input detected")
  if args.out:
    output.close()
  if args.file:
    file.close()

if __name__ == "__main__":
    main()
