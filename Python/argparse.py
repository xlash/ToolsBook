import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="file list of S3 buckets name with region name. (<S3 BUCKET_NAME> <AWS_REGION_NAME>",
                        type=str)
    parser.add_argument("stdout", help="file name for output",
                        type=str, default=sys.stdout)
    args = parser.parse_args()
    main(args)
