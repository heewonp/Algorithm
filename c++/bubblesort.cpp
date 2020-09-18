/* Bubble Sott */
/* 버블소트는 항상 연달아 있는 2개의 값을 계속 비교해서 방울이 떠오르는 것과 유사하게
동작하는 정렬이다 */

#include <iostream>
using namespace std;

void bubbleSort(int arr[], int size)
{
	bool isSwap;
	do
	{
		isSwap = false;
		for(int i=1;i<size;i++)
		{
			if(arr[i-1]>arr[i])
			{
				swap(arr[i-1],arr[i]);
				isSwap = true;
			}
		} 
	} while(isSwap);
}

int main()
{
	int arr[] ={9,8,7,4,2,6,1,3, 5};
	int size = sizeof(arr)/sizeof(arr[0]);
	
	bubbleSort(arr,size);
	
	for(int i=0;i<size;i++)
	{
		cout << arr[i] << " ";
	}
	cout << endl;
	
	return 0;
}
