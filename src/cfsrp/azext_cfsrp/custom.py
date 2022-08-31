# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.util import CLIError


def create_cfsrp(cmd, resource_group_name, cfsrp_name, location=None, tags=None):
    raise CLIError('TODO: Implement `cfsrp create`')


def list_cfsrp(cmd, resource_group_name=None):
    raise CLIError('TODO: Implement `cfsrp list`')


def update_cfsrp(cmd, instance, tags=None):
    with cmd.update_context(instance) as c:
        c.set_param('tags', tags)
    return instance