#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include <config.h>

#ifndef HAVE_GETLINE

ssize_t getline(char **lineptr, size_t *n, FILE *stream)
{
    size_t l = 0;
    int ch;
    char *buf = NULL;
    size_t buflen = 16;

    buf = realloc(*lineptr, buflen);
    if (!buf)
        return -1;

    do {
        if ((l + 2) > buflen) {
            char *tmp = realloc(buf, buflen * 2);
            if (!tmp) {
                free(buf);
                return -1;
            }
            buf = tmp;
            buflen *= 2;
        }

        ch = getc(stream);
        if (ch == EOF)
            break;

        buf[l++] = (char) ch;

        if (ch == '\n')
            break;
    } while (1);

    if (l == 0)
        return -1;

    buf[l] = '\0';
    *lineptr = buf;
    *n = buflen;

    return l;
}

#endif
