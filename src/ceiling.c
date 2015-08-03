#include <math.h>

#include "buhlmann.h"

#include <config.h>

double ceiling(const struct compartment_constants *constants,
               struct compartment_state *compt,
               int ncompt)
{
    int i;
    double c = -HUGE_VAL;

    for (i = 0; i < ncompt; i++) {
        double mval = compartment_mvalue(&constants[i], &compt[i]);

        c = fmax(c, mval);
    }

    return c;
}
