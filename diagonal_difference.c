#include <stdio.h>
#include <stdlib.h>

int main(int argc, char * argv[]){
    int n, z, sum = 0;
    scanf("%d", &n);
    
    // Preset the for loops, no need for an array
    for (int i=0; i<n; i++) {
        for (int j=0; j<n; j++) {
            // As we take in the values, check if indexes are on diagonals
            // If so just add/subtract by rows...
            // Instead of one row-other
            scanf("%d",&z);
            if (i==j) {
                sum += z;
            }
            if (n-i-1==j) {
                sum -= z;
            }
        }
    }
    printf("%d", abs(sum));
}