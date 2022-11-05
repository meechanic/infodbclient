#!/usr/bin/env python3

import os
import sys
import argparse
import yaml
from infodbclient.helpers import (IDBCHelper, eprint_exception, eprint)
from infodbclient.rest import ApiException
import infodbclient

yaml.Dumper.ignore_aliases = lambda *args : True
print_traceback = True
print_result = True


def parse_args(argv):
    self_name = os.path.basename(argv[0])
    parent_parser = argparse.ArgumentParser(prog=self_name,
                                            description="Client for information sources database")
    subparsers = parent_parser.add_subparsers(help="Endpoint groups")
    subparsers.required = True
    subparsers.dest = "group"
    subparser_linktags = subparsers.add_parser("linktags", help="Utilities for work with LinkTags")
    subparser_linktags.add_argument("--action", type=str, help="Possible actions: list | get")
    subparser_linktags.add_argument("--profile", type=str, help="Config profile")
    subparser_linktags.add_argument("--id", type=str, help="Entity ID")
    subparser_linktags.add_argument("--input-file", type=str, help="Input file")
    subparser_sourcetags = subparsers.add_parser("sourcetags", help="Utilities for work with SourceTags")
    subparser_sourcetags.add_argument("--action", type=str, help="Possible actions: list | get")
    subparser_sourcetags.add_argument("--profile", type=str, help="Config profile")
    subparser_sourcetags.add_argument("--id", type=str, help="Entity ID")
    subparser_sourcetags.add_argument("--input-file", type=str, help="Input file")
    subparser_links = subparsers.add_parser("links", help="Utilities for work with Links")
    subparser_links.add_argument("--action", type=str, help="Possible actions: list | get")
    subparser_links.add_argument("--profile", type=str, help="Config profile")
    subparser_links.add_argument("--id", type=str, help="Entity ID")
    subparser_links.add_argument("--input-file", type=str, help="Input file")
    subparser_sources = subparsers.add_parser("sources", help="Utilities for work with Sources")
    subparser_sources.add_argument("--action", type=str, help="Possible actions: list | get")
    subparser_sources.add_argument("--profile", type=str, help="Config profile")
    subparser_sources.add_argument("--id", type=str, help="Entity ID")
    subparser_sources.add_argument("--input-file", type=str, help="Input file")
    return parent_parser.parse_args(sys.argv[1:])


def main():
    args = parse_args(sys.argv)
    idbch = IDBCHelper(args)
    obj = None
    if args.group == "linktags":
        if args.action == "list" or args.action == None:
            try:
                api_instance = idbch.get_linktags_api_instance()
                res = api_instance.apilinktags_list()
                if res:
                    obj = [i.to_dict() for i in res]
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "get":
            try:
                id = int(args.id)
            except TypeError as e:
                eprint("Incorrect or missing ID")
                exit(1)
            else:
                try:
                    api_instance = idbch.get_linktags_api_instance()
                    obj = api_instance.apilinktags_create(id).to_dict()
                except ApiException as e:
                    eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "create":
            if not args.input_file:
                eprint("Missing input file")
                exit(1)
            else:
                try:
                    with open(args.input_file, "r") as f:
                        res_pre = yaml.safe_load(f)
                except (OSError, yaml.YAMLError) as e:
                    eprint_exception(e, print_traceback=print_traceback)
                    exit(1)
                linktag_keys = ["name", "type"]
                res = {correct_key: res_pre[correct_key] for correct_key in linktag_keys}
                data = infodbclient.LinkTag(**res)
                try:
                    api_instance = idbch.get_linktags_api_instance()
                    obj = api_instance.apilinktags_create(data).to_dict()
                except ApiException as e:
                    eprint_exception(e, print_traceback=print_traceback)
        else:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    elif args.group == "sourcetags":
        if args.action == "list" or args.action == None:
            try:
                api_instance = idbch.get_sourcetags_api_instance()
                res = api_instance.apisourcetags_list()
                if res:
                    obj = [i.to_dict() for i in res]
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "get":
            try:
                id = int(args.id)
            except TypeError as e:
                eprint("Incorrect or missing ID")
                exit(1)
            else:
                try:
                    api_instance = idbch.get_sourcetags_api_instance()
                    obj = api_instance.apisourcetags_read(id).to_dict()
                except ApiException as e:
                    eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "create":
            if not args.input_file:
                eprint("Missing input file")
                exit(1)
            else:
                try:
                    with open(args.input_file, "r") as f:
                        res_pre = yaml.safe_load(f)
                except (OSError, yaml.YAMLError) as e:
                    eprint_exception(e, print_traceback=print_traceback)
                    exit(1)
                sourcetag_keys = ["name", "type"]
                res = {correct_key: res_pre[correct_key] for correct_key in sourcetag_keys}
                data = infodbclient.SourceTag(**res)
                try:
                    api_instance = idbch.get_sourcetags_api_instance()
                    obj = api_instance.apisourcetags_create(data).to_dict()
                except ApiException as e:
                    eprint_exception(e, print_traceback=print_traceback)
        else:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    elif args.group == "links":
        if args.action == "list" or args.action == None:
            try:
                api_instance = idbch.get_links_api_instance()
                res = api_instance.apilinks_list()
                if res:
                    obj = [i.to_dict() for i in res]
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "get":
            try:
                id = int(args.id)
            except TypeError as e:
                eprint("Incorrect or missing ID")
                exit(1)
            else:
                try:
                    api_instance = idbch.get_links_api_instance()
                    obj = api_instance.apilinks_read(id).to_dict()
                except ApiException as e:
                    eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "create":
            if not args.input_file:
                eprint("Missing input file")
                exit(1)
            else:
                try:
                    with open(args.input_file, "r") as f:
                        res_pre = yaml.safe_load(f)
                except (OSError, yaml.YAMLError) as e:
                    eprint_exception(e, print_traceback=print_traceback)
                    exit(1)
                link_keys = ["base", "comment", "edition", "id", "path", "publisher", "publishing_time", "scheme", "tag", "text"]
                res = {correct_key: res_pre[correct_key] for correct_key in link_keys}
                data = infodbclient.Link(**res)
                try:
                    api_instance = idbch.get_links_api_instance()
                    obj = api_instance.apilinks_create(data).to_dict()
                except ApiException as e:
                    eprint_exception(e, print_traceback=print_traceback)
        else:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    elif args.group == "sources":
        if args.action == "list" or args.action == None:
            try:
                api_instance = idbch.get_sources_api_instance()
                res = api_instance.apisources_list()
                if res:
                    obj = [i.to_dict() for i in res]
            except ApiException as e:
                eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "get":
            try:
                id = int(args.id)
            except TypeError as e:
                eprint("Incorrect or missing ID")
                exit(1)
            else:
                try:
                    api_instance = idbch.get_sources_api_instance()
                    obj = api_instance.apisources_read(id).to_dict()
                except ApiException as e:
                    eprint_exception(e, print_traceback=print_traceback)
        elif args.action == "create":
            if not args.input_file:
                eprint("Missing input file")
                exit(1)
            else:
                try:
                    with open(args.input_file, "r") as f:
                        res_pre = yaml.safe_load(f)
                except (OSError, yaml.YAMLError) as e:
                    eprint_exception(e, print_traceback=print_traceback)
                    exit(1)
                source_keys = ["author_list", "clear_name", "comment", "id", "informal_name", "link", "name", "review", "tag"]
                res = {correct_key: res_pre[correct_key] for correct_key in source_keys}
                data = infodbclient.Source(**res)
                try:
                    api_instance = idbch.get_sources_api_instance()
                    obj = api_instance.apisources_create(data).to_dict()
                except ApiException as e:
                    eprint_exception(e, print_traceback=print_traceback)
        else:
            eprint("Not implemented for action: {}".format(args.action))
            exit(1)
    else:
        eprint("Not implemented for group: {}".format(args.group))
        exit(1)
    if print_result:
        yaml.dump(obj, sys.stdout, default_flow_style=False, allow_unicode=True)


if __name__ == "__main__":
    main()