/*
	
	Oxygen Toxicity Unit Calulation

*/

#include <math.h>

double otu_const(double time,
                 double o2_ratio)

{
	double otu = 0.0;

	if (o2_ratio > 0.5)
		otu = time * pow(( 0.5 / (o2_ratio - 0.5)), (-5/6));

	return (otu);
}

double otu_descend(double time,
                   double o2_ratio_i,
                   double o2_ratio_f)
{
	double otu = 0.0;

	if (o2_ratio_i > 0.5 || o2_ratio_f > 0.5 )
		otu = ((3/11)*time)/(o2_ratio_f-o2_ratio_i)*(pow((o2_ratio_f - 0.5)/0.5,11/6) - pow((o2_ratio_i - 0.5)/0.5, 11/6));

	return otu;
}
