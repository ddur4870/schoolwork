#include<stdio.h>
#include<stdlib.h>

int main(int argc, char *argv[]){
	printf("what is your name?");
	char name[20];
	fgets(name,19,stdin);
	char * name_point;
	int name_size;
	char *name_0;
	for(name_point = name_0 ; *name_point != '\0' ; name_point++){
		name_size =  name_0 - name_point;
	}
	printf("size of the name is : %d", name_size);
	printf("your name is: %s ",name);
	printf("%s, what's something you like?",name);
	char repeater[100];
	fgets(repeater, sizeof repeater, stdin);
	printf("System arguments: %s",*argv);
	printf(" %s likes eating: %s", name, repeater);
}




