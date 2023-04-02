#include<stdio.h>

int main(){
    int len = 6;
    int arr[6]={5, 3, 8, 6, 7, 2};
    for(int i=0;i<(len-1);i++){
        for(int j=i+1;j<len;j++){
            if arr[j]<arr[i]{
                int temp = arr[j];
                arr[j]   = arr[i];
                arr[i]   = temp;
            }
        }
    }
printf("%d",arr);
    return 0;
}