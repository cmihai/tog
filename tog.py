import sys
import click
from datetime import datetime


@click.command()
@click.option('--us', is_flag=True, help='Show time with microsecond precision.')
def cli(us):
    for line in sys.stdin:
        if us:
            format = '%Y-%m-%d %H:%M:%S.%f'
        else:
            format = '%Y-%m-%d %H:%M:%S'
        timestr = datetime.now().strftime(format)

        print('[{}] {}'.format(timestr, line.rstrip()))


if __name__ == '__main__':
    cli()