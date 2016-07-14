#!/usr/bin/env python
#
#   Copyright (c) 2016 In-Q-Tel, Inc, All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
"""
Created on 14 Jul 2016
@author: dgrossman
"""


class Monitor_Action_Base(object):

    def __init__(self):
        self.mod_name = self.__class__.__name__
        self.owner = None
        self.configured = False
        self.config_section_name = None
        self.actions = dict()

    def set_owner(self, owner):
        self.owner = owner
        self.config_section_name = self.owner.mod_name + ':' + self.mod_name

    def configure(self):
        if self.owner:
            conf = self.owner.Config.get_endpoint('Handle_SectionConfig')
            self.config = conf.direct_get(self.mod_name)
            self.configured = True

    def configure_endpoints(self):
        # print self.mod_name,'configure_endpoints'
        if self.owner and self.configured:
            for k, v in self.actions.iteritems():
                # print 'about to configure %s\n' % (k)
                v.configure()