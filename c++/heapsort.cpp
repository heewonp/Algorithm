/* Heap Sort */
/* 힙 소트는 max-heap을 이용해서 처음에 max-heap으로 O(nlogn)으로 전체를 max-heap으로 만든 다음, max값을 계속 추출O(long)함으로써
max-heap이 최대 값을 뽑는데 최적화 되어있는 것을 이용한다. */

#include <iostream>
using namespace std;

void heapify(int arr[], int size, int rootIndex)
{
	int leftChildIndex = (rootIndex + 1) * 2 - 1; 
	int rightChildIndex = (rootIndex + 1) * 2; 
	int largest = rootIndex;
	
	if (leftChildIndex < size && arr[leftChildIndex] > arr[largest]) 
	{ 
		largest = leftChildIndex;
	} 
	if (rightChildIndex < size && arr[rightChildIndex] > arr[largest]) 
	{ 
		largest = rightChildIndex; 
	}
	if (largest != rootIndex) 
	{ 
		swap(arr[rootIndex], arr[largest]); 
		heapify(arr, size, largest); 
	} 
}

void heapSort(int arr[], int size) 
{
	 for (int i = size / 2 - 1; i >= 0 ; i--) 
	 	{
		 	 heapify(arr, size, i); 
		} 
	for (int i = size - 1 ; i >= 0 ; i--) 
	{ 
		swap(arr[0], arr[i]); 
		heapify(arr, i, 0); 
	} 
}
 
int main() 
{ 
	int arr[] = {4,5,1,6,8,9,3,10, 2}; 
	int size = sizeof(arr) / sizeof(arr[0]); 
	heapSort(arr, size); 
	
	for(int i = 0 ; i < size ; i++) 
	{ 
		cout << arr[i] << " "; 
	} 
	
	return 0; 
}


