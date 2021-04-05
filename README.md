# TLS_Info

Inspired by a stack overflow answer, this is a simple script that pulls domains from a file, retrieves the TLS certificate from the related website and then prints out the site name, cert issuer, expiration, and other TLS related information.  

Args:

"-n", "--name", "Display Common Name of Certificate"  
"-e", "--expiration", "Display Certificate Expiration"  
"-a", "--activation", "Display Certificate's activation date"  
"-x", "--selected_cipher", "Display the negotiated cipher"  
"-s", "--subject", "Display the Certificate subject information"  
"-c", "--ciphers", "Display ciphers offered by server"  
"-i", "--issuer", "Diplay Certificate Issuer"  
"-f", "--file", "Specify input file with a list of hostnames to be checked"  
"-o", "--out", "Specify output file"  
"-d", "--domain", "Specify domain name of host to be checked"  
