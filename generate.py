import argparse
import os

_PARSER = argparse.ArgumentParser()

_PARSER.add_argument('type')
_PARSER.add_argument('name')

_ARGS = _PARSER.parse_args()


def create_file(filename, content):
    """
    :param str filename:
    :type content: list[str]
    """
    with open(filename, 'w+') as fp:
        fp.write('\n'.join(content) + '\n')


def main():
    dirname = str(_ARGS.name).lower() # kebab/spinal-case
    camelcase_base = ''.join([x.capitalize() for x in dirname.split('-')])
    component_name = '%sComponent' % camelcase_base
    modal_name = '%sModal' % camelcase_base

    os.chdir('app/pages')
    if _ARGS.type in ['page', 'p', 'Page']:
        os.makedirs(dirname)
        os.chdir(dirname)
        create_file('%s.ts' % dirname, ['import { Component } from "@angular/core";',
                                        '', '@Component({', 'selector: "my-app",',
                                        'templateUrl: "%s.html",' % dirname,
                                        'styleUrls: ["%s.scss"],' % dirname,
                                        '})', 'export class %s {' % component_name,
                                        '', '}'])
        create_file('%s.html' % dirname, ['<StackLayout>', '', '</StackLayout>'])
        create_file('%s.scss' % dirname, ['%s{' % dirname, '', '}'])

    elif _ARGS.type in ['modal', 'm', 'Modal']:
        create_file('%s.ts' % dirname, ['import { Component } from "@angular/core";',
                                        '', '@Component({', 'selector: "my-app",',
                                        'template: ``',
                                        'styleUrls: ["%s.scss"],' % dirname,
                                        "})", "export class %s {" % modal_name,
                                        '', '}'])
        create_file('%s.scss' % dirname, ['%s{' % dirname, '', '}'])


if __name__ == '__main__':
    main()
