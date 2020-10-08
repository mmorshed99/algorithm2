# HomeWork 2 README

Role Playing games

## How to Use the Program

To run test case 1, need to use 1 as a command line argument, Example on mac: java -jar battle.jar 1
To run test case 2, need to use 2 as a command line argument, Example on mac: java -jar battle.jar 2

## Program Completion Overview

The program has been completed as per requirements. There is no known incomplete requirement. It is tested
using unit tests. All the classes have more than 90% test coverage except driver class named battle, which
Contains lot of test related functions, whose can not be tested using unit tests.

## Design and Design Document Changes After Design Meeting

* UML Diagram was updated for changes like adding Comparable class for sorting dresses and Double dispatch. 
  Those changes were not initially thought of, but later used during implementation to remove poor design styles. 
  Double dispatch was used to know the dress types using equals methods both in abstract class and implemented classes.
* Functions names were updated to match the actual functionalities.

## Citation

* Java Syntax: https://www.w3schools.com/java/
