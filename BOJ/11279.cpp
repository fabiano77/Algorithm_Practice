#include <iostream>

using namespace std;

void siftdown(int arr[], int i, int q_len)
{
	int parent(i), largechild;
	bool spotFound(false);
	int siftkey = arr[parent];
	while(2*(parent+1) <= q_len && !spotFound)
	{
		if(2*(parent+1) < q_len 
		   && arr[2*parent+1] <arr[2*parent+2])
			largechild = 2*parent+2;
		else 
			largechild = 2*parent+1;
		if(siftkey < arr[largechild])
		{
			arr[parent] = arr[largechild];
			parent = largechild;
		}
		else spotFound = true;
	}
	arr[parent] = siftkey;
}

int main(int argc, char* argv[]) 
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int priority_Q[100000];
	bool isHeap(false);
	int q_len = 0;
	int N;
	cin >> N;
	
	for(int i = 0; i < N; i++)
	{
		
		
		int input;
		cin >> input;
		if(input == 0)
		{
			//pop 출력하는 부분
			if(q_len == 0)
				cout << 0 << '\n';
			else {
				cout << priority_Q[0] << '\n';
				priority_Q[0] = priority_Q[q_len-1];	
				q_len--;
				siftdown(priority_Q, 0, q_len);
			}
				
		}
		else
		{
			//push 하는 부분
			priority_Q[q_len] = input;
			
			int index(q_len);
			while(index && priority_Q[index] > priority_Q[(index-1)/2])
			{
				int temp = priority_Q[index];
				priority_Q[index] = priority_Q[(index-1)/2];
				priority_Q[(index-1)/2] = temp;
				index = (index-1)/2;
			}
			q_len++;
		}
	}
	
	return 0;
}

