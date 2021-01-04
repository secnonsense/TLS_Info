import ssl
import socket
import argparse


def parse_args():
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
  return args


def process_ssl(host,args,output):  
    hostname=host.strip()
    context = ssl.create_default_context()
    with context.wrap_socket(socket.socket(), server_hostname=hostname) as sock:
        sock.settimeout(4)
        sock.connect((hostname, 443))
        ciphers = sock.shared_ciphers()
        selected_cipher = sock.cipher()
        cert = sock.getpeercert()

    subject = dict(_[0] for _ in cert['subject'])
    issued_to = subject['commonName']
    issuer = dict(_[0] for _ in cert['issuer'])
    issued_by = issuer['commonName'] 

    print(f"Site: {hostname}")
    if args.out:
      output.write("Site: " + hostname)
    if args.issuer:
      print(f"Issuer:  {issuer['organizationName']}")
      print(f"Issued by: {issued_by}")
      if args.out:
        output.write("\nIssuer: " + issuer['organizationName'])
        output.write("\nIssued by: " + issued_by)
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
  args=parse_args()
  output=None
  if args.out:
    output=open(args.out, "w")
  if args.file:
    with open(args.file,"r") as file:
      hosts = file.readlines() 
      for host in hosts:
        try:
          process_ssl(host,args,output)
        except Exception: 
          continue
  elif args.domain:
    process_ssl(args.domain,args,output)
  else:
    print("No input detected")
  if args.out:
    output.close()

            
if __name__ == "__main__":
    main()
