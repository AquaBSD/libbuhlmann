#include <math.h>

#include "buhlmann.h"

#include <config.h>


double gradient_factor_slope(double gfhi, double gflow,
							 double final_stop_depth, double first_stop_depth)
{
	double gfslope = 0.0f;

	if (final_stop_depth - first_stop_depth != 0.0)
	{
		gfslope = (gfhi - gflow)/(final_stop_depth - first_stop_depth);
	}
	return gfslope;
}


double gradient_factor(double gfslope, double curr_stop_depth, double gfhi)
{
	double gf;

	gf = (gfslope * curr_stop_depth) + gfhi;

	return gf;
}
