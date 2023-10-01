#!/usr/bin/env python
# coding=utf-8

# Nikita Akimov
# interplanety@interplanety.org
#
# GitHub
#    https://github.com/Korchy/inkscape_custom_attribute

import sys
from inkex import EffectExtension, NSS


# for debug output
def eprint(*args, **kwargs):
    # print to stderr
    print(*args, file=sys.stderr, **kwargs)


class CustomAttribute(EffectExtension):

    def effect(self):
        # main method for Effect action
        if self.options.ca_name:
            attribute_name = self.options.ca_name
            # add namespace
            if self.options.ca_namespace:
                attribute_name = self.options.ca_namespace + ':' + self.options.ca_name
                # if namespace not exists in the namespace map
                if self.options.ca_namespace not in NSS:
                    namespace_uri = 'http://' + self.options.ca_namespace + '.org/namespace'
                    self.svg.add_namespace(self.options.ca_namespace, namespace_uri)
                    NSS[self.options.ca_namespace] = namespace_uri
            # add custom attribute for each selected object
            for selected_obj in self.svg.selection:
                selected_obj.set(
                    attribute_name,
                    self.options.ca_value
                )

    def add_arguments(self, pars):
        # parse arguments from the UI
        pars.add_argument(
            '--ca_namespace',
            type=str,
            default='',
            help='Namespace'
        )
        pars.add_argument(
            '--ca_name',
            type=str,
            default='',
            help='Name'
        )
        pars.add_argument(
            '--ca_value',
            type=str,
            default='',
            help='Value'
        )


if __name__ == '__main__':
    CustomAttribute().run()
