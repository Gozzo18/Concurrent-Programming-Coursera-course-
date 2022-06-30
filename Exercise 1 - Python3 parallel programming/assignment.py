# Based on RealPython Threading Example page at https://realpython.com/intro-to-python-threading/ and
#   Python.org _thread library documentation at
#   https://docs.python.org/3/library/_thread.html?highlight=_thread#module-_thread
import logging
import random
import sys
import time
from threading import Thread, Lock, active_count

from core import Core

def execute_ticketing_system_participation(ticket_number, part_id, shared_variable):
    output_file_name = "output-" + part_id + ".txt"
    # NOTE: Do not remove this print statement as it is used to grade assignment,
    # so it should be called by each thread
    print("Thread retrieved ticket number: {} started".format(ticket_number), file=open(output_file_name, "a"))
    # wait until your ticket number has been called
    while not ticket_number == shared_variable.ticket_counter:
        time.sleep(random.randint(1,10))
    shared_variable.increaseTicketCount()
    # output your ticket number and the current time
    print(ticket_number, time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.localtime()), file=open(output_file_name, "a"))
    # NOTE: Do not remove this print statement as it is used to grade assignment,
    # so it should be called by each thread
    print("Thread with ticket number: {} completed".format(ticket_number), file=open(output_file_name, "a"))
    return 0

class TicketingSystem:
    ticket_counter = -1

    def __init__(self):
        self.lock = Lock()

    def increaseTicketCount(self):
        self.lock.acquire()
        self.ticket_counter += 1
        self.lock.release()

class Assignment(Core):

    USERNAME = "ric"
    active_threads = []

    def __init__(self, args):
        self.num_threads = 1
        self.shared_ticket_counter = 0
        self.args_conf_list = [['-n', 'num_threads', 1, 'number of concurrent threads to execute'],
                                ['-u', 'user', None, 'the user who is turning in the assignment, needs  to match the '
                                                    '.user file contents'],
                               ['-p', 'part_id', 'test', 'the id for the assignment, test by default']]
        super().__init__(self.args_conf_list)
        super().parse_args(args=args)
        _format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=_format, level=logging.INFO,
                            datefmt="%H:%M:%S")
        self.ticketing_system = TicketingSystem()

    def run(self):
        output_file_name = "output-" + self.part_id + ".txt"
        open(output_file_name, 'w').close()
        if self.test_username_equality(self.USERNAME):
            sleeping_time = 0
            for index in range(self.num_threads):
                logging.info("Assignment run    : create and start thread %d.", index)
                # This is where you will start a thread that will participate in a ticketing system
                # have the thread run the execute_ticketing_system_participation function
                thread = Thread(group=None, target=execute_ticketing_system_participation, args=(index, self.part_id, self.ticketing_system))
                self.active_threads.append(thread)
                # Threads will be given a ticket number and will wait until a shared variable is set to that number
                thread.start()
                sleeping_time += 1
            self.manage_ticketing_system()
            # The code will also need to know when all threads have completed their work
            #for index, thread in enumerate(self.active_threads):
            #    thread.join()
            logging.info("Assignment completed all running threads.")
            return 0
        else:
            logging.error("Assignment had an error your usernames not matching. Please check code and .user file.")
            return 1

    def manage_ticketing_system(self):
        # increment a ticket number shared by a number of threads and check that no active threads are running
        self.ticketing_system.increaseTicketCount()
        while self.ticketing_system.ticket_counter < self.num_threads:
            logging.info("Current number of active threads: %s", len(self.active_threads))
            time.sleep(5)
        return 0


if __name__ == "__main__":
    assignment = Assignment(args=sys.argv[1:])
    exit_code = assignment.run()
    sys.exit(exit_code)
