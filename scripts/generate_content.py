"""Given a course ToC CSV file, this script will populate content files for
either teachers or students
"""
import argparse
from pathlib import Path
from csv import DictReader
from string import Template
import utils


CONTENT_TEMPLATE = Template("""---
title: "$title"
slug: "$slug"
---
""")


def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument(
        'csv_path',
        type=str,
        help='relative path to the ToC CSV file'
    )
    parser.add_argument(
        'content_type',
        type=str,
        choices=[utils.STUDENT_CONTENT_TYPE, utils.TEACHER_CONTENT_TYPE],
        help='Type of content to generate'
    )
    parser.add_argument(
        'output_path',
        type=str,
        help='Path to generate files'
    )
    args = parser.parse_args()

    csv_path = Path(args.csv_path).resolve(strict=True)
    output_path = Path(args.output_path).resolve(strict=True)
    content_type = args.content_type

    with open(csv_path) as csv_file:
        toc_data = list(DictReader(csv_file))

    filtered_data = utils.filter_toc_by_type(toc_data, content_type)

    for item in filtered_data:
        filename = f"{item['content_id']}.html"
        title = utils.select_title(item)
        slug = utils.generate_slug(item)
        filedata = CONTENT_TEMPLATE.substitute(
            title=title,
            slug=slug
        )

        with open(output_path / filename, 'w') as outputfile:
            outputfile.write(filedata)


if __name__ == "__main__":
    main()
