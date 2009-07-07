#!/usr/bin/env python

import os
import optparse
import sys
import re

# script made by result of web pages reading on pgsql optimization
# http://www.varlena.com/GeneralBits/Tidbits/perf.html
def sexec(cmd):
    return os.popen(cmd).read()[:-1]

def main():
    parser = optparse.OptionParser("usage: %prog --help for usage")
    parser.add_option("-i", dest="input",
                      default="", type="string",
                      help="original Postgresql.conf")
    parser.add_option("-m", dest="max_connections",
                      default="100", type="string",
                      help="max connection on the postgres")

    parser.add_option("-o", dest="output",
                      default="", type="string",
                      help="ouput Postgresql.conf")
    (options, args) = parser.parse_args()
    pgconf = options.input
    output = options.output
    if not os.path.exists(pgconf):
        print "Please provide a valid postgresql.conf"
        sys.exit(-1)
    
    # KERNEL OPTIMIZATION
    TotalKbytes=int(sexec("awk '/MemTotal:/ { print $2 }' /proc/meminfo"))
    TotalBytes=TotalKbytes * 1024
    PageSize=int(sexec('getconf PAGE_SIZE'))
    ShmallValue=TotalBytes/PageSize
    kv = {
        'kernel.shmall': ShmallValue,
        'kernel.shmmax': TotalBytes,
    }
    print "Setting KERNEL SYSCTL"
    for value in kv:
        print "%s: %s" % (value, kv[value])
        print sexec('sysctl -w %s=%s' %(value, kv[value]))
    
    # POSTGRESQL OPTIMIZATION
    print "Postgresql Configuration:"
    #shared_buffers=TotalBytes/8196
    pgvals = {
        'shared_buffers': TotalBytes*25/100,
        'cache_size': TotalBytes*25/100,
        'effective_cache_size': TotalKbytes*70/100,
        'sort_memory': TotalKbytes*3/100,
        'sort_size': TotalBytes*3/100,
        'work_mem':

        'fsync': 'on',

        'random_page_cost': 2,
        'wal_buffers': 64,
        
        'vacuum_mem': '32MB',
        'maintenance_work_mem': '256MB',
    }
    # half of ree mem +cached
    #stmt = sexec("free 2>&1|grep Mem |awk '{print $3 \"+\" $7}'")
    #exec "mem=%s" % stmt
    #pgvals['effectivee_cache_size']=mem*50/100
    if os.path.exists(pgconf):
        lines = open(pgconf).readlines()
        additional = []
        for v in pgvals:
            conf = '%s=%s\n' % (v, pgvals[v])
            found=False
            for i, l in enumerate(lines[:]):
                if re.match('^(#?)%s.*' % v, l, re.U):
                    found = True
                    lines[i] = conf
            if not found:
                additional.append(conf)
        if additional:
            lines.append('\n#\n# Added by pypgoptimizator\n#\n')
            lines.extend(additional)
        print "Patching postgresql.conf"
        open(options.output, 'w').writelines(lines)

if __name__ == '__main__':
    main()


