#include<stdio.h>
#include<stdlib.h>

int main(){
	printf("enter something to repeat");
	char word[20];
	fgets(word,20,stdin);
	printf("%s\n",word);
}
