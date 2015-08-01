AC_INIT(libbuhlmann, 1.0, contact@aquabsd.org)
AM_INIT_AUTOMAKE
LT_INIT
AC_CONFIG_SRCDIR([src/buhlmann.c])
AC_CONFIG_HEADERS([config.h])

# Checks for programs.
AC_PROG_CC

# Checks for libraries.

# Checks for header files.
AC_HEADER_STDC
AC_CHECK_HEADERS(math.h)

# Checks for library functions.
AC_CHECK_FUNCS(getline)
AC_CHECK_LIB(m, exp)
AC_CHECK_LIB(m, fmin)

AC_OUTPUT(Makefile src/Makefile)
