#!/usr/bin/env python
from __future__ import unicode_literals
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser(description="domains updater from felixonmars")
    parser.add_argument(
        '-a', '--add',
        metavar="DOMAIN",
        nargs="+",
        help='Add one or more new domain(s) (implies -s)',
    )
    parser.add_argument(
        '-d', '--delete',
        metavar="DOMAIN",
        nargs="+",
        help='Remove one or more old domain(s) (implies -s)',
    )
    parser.add_argument(
        '-s', '--sort',
        action='store_true',
        default=True,
        help='Sort the list (default action)',
    )
    parser.add_argument(
        '-f', '--file',
        nargs=1,
        default=["domains.txt"],
        help="Specify the file to update (domains.txt by default)",
    )

    options = parser.parse_args()

    with open(options.file[0]) as f:
        lines = list(f)

    if options.add:
        options.sort = True

        for domain in options.add:
            new_line = "%s\n" % domain
            if new_line in lines:
                print("Domain already exists: " + domain)
            else:
                print("New domain added: " + domain)
                lines.append(new_line)

    if options.delete:
        options.sort = True

        for domain in options.delete:
            target_line = "%s\n" % domain
            if target_line not in lines:
                print("Failed to remove domain " + domain + ": not found.")
            else:
                print("Domain removed: " + domain)
                lines.remove(target_line)

    if options.sort:
        lines.sort(key=lambda x: x.lstrip("#"))

    with open(options.file[0], "w") as f:
        f.write(''.join(filter(lambda line: line.strip(), lines)))
