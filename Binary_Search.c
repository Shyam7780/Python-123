#include<stdio.h>
void main(){
  int arr[]={1,2,3,4,5,6,7,8,9,10};
  int st=0,end=sizeof(arr)/sizeof(arr[0])-1;
  int key;
  printf("Enter the Searching Element:->");
  scanf("%d", &key);
  while(st<=end){
    int mid=st+(end-st)/2;
    if(key>arr[mid]){
      st=mid+1;
    }
    else if(key<arr[mid]){
      end=mid+1;

    }
    else{
      printf("Element Found at index:->%d", mid);
      return arr[mid];
    }
  }
  printf("Element Not Found");
  return -1;
}