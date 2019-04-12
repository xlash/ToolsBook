#!/usr/bin/env python

import subprocess
from datetime import datetime
import time
import argparse
import sys

'''# Take a list of buckets name in s3_open_list.txt and list them unauthenticated into out.txt
For example 
1209348712093 us-east-1
# FIXME doesn't support multiple AWS region

Further analysis
aws s3 sync s3://sbucket_name/REMOTE_REPOSITORY/ --no-sign-request ./LOCAL_REPOSITORY
'''
def main(args):
    if isinstance(args.outFile, str):
        stdOUT = open(args.outFile, 'w+')
    w = open(args.file).read()

    for s3_info in w.splitlines():
        s3_name, s3_region = s3_info.split() if s3_info.find(' ') > -1 else (s3_info, 'us-east-1')
        print('#########%s %s START######### @ %s\n' % (s3_name, s3_region, str(datetime.now())))
        stdOUT.write('#########%s %s START######### @ %s\n' % (s3_name, s3_region, str(datetime.now())))
        stdOUT.flush()
        subprocess.run(['aws', 's3', 'ls', 's3://%s' % s3_name, '--no-sign-request', '--region', s3_region, '--recursive'], stdout=stdOUT, stderr=stdOUT)
        stdOUT.flush()
        stdOUT.write('#########%s %s END######### @ %s\n' % (s3_name, s3_region, str(datetime.now())))
        stdOUT.flush()
        print('#########%s %s END######### @ %s\n' % (s3_name, s3_region, str(datetime.now())))
        # Allow possibility to break and wait
        time.sleep(2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="file list of S3 buckets name with region name. (<S3 BUCKET_NAME> <AWS_REGION_NAME>",
                        type=str, required=True)
    parser.add_argument("--stdout", help="file name for output",
                        dest='outFile', type=str)
    parser.set_defaults(outFile=sys.stdout)
    args = parser.parse_args()
    main(args)
