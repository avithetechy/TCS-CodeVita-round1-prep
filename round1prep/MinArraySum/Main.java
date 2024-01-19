import java.util.*;
import java.lang.Math;
class Main{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Enter no of elements:");
		int n = sc.nextInt();
		System.out.print("enter constraints:");
		int x = sc.nextInt();
		int[] arr = new int[n];
		System.out.println("enter elements:");
		for(int i =0;i<n;i++){
		    arr[i]=sc.nextInt();
		}
		for(int i =0;i<n;i++){
		    System.out.println(arr[i]);
		}
		int sum=0;
		int max=0;
		for(int i=0;i<x;i++){
		    for(int j=0;j<n;j++){
		        if(arr[i]>max){
		            max=arr[i];
		        }
		    }
		    for(int l=0;l<n;l++){
		        if(arr[l]==max){
		            arr[l]=Math.floorDiv(max,2);
		        }
		    }
		}
		for(int i=0;i<n;i++){
		    sum=sum+arr[i];
		}
		System.out.println(max);
		for(int i =0;i<n;i++){
		    System.out.println(arr[i]);
		}
		System.out.print("Min sum of Array is:"+sum);
	}
}

