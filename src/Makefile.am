lib_LTLIBRARIES = libbuhlmann.la
libbuhlmann_la_SOURCES = buhlmann.c \
						 haldane.c \
						 schreiner.c \
						 zh-l12.c \
						 zh-l16.c \
						 compartment.c \
						 alveolar.c \
						 ceiling.c \
						 stop.c \
						 otu.c \
						 gradientfactor.c
libbuhlmann_la_CFLAGS = -W -Wall -O2
include_HEADERS = buhlmann.h
noinst_PROGRAMS = dive
dive_LDFLAGS = -static
dive_LDADD = libbuhlmann.la
dive_SOURCES = dive.c getline.c
