from slugify import slugify
from functools import partial

STUDENT_CONTENT_TYPE = 'students'
TEACHER_CONTENT_TYPE = 'teachers'


def is_correct_type(content_type, toc_item):
    visible = toc_item['visible']
    non_content_lesson_page = toc_item['lesson_page'] != '' and \
        toc_item['lesson_page_type'] != 'content'
    if toc_item['section'] in ('Research in Practice', 'Appendix'):
        # Adding this because of a mistake in moodle MBZ.
        # Alyssa wants Research in Practice and Course Design in TG.
        return True

    if ((visible == '0') and (content_type == STUDENT_CONTENT_TYPE)) or \
       ((visible == '1') and (content_type == TEACHER_CONTENT_TYPE)) or \
       non_content_lesson_page:
        return False
    return True


def filter_toc_by_type(toc_data, content_type):
    filtered_data = filter(
        partial(is_correct_type, content_type),
        toc_data
    )
    return list(filtered_data)


def select_title(toc_item):
    if toc_item['lesson_page'] != '':
        return toc_item['lesson_page']
    return toc_item['activity_name']


def generate_slug(toc_item):
    title = select_title(toc_item)
    section_slug = slugify(toc_item['section'], allow_unicode=True)
    title_slug = slugify(title, allow_unicode=True)
    return f"{section_slug}/{title_slug}"
