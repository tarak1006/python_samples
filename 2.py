import click

class Config(object):
    def __init__(self):
        self.verbose=False
pass_config=click.make_pass_decorator(Config,ensure=True)
@click.group()
@click.option('--removedigits/--no-removedigits',default=False,help='remove digits from string')
@pass_config
def cli(config,removedigits):
    if removedigits:
        config.verbose=True
    else:
        config.verbose=False
@cli.command()
@click.option('-d',default=':',help='--delimiter TEXT defaults to :')
#@click.option('--repeat',default=1,help='how many times should be greted')
@click.argument('set_strings',nargs=-1)
@pass_config
def concat(config,d,set_strings):
    """concat the given set of strings"""
    res_str=''
    if config.verbose:
        click.echo('we are in remove digits mode')
        for string in set_strings:
            s=''.join([i for i in string if i.isdigit()==False])
            if res_str=="":
                res_str+=s
            else:
                res_str=res_str+d+s
    else:
        print('we are in no remve digits mode')
        for string in set_strings:
            if res_str=='':
                res_str+=string
            else:
                res_str=res_str+d+string
    print(res_str)

@cli.command()
@click.argument('string',nargs=1)
@pass_config
def lower(config,string):
    """ convert the given string to lower case"""
    if config.verbose==True:
        s=''.join([i for i in string if i.isdigit()==False])
    else:
        s=string
    print(s.lower())


@cli.command()
@click.argument('string',nargs=1)
@pass_config
def upper(config,string):
    """convert the given string to upper case"""
    if config.verbose==True:
        s=''.join([i for i in string if i.isdigit()==False])
    else:
        s=string
    print(s.upper())


if __name__ == '__main__':
    cli()