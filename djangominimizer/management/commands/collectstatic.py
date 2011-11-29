import os
from subprocess import call
from django.contrib.staticfiles.management.commands.collectstatic \
    import Command as CollectStaticCommand
from djangominimizer import settings
from djangominimizer.models import Minimizer


# FIXME: Is it true way to override command?
class Command(CollectStaticCommand):
    def handle_noargs(self, **options):
        super(Command, self).handle_noargs(**options)

        print("\n\nNow, this will compress javascript and css files.")
        self.missing_files = 0
        self.minimizer = Minimizer.objects.create()
        self.cmd_template = 'java -jar %(yui)s -o %(file_min)s %(file)s'

        # compress script files.
        self.run_yui(settings.SCRIPTS, settings.JS_PATH)

        # then, comress style files.
        self.run_yui(settings.STYLES, settings.CSS_PATH)

        if self.missing_files:
            print("%s file(s) not compiled. Please check these files." % \
                  self.missing_files)

    def run_yui(self, file_list, static_path):
        for static_file in file_list:
            file_path = os.path.join(static_path, static_file)

            if not os.path.exists(file_path):
                self.missing_files += 1
                print("Missing file, %s" % static_file)

                continue

            print("Compressing %s..." % static_file)
            file_min_path = '%s-%s.js' % (
                os.path.splitext(file_path)[0], self.minimizer.timestamp)

            cmd = self.cmd_template % {
                'yui': os.path.join(
                    settings.TOOLS_PATH, settings.YUI_COMPRESSOR),
                'file': file_path,
                'file_min': file_min_path
            }

            call(cmd.split())
