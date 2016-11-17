#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <inttypes.h>
#include <unistd.h>

const char main_str[] = "zyxwvutsrqponmlkjihgfedcba,9876543210.ZYXWVUTSRQPONMLKJIHGFEDCBA";
const size_t SETSIZE = sizeof( uint64_t) << 3 ;
const size_t BUFSIZE = 256;

uint64_t set_intersect(uint64_t set1, uint64_t set2){
  uint64_t intersect = 0;
  intersect = set1 & set2;
  return intersect;
}

uint64_t set_union(uint64_t set1, uint64_t set2){
  uint64_t union_set = 0;
  union_set = set1 | set2;
  return union_set;
}

uint64_t set_complement( uint64_t set1 ){
  uint64_t reverse = ~set1;
  return reverse;
}

uint64_t set_difference( uint64_t set1, uint64_t set2 ){
  uint64_t diff = set1 & set_complement(set2);
  return diff;
}

uint64_t set_symdifference( uint64_t set1, uint64_t set2 ){
  uint64_t diff = set_difference(set1, set2) | set_difference(set2, set1);
  return diff;
}

size_t set_cardinality( uint64_t set ){
  size_t count;
  for(count = 0; set; set >>=1){
    if(set & 1){
      count += 1;
    }
  }
  return count;
}

char * set_decode( uint64_t set ){
  size_t len = set_cardinality(set);
  size_t count;
  size_t index = 0;
  char *decode = malloc(len+1);
  decode[len] = '\0';
  for(count = 0; set; set >>=1){
      if(set & 1){
        decode[len-index-1] = main_str[count];
        index+=1;
      }
      count += 1;
  }
  return decode;
}


uint64_t set_encode(char * str){
  unsigned long long mask = 1;
  uint64_t set = 0;
  for(size_t x = 0; x < strlen(str); x ++){
    int index = strchr(main_str, str[x])-main_str;
    if(index >= 0){
      set |= mask << index;
    }
  }
  return set;
}

uint64_t file_set_encode(FILE * fp){
  char buffer[256];
  uint64_t set = 0;

  while(fgets(buffer, 256, fp) != NULL){
    uint64_t temp = set_encode(buffer);
    set |= temp;
  }
  return set;
}


int main(int argc, char *argv[]){
  (void)argc;
  FILE *fp1 = fopen(argv[1], "r");
  uint64_t set1;
  uint64_t set2;
  if(fp1){
    set1 = file_set_encode(fp1);
    printf("its lit\n");
  }
  else{
    set1 = set_encode(argv[1]);
  }
  FILE *fp2 = fopen(argv[2], "r");
  if(fp2){
    printf("its lit\n");
    set2 = file_set_encode(fp2);
  }
  else{
    set2 = set_encode(argv[2]);
  }
  printf("set1: %#018llx\n", set1);
  printf("set2: %#018llx\n", set2);

  uint64_t intersect = set_intersect(set1, set2);
  uint64_t union_set = set_union(set1, set2);
  printf("set_intersect: %#018llx\n", intersect);
  printf("set_union: %#018llx\n", union_set);

  uint64_t reverse1 = set_complement(set1);
  uint64_t reverse2 = set_complement(set2);
  printf("set1 set_complement: %#018llx\n", reverse1);
  printf("set2 set_complement: %#018llx\n", reverse2);

  uint64_t diff = set_difference(set1, set2);
  uint64_t diff2 = set_symdifference(set1, set2);
  printf("set_difference: %#018llx\n", diff);
  printf("set_symdifference: %#018llx\n", diff2);

  size_t size1 = set_cardinality(set1);
  size_t size2 = set_cardinality(set2);
  printf("set1 set_cardinality: %zu\n", size1);
  printf("set2 set_cardinality: %zu\n", size2);

  char *mem1 = set_decode(set1);
  char *mem2 = set_decode(set2);
  printf("members of set1: \'%s\'\n", mem1);
  printf("members of set2: \'%s\'\n", mem2);

  return 0;
}
