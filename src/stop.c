#include <math.h>

#include "buhlmann.h"

#include <config.h>
#include <stdio.h>


// void compartment_stagnate(const struct compartment_constants *constants,
//                           struct compartment_state *cur,
//                           struct compartment_state *end,
//                           double p_ambient,
//                           double time,
//                           double rq,
//                           double n2_ratio, double he_ratio)


double nodecotime(const struct compartment_constants *constants,
				struct compartment_state *compt,
				double p_ambient,
				double n2_ratio,
				double he_ratio)
{
	double ceiling = 0.0;
	double Addtime = 100;
	int iter = 0;
	struct compartment_state end;
	
    compartment_stagnate(constants,
                        compt, &end,
                        p_ambient,
                        Addtime, 
                        BUHLMANN_RQ, 
                        n2_ratio, 
                        he_ratio);
   
    ceiling = getCeiling(constants,&end);
    
    if (ceiling <= 1.0) // Surface donc 99
    	return Addtime;

    // trop de celing ou trop en surface 
    while ( iter < 100 && Addtime < 101 && (ceiling < 0.99 || ceiling > 1.1))
	{
		compartment_stagnate(constants,
                        compt, &end,
                        p_ambient,
                        Addtime, 
                        BUHLMANN_RQ, 
                        n2_ratio, 
                        he_ratio);
		ceiling = getCeiling(constants,&end);

		if (ceiling )


		if (ceiling > 1.1) // on a un ceilling trop gros
			Addtime = Addtime*.5;
		else
			Addtime = Addtime*1.5;
		iter ++;

		
	}

    //printf ("\n iter : %i - ceiling : %f - AddTime : %f \n", iter, ceiling, Addtime);
    return Addtime;

}