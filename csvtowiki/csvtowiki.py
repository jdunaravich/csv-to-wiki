import argparse
import csv
import codecs


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
    """== Schedule ==
    {| border="1" style="border-collapse:collapse;" cellpadding="2" width="100%"
    |- style="color:#FFFFFF; background-color:#5B9BD5; text-align:center; vertical-align:center; font-weight:bold; font-size:12pt;"
    |style=""|Deliverable
    |style=""|Start Date
    |style=""|End Date
    |style=""|Owner
    |style=""|Status
    |style=""|SIM
    |- style="background-color:#FFFFFF; vertical-align:center;"
    |style="text-align:center;"|FooBar
    |style="text-align:center;"|FooBar
    |style="text-align:center;"|FooBar
    |style="text-align:center;"|FooBar
    |style="text-align:center;"|FooBar
    |style="text-align:center;"|FooBar
    |}
    """
    row_strings = []
    for row in rows:
        row_strings.append("""|- style="background-color:#FFFFFF; vertical-align:center;"\n""")
        for header in headers:
            row_strings.append("""|style="text-align:center;"|{cell}\n""".format(cell=row[header]))
    row_string = "".join(row_strings)
    boilerplate = ("""{| border="1" style="border-collapse:collapse;" cellpadding="2" width="100%"\n"""
                   """|- style="color:#FFFFFF; background-color:#5B9BD5; text-align:center; vertical-align:center; font-weight:bold; font-size:12pt;"\n""")
    end = "|}"
    header_string = "".join(["""|style="width:16.66%%;"|%s\n""" % header for header in headers])
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
