PRO.1                                                                          <<10-02-26>>
#include<stdio.h>
main()
{
	int a=10;
	int *p;
	printf("a=%d",a);
	printf("\naddress=%d",&a);
	p=&a;
	printf("\naddress=%d",p);
	
	printf("\nbefor change value=%d",*p);
	*p=200;
	printf("\nafter change valude=%d",*p);
	printf("\na=%d",a);
}
/*out put:
a=10
address=6487572
address=6487572
befor change value=10
after change valude=200
a=200
*/
--------------------------------
PRO.2                                                                          <<10-02-26>>
#include<stdio.h>
int main()
{
	int a;
	int *p;
	printf("\naddress (&a):%d",&a);
	p=&a;
	printf("\naddress (p):%d",p);
	printf("\nenter a number:");
	scanf("%d",&*p);
	printf("\n%d",*p);
	printf("\n%d",a);
	*p=60;
	printf("\n%d",a);
	
}
/*
output:
address (&a):6487572
address (p):6487572
enter a number:23

23
23
60
*/