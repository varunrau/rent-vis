import argparse
import csv

class ZillowParser:

    def __init__(self, infile):
        self.infile = infile

    def _get_headers(self):
        """Extract headers (first line of csv)"""
        reader = csv.reader(self.infile)
        for l in reader:
            headers = l
            break
        return headers

    def stream_data(self):
        """Streams rows of files in the csv as dictionaries"""
        headers = self._get_headers()
        reader = csv.reader(self.infile)
        for lineno, line in enumerate(reader):
            # skip headers
            if lineno == 0:
                continue
            row = {}
            for header_index in range(len(headers)):
                header = headers[header_index]
                val = line[header_index]
                row[header] = val
            yield row


def main():
    parser = argparse.ArgumentParser(description='Parses Zillow CSVs.')
    parser.add_argument('--file', metavar='file', type=argparse.FileType('r'),
                        help='the file to parse')
    parser.add_argument('--out', metavar='file',
                        help='[optional] print out result')
    args = parser.parse_args()

    parser = ZillowParser(args.file)
    stream = parser.stream_data()

    if args.out:
        for val in stream:
            print(val)

if __name__ == '__main__':
    main()
