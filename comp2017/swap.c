#include<stdio.h>
#include<stdlib.h>
void swap(int a, int b){
	int c;
	int c = a;
	int a=b;
	int b=c;
	printf("%d , %d",a,b);

}

int main(int argc, char * argv[]){
	int a = 2;
	int  b = 5;
	swap(a,b);
	printf("%d %d\n",a,b); //print 3,2 despite giving 2, 3
	return 0;
}
