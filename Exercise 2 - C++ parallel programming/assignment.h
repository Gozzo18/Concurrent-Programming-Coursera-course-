//
// Created by Chancellor Pascale on 1/31/21.
//
#include <thread>
#include <iostream>
#include <fstream>
#include <string>
#include <chrono>
#include <ctime>
#include <atomic>

#ifndef CPP_INITIAL_CODE_ASSIGNMENT_H
#define CPP_INITIAL_CODE_ASSIGNMENT_H

const std::string USERNAME = "ric";
std::atomic<int> currentTicketNumber; // This could be an atomic variable
// Based on the implementation, the student may want to create a shared variable for managing the next ticket number
// to be assigned to a thread
static std::string currentPartId;
static std::string currentUser;
static int currentNumThreads;

void executeTicketingSystemParticipation(int threadIndex);
int runSimulation();
std::string getUsernameFromUserFile();
int manageTicketingSystem(std::thread *threadsPointer);

#endif //CPP_INITIAL_CODE_ASSIGNMENT_H
