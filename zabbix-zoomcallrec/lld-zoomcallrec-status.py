#!/usr/bin/python
import json
import re
import subprocess

if __name__ == "__main__":
    data = []
    output = subprocess.Popen(["/opt/callrec/bin/callrec_status", "-names"], stdout=subprocess.PIPE).communicate()[0]

    names = re.findall(r'^//.+/(.+)$', output, flags=re.MULTILINE)
    pattern = re.compile(r'^(\d+)\s+\[(.*)\]\s*\[[.*]{5}\]\s+\-\s+((.*\S)\s+\.{3}\s+.*\S|[^.]+)\s+\.+\s+\[\s*(\S*)\s*\]$', flags=re.MULTILINE)
    pattern_s = re.compile(r'[^A-Za-z0-9/._]', flags=re.MULTILINE)
    for name in names:
        output = subprocess.Popen(["/opt/callrec/bin/callrec_status", "-name "+name+" -state all -stateOption status -verbosity 5"], stdout=subprocess.PIPE).communicate()[0]
        states = pattern.findall(output)
        for state in states:
            data.append({"{#RMIBINDNAME}": name,
            "{#ID}": state[0],
            "{#MODULE}": state[1],
            "{#MODULEREQ}": "" if pattern_s.findall(state[1]) else state[1],
            "{#DESCRIPTION}": state[3] if state[3] else state[2]})
    print(json.dumps({"data": data}, indent=4))
