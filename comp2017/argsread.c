#include<stdio.h>
#include<stdlib.h>

int main(int argc, char *argv[]){

	int counter;
	int i;
	printf("program name is %s\n",argv[0]);
	if(argc==1){
	printf("no extra arguments\n");
	}
	else{
		for(i=0;i<argc;i++){
			printf("argument number %d is %s\n",i,argv[i]);
		}
	}
}
