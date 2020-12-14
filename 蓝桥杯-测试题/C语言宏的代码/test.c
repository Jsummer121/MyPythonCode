#include <stdio.h>
#include <string.h>
int main()
{
#ifndef __x86_64__
    printf("The platform is not x86_64.\n");
#endif
    return 0;
}