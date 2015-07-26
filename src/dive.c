#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

#include <buhlmann.h>

int main(void)
{
    struct compartment_state s[ZH_L12_NR_COMPARTMENTS];
    int i;
    char *line; size_t buflen;
    ssize_t l; int n;
    double lastt, lastp;

    lastt = 0.0f;
    lastp = 1.0f;
    for (i = 0; i < ZH_L12_NR_COMPARTMENTS; i++) {
        s[i].he_p = ventilation(lastp, BUHLMANN_RQ, 0.0f);
        s[i].n2_p = ventilation(lastp, BUHLMANN_RQ, 0.78084f);

    }

    line = NULL;
    buflen = 0;
    n = 0;
    while ((l = getline(&line, &buflen, stdin)) != -1) {
        double t, p;
        double dt, dp;

        if (!l) {
            n++;
            continue;
        }

        if (2 != sscanf(line, "%lf %lf", &t, &p)) {
            fprintf(stderr, "Line %d: invalid format\n", n);
            n++;
            continue;
        }

        dt = t - lastt;
        dp = p - lastp;

        if (dt < 0) {
            fprintf(stderr, "Line %d: negative time interval\n", n);
            n++;
            continue;
        }

        fprintf(stdout, "%lf %lf", t, p);
        for (i = 0; i < ZH_L12_NR_COMPARTMENTS; i++) {
            if (dt) {
                compartment_descend(&zh_l12[i],
                                    &s[i], &s[i],
                                    lastp, dp / dt,
                                    dt, BUHLMANN_RQ, 0.78084f, 0.0f);
            }
            fprintf(stdout, " %lf %lf", s[i].he_p, s[i].n2_p);
        }
        fprintf(stdout, "\n");

        lastp = p;
        lastt = t;
        n++;
    }

    free(line);

    return 0;
}
