#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

int sum; /* this data is shared by the thread(s) */
void *runner(void *param); /* the thread */

main(int argc, char *argv[])
{
	pthread_t tid1, tid2; /*the thread identifier*/
	pthread_attr_t attr; /*set of thread attributes*/

	if (argc != 2) {
  		fprintf(stderr, "usage: a.out<integer value>\n");
  		exit(0);
	}
	if (atoi(argv[1]) < 0) {
		fprintf(stderr, "%d must be >= 0\n", 	atoi(argv[1]));
		exit(0);
	}

	pthread_attr_init(&attr);
	/* create the threads*/
	pthread_create(&tid1,&attr,runner,argv[1]);
	pthread_create(&tid2,&attr,runner,argv[1]);

	pthread_join(tid1,NULL);
	pthread_join(tid2,NULL);
	printf("sum = %d\n",sum);
}

/*The thread will begin control in this function*/
void *runner(void *param)
{
	int upper = atoi(param);
	int i;
	sum = 0;
	if (upper > 0) {
			for (i = 1; i <= upper; i++){
				sum += i;
				printf("sum = %d, %d\n",sum,i);
			}
	}
	pthread_exit(0);
}



