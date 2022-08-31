# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
from azure.cli.core.commands import CliCommandType
from azext_cfsrp._client_factory import cf_cfsrp


def load_command_table(self, _):

    # TODO: Add command type here
    # cfsrp_sdk = CliCommandType(
    #    operations_tmpl='<PATH>.operations#None.{}',
    #    client_factory=cf_cfsrp)


    with self.command_group('cfsrp') as g:
        g.custom_command('create', 'create_cfsrp')
        # g.command('delete', 'delete')
        g.custom_command('list', 'list_cfsrp')
        # g.show_command('show', 'get')
        # g.generic_update_command('update', setter_name='update', custom_func_name='update_cfsrp')


    with self.command_group('cfsrp', is_preview=True):
        pass

