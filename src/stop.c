#include <math.h>

#include "buhlmann.h"

#include <config.h>
#include <stdio.h>


double checkforstop(const struct compartment_constants *constants,
					struct compartment_state *compt,
					double p_ambient)
{
	double next_stop = 0.0; 
	double dp = STOPINC;
	double dt = 1;
	short isFound = 0;
	struct compartment_state end;

	end.n2_p = compt->n2_p;
	end.he_p = compt->he_p;
 
	if (p_ambient != 0)
		next_stop =  p_ambient - fmod(p_ambient,0.3);

	while (next_stop >= 0 && !isFound)
	{
		compartment_descend(constants,
                            &end, &end,
                            p_ambient, dp / dt,
                            dt, BUHLMANN_RQ, 0.78084f, 0.0f);
		if (end.n2_p > constants->n2_a)
			isFound = 1;
		next_stop = next_stop - 0.3;
	}
	return next_stop;


} 

double nostoptime(const struct compartment_constants *constants,
				struct compartment_state *compt,
				double p_ambient)
{
	double k = 0.0;
	double pi = 0.0;  
	double po = 0.0;
	double p = 0.0;
	double t = 0.0;

	k = 0.693/constants->n2_h;
	p = ((constants->n2_a + 1.003) / constants->n2_b)*10;

	pi = ((p_ambient*10) - WATER_VAPOR_PRESSURE)*0.79;
	po = ((1.003*10) - WATER_VAPOR_PRESSURE)*0.79;

	if (pi == po)
		return 0.0;

	
	t = (-1 / k) * log((pi - p)/(pi - po));
	if (t < 0)
		t = 0;

	return t;

}