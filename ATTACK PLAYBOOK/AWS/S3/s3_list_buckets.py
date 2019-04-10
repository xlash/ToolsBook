#!/usr/bin/env python

import subprocess
from datetime import datetime
import time
import argparse
import sys

# Take a list of buckets name in s3_open_list.txt and list them unauthenticated into out.txt
# FIXME doesn't support multiple AWS region
def main(ArgumentParser):
    w = open('args.file').read()
    stdOUT = open('671639806142_2019-04-10.txt', 'w+')
    for s3_info in w.splitlines():
        s3_name, s3_region = s3_info.split() if s3_info.find(' ') > -1 else (s3_info, 'us-east-1')
        print('#########%s START######### @ %s\n' % (s3_name, str(datetime.now())))
        stdOUT.write('#########%s START######### @ %s\n' % (s3_name, str(datetime.now())))
        stdOUT.flush()
        subprocess.run(['aws', 's3', 'ls', 's3://%s' % s3_name, '--no-sign-request', '--region', 'us-east-1', '--recursive'], stdout=stdOUT, stderr=stdOUT)
        stdOUT.flush()
        stdOUT.write('#########%s END######### @ %s\n' % (s3_name, str(datetime.now())))
        stdOUT.flush()
        print('#########%s END######### @ %s\n' % (s3_name, str(datetime.now())))
        # Allow possibility to break and wait
        time.sleep(2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-h', "help", help="echo the string you use here", action="store_true")
    parser.add_argument("file", help="file list of S3 buckets name with region name. (<S3 BUCKET_NAME> <AWS_REGION_NAME>",
                        type=str)
    parser.add_argument("stdout", help="file name for output",
                        type=str, default=sys.STDOUT)
    args = parser.parse_args()
    main(args)
