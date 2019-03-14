#include <stdio.h>
#include <stdlib.h>

int main(int argc, char * argv[]){
	char String[100];
	printf("enter something to shout: ");
	fgets(String, 99, stdin);
	uppercase(String);
	printf("the String in upper case:\n%s",String);
}

void uppercase(char S[]){
	int index_count;
	while(S[index_count] != '/0'){
		if(S[index_count]>'a' && S[index_count]<'z'){
			s[index_count]=s[index_count]-32;
		}
		index_count++;
	}
}

