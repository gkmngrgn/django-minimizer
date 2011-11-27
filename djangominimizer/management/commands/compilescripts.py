import os
from subprocess import call
from django.core.management.base import BaseCommand
from djangominimizer import settings
from djangominimizer.models import Minimizer


class Command(BaseCommand):
    help = "Compiles javascript files that you have specified in settings.py."
    requires_model_validation = True

    def handle(self, **options):
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
                os.path.splitext(script_path)[0], minimizer.script_name)

            cmd = cmd_template % {
                'yui': os.path.join(
                    settings.TOOLS_PATH, settings.YUI_COMPRESSOR),
                'script': script_path,
                'script_min': script_min_path
            }

            call(cmd.split())

        if missing_files:
            print("%s file(s) not compiled. Please try to run "
                  "`collectstatic` before `compilescripts`." % missing_files)
