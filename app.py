import argparse
import metadata


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parser.add_argument(
        '-V', '--version',
        action='version',
        version='{0} {1}'.format(metadata.project, metadata.version))
    parser_add = subparsers.add_parser('scrape', help='scrape ICSD')
    parser_add.add_argument('-A', '--all', action='store_true', help='scrape everything using ICSD Collection Code')
    parser_add.add_argument('--composition', help='scrape everything using ICSD Collection Code', default=None, type=str)
    parser_add.add_argument('--code', help='scape by ICSD Collection Code (e.g. 2000, 2000-2050)', default=None, type=str)
    parser_add.set_defaults(handler=command_add)

    parser_enumerate = subparsers.add_parser('enumerate', help='make list of all ICSD codes')

    parser_ls = subparsers.add_parser('ls', help='report already retrieved entries')
    parser_ls.add_argument('--code', help='ICSD Collection Code (e.g. 2000, 2000-2050)', default=None, type=str)