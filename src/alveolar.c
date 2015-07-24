#include <math.h>

#include "buhlmann.h"

#include <config.h>

double ventilation(double pamb,
                   double rq,
                   double ig_ratio)
{
    double palv;

    palv = (pamb - WATER_VAPOR_PRESSURE + ((1 - rq) / rq) * CO2_PRESSURE) *
           ig_ratio;

    return palv;
}


