#!/usr/bin/env python3

import os
import sys
import argparse
import json
from infodbclient.helpers import (IDBCHelper, eprint_exception, eprint)
from infodbclient.rest import ApiException

print_traceback = True


def parse_args(argv):
    self_name = os.path.basename(argv[0])
    parent_parser = argparse.ArgumentParser(prog=self_name,
                                            description="Client for information sources database")
    subparsers = parent_parser.add_subparsers(help="Endpoint groups")
    subparsers.required = True
    subparsers.dest = "group"
    apilinktags_calendars = subparsers.add_parser("apilinktags", help="Utilities for work with ApiLinkTags")
    apilinktags_calendars.add_argument("--action", type=str, help="Actions: list")
    apilinktags_calendars.add_argument("--profile", type=str, help="Config profile")
    return parent_parser.parse_args(sys.argv[1:])


def main():
    args = parse_args(sys.argv)
    idbch = IDBCHelper(args)
    obj = None
    if args.group == "apilinktags":
        if args.action == "list" or args.action == None:
            try:
                res = idbch.apilinktags_list()
                if res:
                    obj = [i.to_dict() for i in res]
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        else:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    else:
        eprint("Not implemented for group: {}".format(args.group))
        exit(1)
    json.dump(obj, sys.stdout, indent=4, default=str, ensure_ascii=False)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()