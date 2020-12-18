#include <iostream>
#include <cstring>
using namespace std;

int main(void)
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N; 
	cin >> N;

	int cnt_arr[10001] = {0, };
	for (int i = 0; i < N; i++)
	{
		int temp;
		cin >> temp;
		cnt_arr[temp]++;
	}
	for (int i = 0; i < 10001; i++)
		while (cnt_arr[i]--)
			cout << i << '\n';


	return 0;
}