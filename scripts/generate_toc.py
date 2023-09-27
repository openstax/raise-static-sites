"""Given a course ToC CSV file, this script will create a JSON data file for
either teachers or students
"""
import argparse
from pathlib import Path
from csv import DictReader
import utils
import json


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
        help='Path to generate file'
    )
    args = parser.parse_args()

    csv_path = Path(args.csv_path).resolve(strict=True)
    output_path = Path(args.output_path)
    content_type = args.content_type

    with open(csv_path) as csv_file:
        toc_data = list(DictReader(csv_file))

    filtered_data = utils.filter_toc_by_type(toc_data, content_type)

    toc_tree = []

    for item in filtered_data:
        title = utils.select_title(item)
        slug = utils.generate_slug(item)
        section = item["section"]

        is_new_section = toc_tree[-1]['title'] != section if toc_tree else True
        if is_new_section:
            # Add a level 1 entry
            toc_tree.append({
                'title': section,
                'items': []
            })

        if item['lesson_page'] == '':
            # Insert level 2 entry for page activity to current section
            toc_tree[-1]['items'].append({
                'title': title,
                'slug': slug
            })
            # Done processing this item, go to the next one
            continue

        # We are in a lesson and need to insert a level 3 entry

        current_subsection_items = toc_tree[-1]['items']
        is_new_subsection = current_subsection_items[-1]['title'] != \
            item['activity_name'] if current_subsection_items else True
        if is_new_subsection:
            # Add a new level 2 entry for subsubsections
            toc_tree[-1]['items'].append({
                'title': item['activity_name'],
                'items': []
            })
        toc_tree[-1]['items'][-1]['items'].append({
            'title': title,
            'slug': slug
        })

    with open(output_path, 'w') as outputfile:
        json.dump(toc_tree, outputfile, indent=2)


if __name__ == "__main__":
    main()
