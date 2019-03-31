#include<stdio.h>
void swap(int a[], int b[]){
	int *temp;
	temp=&a[0];
	int temp_val = *temp;
	//	b[0]=*temp;
	printf("temp should be 2 and is: %d\n",*temp);
	a[0]=b[0];
	printf("a should now be 3 and is: %d\n", a[0]);
	b[0]=temp_val;
	printf("b should now be 2 and is: %d\n", b[0]);
}

int main(void){
	int a=2;
	int b=3;
	int *c = &a;
	int *d = &b;
	swap(c,d);
	printf("%d %d",a,b);
	return 0;
}

