#include<stdio.h>
#include<curses.h>
#include<string.h>
#include <stdlib.h>

int main()
{
	printf(".......Pass One assembler.......\n\n\n");
	FILE *f1, *f2, *f3, *f4;
	printf("The input program is as follows: \n\n");
	char pp;
	f1 = fopen("input.txt","r");
	f3 = fopen("symtab.txt","w");
	pp = fgetc(f1);
	while (pp!= EOF) 
    	{ 
        	printf ("%c", pp); 
        	pp = fgetc(f1); 
    	} 
	printf("\nThe program after the addresses were assigned: \n\n");
	fseek(f1, 0, SEEK_SET);
	int op,lc,sa,o,len;
	char l[20], m[20],opp[20],otp[20];
	fscanf(f1,"%s %s %d", l,m,&op);
	if(strcmp(m,"START")==0)
	{
		sa=op;
		lc = sa;
		printf("\t%s\t%s\t%d\n",l,m,op);
		
	}
	else
		lc=0;
	fscanf(f1,"%s %s",l,m);
	while(!feof(f1))
	{
		fscanf(f1,"%s",opp);
		printf("%d\t%s\t%s\t%s\n",lc,l,m,opp);
 		if(strcmp(l,"-")!=0)
 		{
 			fprintf(f3,"\n%d\t%s\n",lc,l);
 		}
		f2 = fopen("Optab.txt","r");
		fscanf(f2,"%s %d",otp,&o);
		while(!feof(f2))
		{
			if(strcmp(m,otp)==0)
			{
				lc=lc+3;
				break;
			}
			fscanf(f2,"%s %d", otp,&o);
		}
		fclose(f2);
		if(strcmp(m,"WORD")==0)
		{
			lc=lc+3;
		}
		else if(strcmp(m,"RESW")==0)
		{
			op = atoi(opp);
			lc = lc+(3*op);
		}
		else if(strcmp(m,"BYTE")==0)
		{
			if(opp[0]=='C')
			{
				lc=lc+1;
			}
			else 
			{
				len = strlen(opp)-2;
				lc =lc+len;
			}
		}
		else if(strcmp(m,"RESB")==0)
		{
			op = atoi(opp);
			lc = lc+op;
		}
		fscanf(f1,"%s%s",l,m);
	}
	if(strcmp(m,"END")==0)
	{
		printf("\nProgram length:  %d \n",lc-sa);
	}

	printf("\nThe content of the symbol table is: \n");
	char tt;
	f2 = fopen("Optab.txt","r");
	fseek(f2, 0, SEEK_SET);
	tt = fgetc(f2);
	while (tt!= EOF) 
    	{ 
        	printf ("%c", tt); 
        	tt = fgetc(f2); 
    	} 
	fclose(f1);
	fclose(f3);
	fclose(f2);
	return 0;
}
			
		
