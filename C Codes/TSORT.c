#include<stdio.h>
#include<stdlib.h>

int a[1000000] = {0};
int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int main(void) {
 int t;
 scanf("%d",&t);
 int i;

 for(i = 0;i < t;i++){
	scanf("\n%d",&a[i]);	
 }

 int n;
 qsort (a, t, sizeof(int), compare);
 for (n=0; n<t; n++)
    printf ("%d\n",a[n]); 

return 0;
}