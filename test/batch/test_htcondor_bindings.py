from __future__ import print_function
import htcondor
import classad
import os
from threading import Thread
import time

LOGFILE = '/tmp/test.log'

SCHEDD_STATUS_CODES = {
    0: 'Unexpanded',
    1: 'Idle',
    2: 'Running',
    3: 'Removed',
    4: 'Completed',
    5: 'Held',
    6: 'Error',
    7: '<',
    8: '>',
}

LOGFILE_STATUS_CODES = {
    0: SCHEDD_STATUS_CODES[1],
    1: SCHEDD_STATUS_CODES[2],
    2: SCHEDD_STATUS_CODES[6],
    4: SCHEDD_STATUS_CODES[3],
    5: SCHEDD_STATUS_CODES[4],
    7: SCHEDD_STATUS_CODES[6],
    9: SCHEDD_STATUS_CODES[6],
    10: SCHEDD_STATUS_CODES[5],  # suspended == held
    11: SCHEDD_STATUS_CODES[1],  # unsuspended == idle
    12: SCHEDD_STATUS_CODES[5],
    13: SCHEDD_STATUS_CODES[1],  # released == idle
    9: SCHEDD_STATUS_CODES[6],
    # ignore rest
}

TERMINAL_STATUS_CODES = [
    SCHEDD_STATUS_CODES[4],
    SCHEDD_STATUS_CODES[6],
]


def submit_sleeper():
    sub = htcondor.Submit({
        "executable": "/bin/sleep",
        "arguments": "20s",
        'log': LOGFILE})
    schedd = htcondor.Schedd()
    with schedd.transaction() as txn:
        return sub.queue(txn)


def status_from_logfile():
    with open(LOGFILE) as f:
        status = None
        while status not in TERMINAL_STATUS_CODES:
            events = htcondor.read_events(f)
            for event in events:
                eventType = event['MyType']
                eventTypeID = event['EventTypeNumber']
                if eventTypeID in LOGFILE_STATUS_CODES:
                    status = LOGFILE_STATUS_CODES[eventTypeID]
                print("From JOBFILE:", status)


def status_from_schedd(jobID):
    # known_statuses = [
    #     'Unexpanded', 'Idle', 'Running', 'Removed', 'Completed', 'Held',
    #     'Error', '<', '>',
    # ]
    status = None

    schedd = htcondor.Schedd()
    tries = 0
    constraint = 'ClusterId =?= {0}'.format(jobID)
    while status not in TERMINAL_STATUS_CODES:
        jobAD = schedd.query(constraint)
        if jobAD:
            jobAD = jobAD[0]
        else:
            if status is not None:
                # check history
                history = list(schedd.history(constraint, ['JobStatus'], 1))
                if not history:
                    print('Job status is UNKNOWN!')
                    msg = "Could not find job with job id = {0}".format(
                        jobID
                    )
                    raise Exception(msg)
                else:
                    jobAD = list(history)[0]
        jobStatus = jobAD['JobStatus']
        status = SCHEDD_STATUS_CODES[jobStatus]
        print('From Schedd:', status)
        time.sleep(5)
        tries += 1


if __name__ == '__main__':
    os.remove(LOGFILE)
    jobID = submit_sleeper()
    print(jobID)
    Thread(target=status_from_logfile).start()
    Thread(target=status_from_schedd, args=(jobID,)).start()
