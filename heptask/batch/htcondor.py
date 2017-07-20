'''
 - Tasks should work as a composite pattern
 - should be able to inject
    - resource requirements and task dependencies
    - expected output
'''

class HTCondorTask(object):
    __slots__ = ['subtasks', 'payload']
    def __init__(self):
        pass

    def requires(self):
        pass

    def run(self):
        for task in self.subtasks:
            task.run()

        # execute own payload
        self.payload.execute()
