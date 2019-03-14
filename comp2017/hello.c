#include<stdio.h>
#include<stdlib.h>

int main(){
	char sentence[] = "what is your name?";
	printf("%s\n",sentence);
	char name[20];
	fgets(name,19,stdin);
	printf("your name is %s\n",name);}

