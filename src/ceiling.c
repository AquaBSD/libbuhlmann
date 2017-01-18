#include <math.h>

#include "buhlmann.h"

#include <config.h>



// Return Absolute pressure of the Ceiling
double getCeiling(const struct compartment_constants *constants,
               struct compartment_state *compt)
{
    double PStopN2 = 0.0;
	double PStopHe = 0.0;
	
	//N2
	PStopN2 = (compt->n2_p - constants->n2_a) * constants->n2_b;

	//H2
	PStopHe = (compt->he_p - constants->he_a) * constants->he_b;

	if (PStopN2 > PStopHe)
		return PStopN2;
	return PStopHe;
}
