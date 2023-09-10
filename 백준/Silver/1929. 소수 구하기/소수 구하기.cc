#include <iostream>
#include <stdio.h>
using std::cin;
using std::cout;
int arr[1000001];
int main(){
    int min, max;
    cin >> min;
    cin >> max;
    for(int j = 2; j < max+1; j++){
        if(arr[j]==0){
            for(int m = j+j;m<max+1;m+=j){
                arr[m] = 1;
            }
        }
    }
    arr[0] = 1;
    arr[1] =1;
    for(int k = min; k < max+1;k++){
        if(arr[k]==0){
            printf("%d\n",k);
        }
    }
}