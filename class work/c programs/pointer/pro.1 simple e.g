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