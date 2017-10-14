import click
@click.group()
@click.option('--removedigits/--no-removedigits', default=False)
@click.pass_context
def cli(ctx, removedigits):
    ctx.obj['DEBUG'] = removedigits
    print("value is",ctx.obj['DEBUG'])


@cli.command()
@click.pass_context
def lower(ctx,s):
    click.echo('haiii')
    if ctx.obj['DEBUG']==True:
        s=''.join([i for i in str if i.isdigit()==False])
        print('entered remove digits',s)
    else:

        print('not entered remove digits',str)

if __name__ == '__main__':
    cli(obj={})


========================================
import click

class Config(object):
    def __init__(self):
        self.verbose=False
pass_config=click.make_pass_decorator(Config,ensure=True)
@click.group()
@click.option('--verbose',is_flag=True)
@pass_config
def cli(config,verbose):
    config.verbose=verbose

@cli.command()
@click.option('--string',default='world',help='this is thing that is greeted')
@click.option('--repeat',default=1,help='how many times should be greted')
@click.argument('out',type=click.File('w'),default='-',required=False)
@pass_config
def say(config,string,repeat,out):
    """haii ihis script greets you"""
    if config.verbose:
        click.echo('we arte in verbse mode')
    for x in xrange(repeat):
        click.echo('Hello %s!'%string,file=out)
