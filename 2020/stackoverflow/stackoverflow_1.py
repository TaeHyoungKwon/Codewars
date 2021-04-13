import argparse


def main():
    parser = argparse.ArgumentParser("test", description="subparser help test")
    commands = parser.add_subparsers(dest="command", title="Commands")

    subparser_a = commands.add_parser("parser_a", help="description_of_parser_a")
    subparser_a.add_argument("--foo")
    subparser_a.add_argument("--bar")

    subparser_b = commands.add_parser("parser_b", help="description_of_parser_b")
    subparser_b.add_argument("--foo-b")
    subparser_b.add_argument("--bar-b")

    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()