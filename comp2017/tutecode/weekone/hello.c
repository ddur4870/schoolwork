#include<stdio.h>
#include<stdlib.h>

int main(int argc, char *argv[])
{
	char word[100];
	char other[100];
	if(fgets(word, 100, stdin)){
		printf("1: %s\n", word);
	}
	fgets(other, 100, stdin);
	printf("2: %s\n", other);
}
