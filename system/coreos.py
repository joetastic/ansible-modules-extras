#!/usr/bin/python
# -*- coding: utf-8 -*-

DOCUMENTATION = '''
---
module: coreos
short_description: FIXME
description:
    - FIXME
version_added: FIXME
options: FIXME
notes: FIXME
requirements: FIXME
'''

EXAMPLES = '''
FIXME
'''


def main():
    module = AnsibleModule(
        argument_spec=dict(
        )
    )

    module.exit_json(changed=False)

# weird pattern that seems normal in ansible
# import module snippets
from ansible.module_utils.basic import *

main()
