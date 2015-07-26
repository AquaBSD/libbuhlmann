#include <math.h>

#include "buhlmann.h"

#include <config.h>

double schreiner(double pt0,
                 double palv0,
                 double r,
                 double t,
                 double half_val)
{
    double k;
    double pt;

    k = M_LN2 / half_val;
    pt = palv0 + r * (t - 1.0f / k) - (palv0 - pt0 - r / k) * exp(-k * t);

    return pt;
}

