from djangominimizer import settings


def get_minimizer_list(file_list, timestamp):
    if not settings.MINIMIZER_DEBUG:
        file_min_list = []

        for file_orig in file_list:
            file_min = ('-%s' % timestamp).join(
                os.path.splitext(script))
            file_min_list.append(file_min)

        return file_min_list

    return file_list
