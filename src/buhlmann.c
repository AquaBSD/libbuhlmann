#include <math.h>

#include "buhlmann.h"

#define PP_VAPOR 0.063f

#define ZHL12_NR_COMPARTMENTS 16
static const struct compartment_constants zhl12[ZHL12_NR_COMPARTMENTS] = {
    /* He-1/2t, N2-1/2t, He factors {A, B}, N2 factors {A, B} */
    {     1.0f,   2.65f,  {2.200f, 0.820f},  {2.200f, 0.820f} },
    {     3.0f,   7.94f,  {1.500f, 0.820f},  {1.500f, 0.820f} },
    {     4.6f,  12.20f,  {1.080f, 0.825f},  {1.080f, 0.825f} },
    {     7.0f,  18.50f,  {0.900f, 0.835f},  {0.900f, 0.835f} },
    {    10.0f,  26.50f,  {0.750f, 0.845f},  {0.750f, 0.845f} },
    {    14.0f,  37.00f,  {0.580f, 0.860f},  {0.580f, 0.860f} },
    {    20.0f,  53.00f,  {0.470f, 0.870f},  {0.470f, 0.870f} },
    {    30.0f,  79.00f,  {0.455f, 0.890f},  {0.455f, 0.890f} },
    {    43.0f, 114.00f,  {0.455f, 0.890f},  {0.455f, 0.890f} },
    {    55.0f, 146.00f,  {0.511f, 0.926f},  {0.455f, 0.934f} },
    {    70.0f, 185.00f,  {0.511f, 0.926f},  {0.455f, 0.934f} },
    {    90.0f, 238.00f,  {0.515f, 0.926f},  {0.380f, 0.944f} },
    {   115.0f, 304.00f,  {0.515f, 0.926f},  {0.255f, 0.962f} },
    {   150.0f, 397.00f,  {0.515f, 0.926f},  {0.255f, 0.962f} },
    {   190.0f, 503.00f,  {0.515f, 0.926f},  {0.255f, 0.962f} },
    {   240.0f, 635.00f,  {0.515f, 0.926f},  {0.255f, 0.962f} },
};

static double p_insp(double p_amb,
                     double f_ig)
{
    return (p_amb - PP_VAPOR) * f_ig;
}

static double equalize(double p_o,
                       double p_insp,
                       double time,
                       double half_val)
{
    double k;
    double p_e;

    k = M_LN2 / half_val;
    p_e = p_o + (p_insp - p_o) * (1.0f - exp(-k * time));

    return p_e;
}

static double zhl12_p_tol(int    compt,
                          double p_he,
                          double p_n2)
{
    double p;
    double a;
    double b;
    double p_tol;

    if (compt >= ZHL12_NR_COMPARTMENTS)
        return 0.0f;

    p = p_he + p_n2;
    a = ((p_he * zhl12[compt].he_mvalues[0]) +
         (p_n2 * zhl12[compt].n2_mvalues[0])) / p;
    b = ((p_he * zhl12[compt].he_mvalues[1]) +
         (p_n2 * zhl12[compt].n2_mvalues[1])) / p;

    p_tol = (p - a) * b;

    return p_tol;
}

void zhl12_update(struct compartment_state *cur,
                  struct compartment_state *end,
                  double p_amb,
                  double time,
                  double f_n2,
                  double f_he)
{
    int i;
    double p_n2_insp;
    double p_he_insp;

    p_n2_insp = p_insp(p_amb, f_n2);
    p_he_insp = p_insp(p_amb, f_he);

    for (i = 0; i < ZHL12_NR_COMPARTMENTS; i++) {
        end[i].p_he = equalize(cur[i].p_he, p_he_insp, time,
                               zhl12[i].he_half_val);
        end[i].p_n2 = equalize(cur[i].p_n2, p_n2_insp, time,
                               zhl12[i].n2_half_val);
        end[i].p_tol = zhl12_p_tol(i, end[i].p_he, end[i].p_n2);
    }
}

