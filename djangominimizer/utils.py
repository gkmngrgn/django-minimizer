from djangominimizer import settings
from djangominimizer.models import Minimizer


def get_minimizer_list(file_list):
    if not settings.MINIMIZER_DEBUG:
        try:
            minimizer = Minimizer.objects.latest()
            file_min_list = []

            for file_orig in file_list:
                file_min = ('-%s' % minimizer.timestamp).join(
                    os.path.splitext(script))
                file_min_list.append(file_min)

            return file_min_list

        except Minimizer.DoesNotExist:
            pass

    return file_list
