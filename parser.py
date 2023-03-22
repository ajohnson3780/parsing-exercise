import re

#List of logs for general parser
logFiles = ["Kerberos_log.txt", "firewall_log.txt"]

#general parser
#open files and read logs as strings
for file in logFiles:
    with open(file, 'r') as openfile:
        log = openfile.read()
       
        #regex to find port numbers based on how they're identified in each log, as a number (between 1 and 5 digits) following certain words
        #this mostly works because the data is clean, this could possibly match patterns in other fields
        ports = re.findall("([Pp]ort\D{1,2}|service\D{2})(\d{1,5})", log)
       
       
        print(file + " logged port(s):")
        for tuplefound in ports:
            print(tuplefound[1])
        #print(file + " ports found: " + ports)
        
#above solution (general parser) works for this set but isn't ideal because cleaned logs is a large assumption
#below solution (specific parser) is a bit much for the request to just pull ports, but is more specific for a certain format

with open("ssh_log.txt", 'r') as openfile:
    log = openfile.read()
    
    #This ensures the entire line matches the format, and also pulls more fields besides the port number
    #It also assumes ssh log is either a Accepted or Failed password
    fields = re.findall("^<(\d+)>(\S+\s+\d+\s+\d+:\d+:\d+) (\w+) (\w+)\[(\d+)\]: (\w+).*user (\w+) from (\d+\.\d+\.\d+\.\d+) port (\d+) ssh2$", log)
    print("ssh logged port(s):")
    print(fields[0][8])