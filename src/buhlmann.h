#ifndef _BUHLMANN_H_
#define _BUHLMANN_H_

struct compartment_constants
{
    double he_half_val;
    double n2_half_val;
    double he_mvalues[2];
    double n2_mvalues[2];
};

struct compartment_state
{
    double p_he;
    double p_n2;
    double p_tol;
};

#endif /* _BUHLMANN_H_ */
