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
        minimizer = Minimizer.objects.create()
        cmd_template = 'java -jar %(yui)s -o %(script_min)s %(script)s'
        missing_files = 0

        for script in settings.SCRIPTS:
            script_path = os.path.join(settings.JS_PATH, script)

            if not os.path.exists(script_path):
                missing_files += 1
                print("Missing file, %s" % script)

                continue

            print("Compiling %s..." % script)
            script_min_path = '%s-%s.js' % (
                os.path.splitext(script_path)[0], minimizer.timestamp)

            cmd = cmd_template % {
                'yui': os.path.join(
                    settings.TOOLS_PATH, settings.YUI_COMPRESSOR),
                'script': script_path,
                'script_min': script_min_path
            }

            call(cmd.split())

        if missing_files:
            print("%s file(s) not compiled. Please check these files." % missing_files)
