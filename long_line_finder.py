'''
find lines that above a specified length.
outputs a CSV with details of the long files.

Created on 6 Nov 2012
@author: astaveley
'''

import os;
import csv;
    
def find_long_lines_in_files(rootdir, line_limit):
    total_violations = [];
    for path, dirs, files in os.walk(rootdir):
        for file in files:
            #print("22 path=%s, dir=%s, file=%s" % (path, dir, file));
            total_violations += (find_long_lines(path + "\\" + file, line_limit));
    print("Total number of lies over limit= %d " % len(total_violations)); 
    write_csv_file("lines_greater_than_" + str(line_limit) + ".csv", ('file', 'line_number', 'line_length', 'text'), total_violations);
    
def find_long_lines(filename, length): 
    with open(filename, 'r') as f:
        violations = [];
        for num, line in enumerate(f):
            if (len(line) > length):
                print("file=%s,line_number=%d,length=%d,line=%s" % (filename, num + 1, len(line), line.rstrip('\r\n')));
                violation = {"file": filename, "line_number": num+ 1, 
                             "line_length":len(line), "text":line.rstrip('\r\n')};
                violations.append(violation);
        return violations;    
    
def write_csv_file(filename, fields, rows):
    # remove entries rows that are not in fields
    new_rows =  [dict((k,v) for k,v in d.iteritems() if k in fields) for d in rows]
    with open(filename, 'wb') as f:
        writer = csv.DictWriter(f, fields)
        writer.writerow({f: f for f in fields})  # write a header row
        for entry in new_rows:
            writer.writerow(entry) 
            
if __name__ == '__main__':
    find_long_lines_in_files('C:\workspaces\DM8_dev1\dev1\src', 120);
    pass