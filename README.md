# TLS_Info

Simple script cobbled together from stack overflow answer that pulls domains from a file and retrieves their SSL certificate from the website and prints out the site name and issuer as well as saves them to a specified file.  


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
