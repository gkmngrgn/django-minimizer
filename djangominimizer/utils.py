import os
from djangominimizer import settings

def get_minimizer_list(file_list, timestamp, ext):
    if not settings.MINIMIZER_DEBUG:
        file_min_list = []

        for file_orig in file_list:
            filename = os.path.splitext(file_orig)[0]
            file_min = '%s-%s.%s' % (filename, timestamp, ext)
            file_min_list.append(file_min)

        return file_min_list

    return file_list
