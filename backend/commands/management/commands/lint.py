import signal
import subprocess

from django.core.management.base import BaseCommand, CommandError, CommandParser


class Command(BaseCommand):
    requires_system_checks = []
    help = 'Run ruff against the application to check for syntax and style errors.'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('--no-fix', action='store_true', default=False)

    def handle(self, *args, **options):
        ruff_args = ['ruff', 'backend']
        if not options['no_fix']:
            ruff_args += ['--fix']

        self.subprocess(ruff_args)

    def subprocess(self, args, acceptable_codes=(0,), raise_on_code=True, **kwargs):
        self.stdout.write(f'$> {" ".join(args)}')
        output = []
        try:
            p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, **kwargs)
            for line in iter(p.stdout.readline, b''):
                line_str = line.decode('utf-8')
                self.stdout.write(line_str)
                output.append(line_str)

            p.stdout.close()
            p.wait()
        except KeyboardInterrupt:
            p.send_signal(signal.SIGINT)
            p.wait()
        if p.returncode not in acceptable_codes and raise_on_code:
            codes = ', '.join([str(x) for x in acceptable_codes])
            raise CommandError(f'{args[0]} returned a code that was not in acceptable range [{codes}]')
        return p.returncode, output
