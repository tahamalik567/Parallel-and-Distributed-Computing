#include <omp.h>
#include <stdlib.h>
#include <stdio.h>

int main(int argc , char** arg){
	int th_id;
	int nthreads = omp_get_num_threads();
	#pragma omp parallel private(th_id)
	{
		th_id = omp_get_thread_num();
		printf("hello world form thread %d \n",th_id);
		
	}
	return 0;
}