#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct matrix_t {
  double **m;
  int r;
  int c;
} matrix;

void print_m(double **m, int r, int c){
  for(int x = 0; x < r; x++){
      for(int j = 0; j < c; j++){
          printf("%8.2f ", m[x][j]);
      }
      printf("\n");
  }
  printf("\n");
}

double **xalloc(int r, int c){
  double **matrix = (double**)malloc(sizeof(double*) * r);
  for(int x = 0; x < r; x ++){
    matrix[x] = (double*)calloc(c, sizeof(double));
  }
  return matrix;
}

double **mmult(double **A, double **B, int rA, int cA, int rB, int cB){
    double **new = xalloc(rA, cB);
    for(int x = 0; x < rA; x++){
        for(int i = 0; i < cB; i ++){
            for(int j = 0; j < rB; j++){
                new[x][i] += A[x][j] * B[j][i];
            }
        }
    }
    return new;
}

double **mread(FILE *fp, int *r, int *c){
  double **matrix = xalloc(*r, *c);
  for(int x = 0; x < *r; x++){
    for(int j = 0; j < *c; j++){
      scanf("%lf", &matrix[x][j]);
    }
  }
  return matrix;
}


int main(){
    int total;
    scanf("%d", &total);
    struct matrix_t *matrices[total];

    for(int x = 0; x < total; x++){
        printf("Matrix: %d\n", x);
        struct matrix_t *mx = malloc(sizeof(struct matrix_t));
        scanf("%d", &mx->r);
        scanf("%d", &mx->c);
        mx->m = mread(stdin, &mx->r, &mx->c);
        matrices[x] = mx;
        print_m(mx->m, mx->r, mx->c);
    }

    for(int x = 0; x < total - 1; x++){
        matrices[x+1]->m = mmult(matrices[x]->m, matrices[x+1]->m,
                              matrices[x]->r, matrices[x]->c,
                              matrices[x+1]->r, matrices[x+1]->c);
        matrices[x+1]->r = matrices[x]->r;
    }
    
    printf("Resulting Matrix:\n");
    print_m(matrices[total-1]->m, matrices[total-1]->r, matrices[total-1]->c);
    return 0;
}
