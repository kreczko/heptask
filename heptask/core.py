import os
from plumbum import local


class Payload(object):
    __slots__ = ['executable', 'parameters']

    def __init__(self, executable, parameters):
        '''

        '''
        self.executable = executable
        self.parameters = parameters

    def execute(self):
        if callable(self.executable):
            if isinstance(self.parameters, dict):
                self.executable(**self.parameters)
            else:  # assume list
                self.executable(*self.parameters)
        elif os.path.isfile(self.executable):
            if isinstance(self.parameters, dict):
                exe = local[self.executable]
                result = exe[self.__params2commandline]

    def __params2commandline(self):
        parameters = self.parameters
        if isinstance(parameters, dict):
            parameters = [
                '--{name}={value}'.format(name, value) for name, value in parameters]
        return parameters


class HEPTask(object):
    :
    pass


class TaskFactory(object):

    @staticmethod
    def map(task, input_files, watcher=True, taskClass=)
