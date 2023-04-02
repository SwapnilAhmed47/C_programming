#include<stdio.h>

int main(){
    int temp;
    int len=5;
    int arr[5]={2,3,4,5,6};
    int key=3;
    int left = 0;
    int right = len-1;
    while (left<=right){
        int mid_ind = (left + right)/2;
        int mid_val = arr[mid_ind];
        if (key == mid_val){
            printf("%d\n", mid_ind);
            temp = arr[mid_ind];
            break;

        }
        else if (key > mid_val){
            left = mid_ind + 1;
        }
        else{
            right = mid_ind - 1;
        }

    }
    if (key != temp){
        int var = -1;
        printf("%d", var);

    }

    
    return 0;
}