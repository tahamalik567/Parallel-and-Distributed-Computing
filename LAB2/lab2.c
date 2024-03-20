#include <omp.h>
#include <stdio.h>

//int main() {
//  int n = 60; // Initialize n
//  int i;
//#pragma omp parallel shared(n) private(i)
//  {
//  	
//#pragma omp for
//
//    for (i = 0; i < n; i++) {
//      printf("Thread %d executes loop iteration %d\n", omp_get_thread_num(), i);
//    }
//  }
//
//  return 0;
//}


//#include <stdio.h>
//#include <omp.h>
//
//int main() {
//    int n = 10; // Initialize n
//    int a; // Declare 'a' outside the parallel region
//	int i;
//    #pragma omp parallel for private(i, a) schedule(static,chunk)
//    for (int i = 0; i < n; i++) {
//        a = i + 1;
//        printf("Thread %d has a value of a = %d for i = %d\n",
//               omp_get_thread_num(), a, i);
//    }
//    // End of parallel for
//
//    return 0;
//}


//---------------------------------------------------------------------------------------------------------------------

//#include <stdio.h>
//#include <omp.h>
//
////Static Scheduling:
////In static scheduling, the iterations are divided into equal-sized chunks, and each thread is assigned a fixed set of chunks.
////The schedule(static) clause ensures that each thread gets a predetermined chunk of work.
////It is useful when the workload is evenly distributed across iterations.
////Here’s the modified code using static scheduling:
//
//
//int main() {
//    int n = 60; // Initialize n
//    int a; // Declare 'a' outside the parallel region
//	int i;
//    #pragma omp parallel for private(i, a) schedule(static)
//    for (int i = 0; i < n; i++) {
//        a = i + 1;
//        printf("Thread %d has a value of a = %d for i = %d\n",
//               omp_get_thread_num(), a, i);
//    }
//
//    return 0;
//}


//----------------------------------------------------------------------------------------------------------------

//#include <stdio.h>
//#include <omp.h>
////Dynamic Scheduling:
////In dynamic scheduling, each thread grabs a chunk of work dynamically as it becomes available.
////The schedule(dynamic) clause allows threads to take work as they finish their previous chunks.
////It is useful when the workload is unevenly distributed or unpredictable.
////Here’s the modified code using dynamic scheduling:
//
//int main() {
//    int n = 100; // Initialize n
//    int a; // Declare 'a' outside the parallel region
//	int i;
//    #pragma omp parallel for private(i, a) schedule(dynamic)
//    for (int i = 0; i < n; i++) {
//        a = i + 1;
//        printf("Thread %d has a value of a = %d for i = %d\n",
//               omp_get_thread_num(), a, i);
//    }
//
//    return 0;
//}

//--------------------------------------------------------------------------------------------------

//Guided Scheduling:
//Guided scheduling is similar to dynamic scheduling but starts with larger chunks and gradually reduces the chunk size.
//The schedule(guided) clause balances between dynamic and static scheduling.
//It is useful when the workload varies but tends to stabilize over time.
//Here’s the modified code using guided scheduling:

#include <stdio.h>
#include <omp.h>

int main() {
    int n = 100; // Initialize n
    int a; // Declare 'a' outside the parallel region
	int i;
    #pragma omp parallel for private(i, a) schedule(guided)
    for (int i = 0; i < n; i++) {
        a = i + 1;
        printf("Thread %d has a value of a = %d for i = %d\n",
               omp_get_thread_num(), a, i);
    }

    return 0;
}


