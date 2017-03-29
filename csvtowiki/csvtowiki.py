import argparse
import csv
import codecs

MAGIC_VALUES = {
    "GREEN": "#00B050",
    "COMPLETE": "#0070C0",
    "YELLOW": "#FFFF00",
    "RED": "#FF0000"
}


def get_args():
    parser = argparse.ArgumentParser(description='Turn a csv into a wiki table')
    parser.add_argument('-i','--input', help='Input File', required=True)
    args = vars(parser.parse_args())
    return args


def parse_input_csv(full_path):
    with codecs.open(full_path,
                     'rU',
                     encoding="utf-8-sig") as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(1024))
        csvfile.seek(0)
        reader = csv.DictReader(csvfile, dialect=dialect)
        headers = reader.fieldnames
        rows = list(reader)
    return headers, rows


def construct_wiki_table(headers, rows):
    row_strings = []
    for row in rows:
        row_strings.append("""|- style="background-color:#FFFFFF; vertical-align:center;"\n""")
        for header in headers:
            cell = row[header]
            extra_style = ""
            if cell in MAGIC_VALUES:
                extra_style = "background-color:{magic}; ".format(magic=MAGIC_VALUES[cell])
            row_strings.append("""|style="{extra_style}text-align:center;"|{cell}\n""".format(cell=cell, extra_style=extra_style))
    row_string = "".join(row_strings)
    boilerplate = ("""{| border="1" style="border-collapse:collapse;" cellpadding="2" width="100%"\n"""
                   """|- style="color:#FFFFFF; background-color:#5B9BD5; text-align:center; vertical-align:center; font-weight:bold; font-size:12pt;"\n""")
    end = "|}"
    width = "{:0.2f}".format(100.0 / len(headers))
    header_string = "".join(["""|style="width:{width}%%;"|{header}\n""".format(width=width, header=header) for header in headers])
    table = """{boilerplate}{header_string}{row_string}{end}""".format(**locals())
    return table

def main():
    args = get_args()
    headers, rows = parse_input_csv(full_path=args['input'])
    wiki_table = construct_wiki_table(headers=headers,
                                      rows=rows)
    print wiki_table


if __name__ == '__main__':
    main()
