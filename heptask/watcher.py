'''
                       xxxxxxxx
              xxxxxxxxxxxxx  xxxxxxxxxx
          xxxxxxxxxxxxxx    xxx  xxxxxxxxx
       xxxxxx    xxxxxxxxx   xxxx    xxxxxxxx
       xxx      xxxxxxxxxxxx  xxxx     xxxxxxxxx
      xx       xxxxxxxxxxxxxxxxxxxx       xxxxxx
     xx        xxxxxxxxxxxxxxxxxxxx       xxxxxx
     xxx        xxxxxxxxxxxxxxxxxx       xxxxx
      xxx        xxxxxxxxxxxxxxx       xxxxx
        xxxx        xxxxxxxxxx        xxxx
           xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
               xxxxxxxxxxxxxxxxxxx
'''


class Resource(object):
    '''
        Resource object that is filled by the task
    '''
    __slots__ = ['disk', 'cpu', 'memory', 'swap', 'network', 'processes']

    def __init__(self):
        pass


class WatcherInfo(object):
    '''
        Stores
            - ID: pid(local), batch ID (batch), grid_url (grid)
            - executable & parameters
            - resource_usage (disk, cpu, memory, swap, network, processes)
            - resource_requests (cpu, memory)
            - host, host_ip(v4,v6)
            - taskmon_url (if available)
            - status
    '''
    __slots__ = ['id', 'executable',
                 'resource_usage', 'resource_requests', 'host', 'host_ipv4',
                 'host_ipv6', 'taskmon_url', 'status']



class Watcher(object):
    __slots__ = ['_info', '_task']

    def __init__(self, task):
        self._task = task
        self._info = self.__extract_into(task)

    def __safe_info(self, monitorable):
        if self._info and monitorable in self._info:
            return self._info[monitorable]
        else:
            return None

    @property
    def id(self):
        self.__safe_info('id')

    @property
    def executable(self):
        self.__safe_info('executable')
