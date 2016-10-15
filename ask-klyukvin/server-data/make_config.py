#!/usr/bin/env python3
import os
import os.path


def make_config(file_name='ask-klyukvin.io'):
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    config_template_path = os.path.join(curr_dir, 'config_template')
    result_path = os.path.join(curr_dir, file_name)

    with open(config_template_path) as config_template:
        lines = config_template.readlines()

    site_root = os.path.dirname(os.path.dirname(curr_dir))
    with open(result_path, 'w+') as result:
        for line in lines:
            result.write(line.replace('{{site_root}}', site_root))


if __name__ == '__main__':
    make_config()
