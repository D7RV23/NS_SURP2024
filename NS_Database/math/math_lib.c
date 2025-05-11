// Compile into shared lib with command:
//
//  clang -shared -o ns_math_lib.so -fPIC math_lib.c -lm

//----------------------------------------------------------------------------

#include <math.h> // Remember to include compiler flag -lm for this math lib
#include <stdio.h>

// Just incase the Macro doesnt exist in the compile environment
#ifndef M_PI                            
#define M_PI 3.14159265358979323846     
#endif

double compute_dPdr(double p, double rho, double r, double mr){

    const double speed_of_light = 2.99792458e10;
    const double grav_constant = 6.6743e-8;
    const double pi = M_PI;

    // The actual formula:
    return (-(grav_constant * mr * rho) / pow(r, 2)) *
        (1 + p / (rho * pow(speed_of_light, 2))) * 
        (1 + ((4 * pi * pow(r, 3) * p) / (mr * pow(speed_of_light, 2)))) * 
        (1 / (1 - (2 * grav_constant * mr) / (pow(speed_of_light, 2) * r)));
}

int main(void){

    printf("Example output:\n");
    double test = compute_dPdr(1.0e16, 1.0e5, 1.0e6, 1.0e30);
    printf("dPdr: %e\n", test);
    
    return 0;
}
