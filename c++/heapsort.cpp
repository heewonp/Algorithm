/* Heap Sort */
/* �� ��Ʈ�� max-heap�� �̿��ؼ� ó���� max-heap���� O(nlogn)���� ��ü�� max-heap���� ���� ����, max���� ��� ����O(long)�����ν�
max-heap�� �ִ� ���� �̴µ� ����ȭ �Ǿ��ִ� ���� �̿��Ѵ�. */

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


