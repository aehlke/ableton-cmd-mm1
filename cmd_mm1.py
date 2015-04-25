from __future__ import with_statement

import Live
from _Framework.ControlSurface import ControlSurface


class CMDMM1(ControlSurface):
    __module__ = __name__
    __doc__ = "CMD MM1"

    def __init__(self, c_instance):
        super(CMDMM1, self).__init__(c_instance)

        with self.component_guard():
            self._c_instance = c_instance
            self.helloworld()


    def helloworld(self):
        self.log_message('helloworld')
        self.show_message('helloworld')
