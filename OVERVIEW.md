# Overview of Schedule Maker

This is another version of the code, I've rewritten this to be as simple as possible. New features include multiple files where the code has been spread out since it was getting impossible to write code in one file (it went over 900 lines).

## Key Changes
- Comments on every line
- Basic Python only (loops, ifs, lists, functions)
- Same features as original (menu system, saves) plus full Round Robin tournament system
- Working tabular format for displaying fixtures and standings
- Round Robin scheduling generates all pairings automatically
- Results can be entered and table updates automatically

## What is Round Robin?
In a round robin tournament, every team plays every other team once. For n teams, there are n*(n-1)/2 matches total.

## How the Table Works
- Win = 3 points
- Draw = 1 point
- Loss = 0 points
- Teams are sorted by points (highest first), then goal difference

All code is documented so you guys can like read and understand most of the stuff
