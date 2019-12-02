import os
from importlib import util as importlib_util

import click


@click.command()
def cli():

    deployment_artifacts_path = '.deployment_artifacts'

    if not os.path.isdir(deployment_artifacts_path):

        os.makedirs(deployment_artifacts_path)

    state_machines_path = 'state_machines'

    if not os.path.isdir(state_machines_path):

        raise Exception('"state_machines" directory not found')

    for filename in os.listdir(state_machines_path):

        click.echo(f'Importing {filename}...')

        module_path = os.path.join(state_machines_path, filename)

        if filename.endswith('.py'):

            module_name = filename.replace('.py', '')

            spec = importlib_util.spec_from_file_location(module_name, module_path)
            module = importlib_util.module_from_spec(spec)
            spec.loader.exec_module(module)

    click.echo('Cool.')
