import argparse
from pathlib import Path


class Config:
    def __init__(self):
        self.path = None
        self.output_path = None
        self.log_output = None
        parser = self._create_parser()
        self.parse_opts(parser)

    def _create_parser(self):
        defaults = {
            "path": self.path,
            "output_path": self.output_path
        }

        parser = argparse.ArgumentParser(
            prog="sherlock",
            description="Code complexity analyser for Robot Framework.\n"
        )

        parser.add_argument(
            "path",
            metavar="SOURCE",
            type=Path,
            help="Path to source code"
        )
        parser.add_argument(
            "--output-path",
            default=self.output_path,
            type=Path,
            help="Path to Robot Framework output file"
        )
        parser.add_argument(
            "--log-output",
            type=argparse.FileType("w"),
            default=self.log_output,
            help="Path to output log"
        )
        parser.set_defaults(**defaults)
        return parser

    def parse_opts(self, parser):
        args = parser.parse_args()
        for key, value in dict(**vars(args)).items():
            if key in self.__dict__:
                self.__dict__[key] = value
