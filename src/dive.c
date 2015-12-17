#define _GNU_SOURCE
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <math.h>

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
        double n2, he;
        double dt, dp;
        double stop = 0.0;
        double nodectime = 90000.0;

        if (!l) {
            n++;
            continue;
        }

        if (4 != sscanf(line, "%lf %lf %lf %lf", &t, &p, &n2, &he)) {
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
            stop = fmax(checkforstop(&zh_l12[i],&s[i],lastp),stop);

            if (nostoptime(&zh_l12[i],&s[i],lastp) > 0)
                nodectime = fmin(nostoptime(&zh_l12[i],&s[i],lastp),nodectime);
            fprintf(stdout, " %lf %lf", s[i].he_p, s[i].n2_p);
        }
       /* if (nodectime > 0 && nodectime != 90000.0)
            printf(" nodectime : %f min \n", nodectime);
        else
            printf("\n");*/

        /*if (stop > 0.0)
            printf(" Stop recommanded at  : %lf m\n", (stop - 1) * 10 );
        else
            printf("\n");*/
        fprintf(stdout, " %lf\n", ceiling(zh_l12, s, ZH_L12_NR_COMPARTMENTS));


        lastp = p;
        lastt = t;
        n++;
    }

    free(line);

    return 0;
}
