#include<stdio.h>
#include<stdlib.h>




int main(void) {
 int t;
 scanf("%d\n",&t);
 
 int i,holes;
 char c;

 for(i = 0;i < t;i++){
	holes = 0;
	do {
    c=getchar();
    if (c == 'B'){
		holes += 2;
		}
	else if ( c == 'A'|| c == 'D'||c == 'O'||c == 'P'||c == 'Q'||c == 'R'){
		holes +=1;
		}
	else {
		}	
	} while (c != '\n');
	printf("%d\n",holes);
 
	
 }

 

return 0;
}