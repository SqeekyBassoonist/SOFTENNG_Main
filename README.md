# SOFTENNG_Main

Contains the Main Project for SOFTENNG 1 - Microservices are in separate repos


## Purpose

This project will eventually be a music player, with a built-in alarm and timer, and both local and database-backed playing.
This repo will define the parts of the project related to UI. It will allow the user to:

    - play and specific song from either local files or from a database
    - set a timer/alarm, which will play a specific song once the alarm goes off.
    - upload music to a database, as well as download music from the database

## Microservices

This is subject to change as the term goes on, but the microservices are tentatively going to be:

    - An alarm system that reports back to the calling process once either the timer hits 0, or the set time is reached
        - So one could set a 15 minute timer, or an alarm for 3:30 PM

    - A database hosting various songs and playlists
        - The main program will be able to access these through some method or other, I haven't decided yet
        
    - A music player, likely based in Python since that's what I'm familiar with.
