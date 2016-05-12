# libbuhlmann

[![Build Status](https://secure.travis-ci.org/AquaBSD/libbuhlmann.svg)](https://travis-ci.org/AquaBSD/libbuhlmann)

#### Table of Contents

1. [Overview](#overview)
2. [Description](#description)
2. [Requirements](#Requirements)
3. [Usage](#usage)
4. [Development](#development)

## Overview

## Description

The Bühlmann decompression algorithm is  a mathematical model (algorithm) of the
way in which inert gases enter and  leave the human body as the ambient pressure
changes. It  is used to create  Bühlmann tables. These  are decompression tables
which  allow  divers  to  plan  the  depth  and  duration  for  dives  and  show
decompression stops when necessary.

The algorithm was  developed by Swiss physician Dr. Albert  A. Bühlmann, who did
research into decompression theory at the Laboratory of Hyperbaric Physiology at
the  University  Hospital in  Zürich,  Switzerland.  The  results of  Bühlmann's
research that began  in 1959 were published in a 1983  German book whose English
translation  was  entitled Decompression-Decompression  Sickness.  The book  was
regarded as the most complete public reference on decompression calculations and
was used soon after in dive computer algorithms.

## Requirements

#### To compile
	- Automake
	- Autoconf

#### To test
	- python
	- matplotlib

## Usage

#### STDIN

Here's an example of decompression calculation from STDIN:

```bash
➥  python test/gen_dive.py -d 20 -t 5 | src/dive 
   [...]
```   

To display the result on a nice interactive graph:

```bash
➥  python test/gen_dive.py -d 20 -t 5 | src/dive | python tools/visoutput.py
```

remember to run the output visuatlisation on a Virtual python environment.
```bash
➥  cd tools && virtualenv venv && source venv/bin/activate
➥  pip install -r requirements.txt
```

## Development

Feel free to contribute on GitHub.


## References

Erik C. Baker - Understanding M-Values