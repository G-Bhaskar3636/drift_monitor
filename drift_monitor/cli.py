import argparse
import pandas as pd

from .monitor import monitor_data
from .report import print_report, generate_html_report


VERSION = "0.1.0"


def main():

    parser = argparse.ArgumentParser(
        prog="drift-monitor",
        description="ML data drift and data quality monitoring tool."
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {VERSION}"
    )

    subparsers = parser.add_subparsers(
        dest="command"
    )

    check_parser = subparsers.add_parser(
        "check",
        help="Run drift monitoring on two CSV files."
    )

    check_parser.add_argument(
        "--reference",
        required=True,
        help="Path to the reference CSV file."
    )

    check_parser.add_argument(
        "--current",
        required=True,
        help="Path to the current CSV file."
    )

    check_parser.add_argument(
        "--output",
        default=None,
        help="Optional path for the HTML report."
    )

    args = parser.parse_args()

    if args.command == "check":

        reference = pd.read_csv(args.reference)
        current = pd.read_csv(args.current)

        report = monitor_data(
            reference,
            current
        )

        print_report(report)

        if args.output:

            output_path = generate_html_report(
                report,
                args.output
            )

            print(
                f"\nHTML report saved to: {output_path}"
            )

    else:
        parser.print_help()


if __name__ == "__main__":
    main()