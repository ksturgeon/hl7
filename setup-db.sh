#! /bin/bash

# set up db demo bits
# Run this on the edge node as user mapr

# create database tables
# User Table:
maprcli table create -path /user-table -tabletype json

