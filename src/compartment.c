#include <math.h>

#include "buhlmann.h"

#include <config.h>

double compartment_mvalue(const struct compartment_constants *constants,
                          struct compartment_state *compt)
{
    double a, b;

    a = ((compt->n2_p * constants->n2_a) + (compt->he_p * constants->he_a)) /
        (compt->n2_p + compt->he_p);
    b = ((compt->n2_p * constants->n2_b) + (compt->he_p * constants->he_b)) /
        (compt->n2_p + compt->he_p);

    return ((compt->n2_p + compt->he_p) - a) * b;
}

void compartment_stagnate(const struct compartment_constants *constants,
                          struct compartment_state *cur,
                          struct compartment_state *end,
                          double p_ambient,
                          double time,
                          double rq,
                          double n2_ratio, double he_ratio)
{
    double n2_palv;
    double he_palv;

    n2_palv = ventilation(p_ambient, rq, n2_ratio);
    he_palv = ventilation(p_ambient, rq, he_ratio);

    end->n2_p = haldane(cur->n2_p, n2_palv, time,
                        constants->n2_h);
    end->he_p = haldane(cur->he_p, he_palv, time,
                        constants->he_h);
}

void compartment_descend(const struct compartment_constants *constants,
                         struct compartment_state *cur,
                         struct compartment_state *end,
                         double p_ambient,
                         double rate,
                         double time,
                         double rq,
                         double n2_ratio, double he_ratio)
{
    double n2_palv;
    double he_palv;
    double n2_rate;
    double he_rate;

    n2_palv = ventilation(p_ambient, rq, n2_ratio);
    he_palv = ventilation(p_ambient, rq, he_ratio);
    n2_rate = rate * n2_ratio;
    he_rate = rate * he_ratio;

    end->n2_p = schreiner(cur->n2_p, n2_palv, n2_rate, time,
                          constants->n2_h);
    end->he_p = schreiner(cur->he_p, he_palv, he_rate, time,
                          constants->he_h);
}


