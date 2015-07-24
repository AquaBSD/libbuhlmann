#include <math.h>

#include "buhlmann.h"

#include <config.h>

double haldane(double pt0,
               double palv0,
               double t,
               double half_val)
{
    double k;
    double pt;

    k = M_LN2 / half_val;
    pt = pt0 + (palv0 - pt0) * (1.0f - exp(-k * t));

    return pt;
}

